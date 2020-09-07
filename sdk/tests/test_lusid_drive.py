import unittest
import json
import logging
import os
from pathlib import Path

import lusid_drive
import lusid_drive.utilities.utility_functions as utilities
from lusid_drive import models as models
from lusid_drive.utilities import ApiClientFactory
from lusid_drive.utilities import ApiConfigurationLoader


class LusidDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        config = ApiConfigurationLoader.load("secrets.json")

        cls.api_factory = ApiClientFactory(token=config.api_token, api_url=config.api_url)
        cls.folder_api = cls.api_factory.build(lusid_drive.api.FoldersApi)
        cls.files_api = cls.api_factory.build(lusid_drive.api.FilesApi)

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
                response = cls.files_api.create_file(
                    x_lusid_drive_filename=file_name,
                    x_lusid_drive_path=f"/{folder_name}",
                    content_length=os.stat(local_path).st_size,
                    body=local_path
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

        get_folder = self.folder_api.get_root_folder()

        list_root_contents = ([folder.name for folder in get_folder.values])

        self.assertIn(self.test_folder_name, list_root_contents)

    def test_create_file(self):

        response = self.files_api.create_file(
            x_lusid_drive_filename=self.create_test_file_name,
            x_lusid_drive_path=f"/{self.test_folder_name}",
            content_length=os.stat(self.local_file_path).st_size,
            body=self.local_file_path
        )
        self.assertEqual(self.create_test_file_name, response.name)

    def test_download_file(self):

        folder_id = utilities.get_folder_id(self.api_factory, self.test_folder_name)
        file_id = utilities.get_file_id(self.api_factory, self.download_test_file_name, folder_id)
        response = self.files_api.download_file(file_id)
        self.assertIn(self.download_test_file_name, response)

    def test_delete_file(self):

        folder_id = utilities.get_folder_id(self.api_factory, self.test_folder_name)
        file_id = utilities.get_file_id(self.api_factory, self.delete_test_file_name, folder_id)
        response = self.files_api.delete_file(file_id)
        self.assertEqual(None, response)


if __name__ == '__main__':
    unittest.main()
