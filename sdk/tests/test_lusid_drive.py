import unittest
import json
import logging
import os
import lusid_drive
import lusid_drive.utilities.utility_functions as utilities

from lusid_drive import models as models, ApiException, FilesApi
from lusid_drive.utilities import ApiClientFactory
from lusid_drive.utilities.wait_for_virus_scan import WaitForVirusScan
from lusid_drive.utilities import ApiConfigurationLoader
from lusid_drive.utilities.folders_api_extensions import create_all_folders_in_path, delete_folder, path_to_search_api_parms, drive_path_formatter
from unittest.mock import patch, Mock
from parameterized import parameterized

class MockApiResponse(object):
    def __init__(self, status=None):
        self.status = status
        self.headers = {}


class LusidDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        config = ApiConfigurationLoader.load("secrets.json")

        cls.api_factory = ApiClientFactory(
            token=config.api_token,
            drive_url=config.drive_url,
            api_secrets_filename=os.path.join(os.getcwd(), "secrets.json"))

        cls.folder_api = cls.api_factory.build(lusid_drive.api.FoldersApi)
        cls.files_api = cls.api_factory.build(lusid_drive.api.FilesApi)
        cls.search_api = cls.api_factory.build(lusid_drive.api.SearchApi)

        cls.test_folder_name = "sdk-test-folder"
        cls.create_test_file_name = "create_test_file.txt"
        cls.download_test_file_name = "download_test_file.txt"
        cls.delete_test_file_name = "delete_test_file.txt"
        cls.local_file_path = os.path.join(os.path.dirname(__file__), "data", "test_file.txt")

        # create the test folder
        try:
            cls.folder_api.create_folder(models.CreateFolder(path="/", name=cls.test_folder_name))

        except lusid_drive.exceptions.ApiException as e:
            if json.loads(e.body)["code"] == 664:
                # a folder with this name already exists in the path
                cls.logger.info(json.loads(e.body)["detail"])

        # define function for creating required testing files

        def create_file(file_name, folder_name, local_path):
            try:
                with open(local_path, 'rb') as data:
                    response = cls.files_api.create_file(
                        x_lusid_drive_filename=file_name,
                        x_lusid_drive_path=f"/{folder_name}",
                        content_length=os.stat(local_path).st_size,
                        body=data.read()
                    )

                if file_name not in response.name:
                    reason = f"{file_name} not successfully created"
                    cls.logger.info(reason)
                    raise lusid_drive.exceptions.ApiException(reason=reason)

            except lusid_drive.exceptions.ApiException as e:
                if json.loads(e.body)["code"] == 671:
                    # a file with this name already exists in the path
                    cls.logger.info(json.loads(e.body)["detail"])

        # create the test files for the download test
        create_file(cls.download_test_file_name, cls.test_folder_name, cls.local_file_path)

        # create the test files for the delete test
        create_file(cls.delete_test_file_name, cls.test_folder_name, cls.local_file_path)

        # make sure the file to be created in the create test does not already exist
        try:
            folder_id = utilities.get_folder_id(cls.api_factory, cls.test_folder_name)
            file_id = utilities.get_file_id(cls.api_factory, cls.create_test_file_name, folder_id)
            if file_id is not None:
                cls.files_api.delete_file(file_id)
            else:
                cls.logger.info("File does not exist")

        except lusid_drive.exceptions.ApiException as e:
            # either the folder or the file does not exist
            cls.logger.info("File or directory does not exist" + ":" + json.loads(e.body)["detail"])

    @classmethod
    def tearDownClass(cls) -> None:

        def delete_file(file_name, folder_name):
            _folder_id = utilities.get_folder_id(cls.api_factory, folder_name)
            _file_id = utilities.get_file_id(cls.api_factory, file_name, _folder_id)
            if _file_id is not None:
                cls.files_api.delete_file(_file_id)

        # delete create test file
        delete_file(cls.create_test_file_name, cls.test_folder_name)

        # delete download test file
        delete_file(cls.download_test_file_name, cls.test_folder_name)

        # delete delete test file if exists
        delete_file(cls.delete_test_file_name, cls.test_folder_name)

        # delete test folder
        folder_id = utilities.get_folder_id(cls.api_factory, cls.test_folder_name)
        cls.folder_api.delete_folder(folder_id)

    def test_get_folder(self):

        get_folder = self.folder_api.get_root_folder(filter=f"name eq '{self.test_folder_name}' and type eq 'Folder'")

        list_root_contents = ([folder.name for folder in get_folder.values])

        self.assertEqual([self.test_folder_name], list_root_contents)

    def test_create_file(self):

        with open(self.local_file_path, 'rb') as data:
            response = self.files_api.create_file(
                x_lusid_drive_filename=self.create_test_file_name,
                x_lusid_drive_path=f"/{self.test_folder_name}",
                content_length=os.stat(self.local_file_path).st_size,
                body=data.read()
            )
            self.assertEqual(self.create_test_file_name, response.name)

    def test_download_file(self):

        folder_id = utilities.get_folder_id(self.api_factory, self.test_folder_name)
        file_id = utilities.get_file_id(self.api_factory, self.download_test_file_name, folder_id)
        response = self.files_api.download_file(file_id)
        self.assertIn(self.download_test_file_name, response)

    def _test_virus_scan(self):

        folder_id = utilities.get_folder_id(self.api_factory, self.test_folder_name)

        mock_download = Mock()
        mock_download.side_effect = [
            ApiException(status=423),
            ApiException(status=423),
            MockApiResponse(status=201)
        ]

        with patch.object(FilesApi, "download_file", side_effect=mock_download) as download_mock:
            wait = WaitForVirusScan(self.files_api)
            download = wait.download_file_with_retry(folder_id)

            self.assertEqual(3, download_mock.call_count)

    def test_delete_file(self):

        folder_id = utilities.get_folder_id(self.api_factory, self.test_folder_name)
        file_id = utilities.get_file_id(self.api_factory, self.delete_test_file_name, folder_id)
        response = self.files_api.delete_file(file_id)
        self.assertEqual(None, response)

    @parameterized.expand([
        ["/sdk-tests-delete-folder-1/test1/test2"],
        ["sdk-tests-delete-folder/test1/test2"],
        ["/sdk-tests-delete-folder-1"],
        ["sdk-tests-delete-folder"]
    ])
    def test_create_folder(self, folder_name):

        create_folder_request = create_all_folders_in_path(self.api_factory, folder_name)

        search_api_params = path_to_search_api_parms(folder_name)
        path_for_search_api = search_api_params[0]
        name_for_search_api = search_api_params[1]

        get_folder = self.search_api.search(search_body=models.SearchBody(
            with_path=path_for_search_api, name=name_for_search_api))

        get_folder_path = get_folder.values[0].path
        get_folder_name = get_folder.values[0].name

        self.assertEqual(get_folder_path, path_for_search_api)
        self.assertEqual(get_folder_name, name_for_search_api)

        big_string_path = "/abc" * 1000

        with self.assertRaises(ValueError) as error:

            create_folder_request = create_all_folders_in_path(self.api_factory, big_string_path)

        self.assertEqual(str(error.exception), 'Path length must be less than 1024 characters')

    @parameterized.expand([
        ["/sdk-tests-delete-folder-1/test1/test2"],
        ["sdk-tests-delete-folder/test1/test2"],
        ["/sdk-tests-delete-folder-1"],
        ["sdk-tests-delete-folder"]
    ])
    def test_delete_folder(self, full_folder_path):

        search_api_params = path_to_search_api_parms(full_folder_path)
        path_for_search_api = search_api_params[0]
        name_for_search_api = search_api_params[1]

        create_folder_request = create_all_folders_in_path(self.api_factory, full_folder_path)

        get_folder_before_delete = self.search_api.search(search_body=models.SearchBody(
            with_path=path_for_search_api, name=name_for_search_api)).values

        delete_folder_request = delete_folder(self.api_factory, full_folder_path)

        get_folder_after_delete = self.search_api.search(search_body=models.SearchBody(
            with_path=path_for_search_api, name=name_for_search_api)).values

        self.assertTrue(len(get_folder_before_delete) > 0)
        self.assertTrue(len(get_folder_after_delete) == 0)


    @parameterized.expand([
        ["/drive-sdk/path/test/format"],
        ["/drive-sdk/path/test/format/"],
        ["drive-sdk/path/test/format"],
        ["drive-sdk/path/test/format/"]
    ])
    def test_path_to_search_api_params(self, paths):

        search_api_params = path_to_search_api_parms(paths)

        self.assertEqual(search_api_params, ("/drive-sdk/path/test", "format"))

    @parameterized.expand([
        ["/drive-sdk/path/test/format", "/drive-sdk/path/test/format"],
        ["/drive-sdk/path/test/format/", "/drive-sdk/path/test/format"],
        ["drive-sdk/path/test/format", "/drive-sdk/path/test/format"],
        ["drive-sdk/path/test/format/", "/drive-sdk/path/test/format"]
    ])
    def test_drive_path_formatter(self, input_path, correct_path):

        updated_drive_path = drive_path_formatter(input_path)

        self.assertEqual(updated_drive_path, correct_path)


if __name__ == '__main__':
    unittest.main()
