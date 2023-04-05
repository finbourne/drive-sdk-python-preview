import json
import logging
import os
import unittest

from lusid_drive import ApiConfigurationLoader, SearchApi, SearchBody, FilesApi, FoldersApi, ApiException, models
from lusid_drive.utilities import ApiClientFactory, get_file_id, get_folder_id
from lusid_drive.utilities.file_streaming import stream_file_upload
from pprint import pprint

class FileStreaming(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)
        config = ApiConfigurationLoader.load(os.path.join(os.getcwd(), "secrets.json"))

        cls.api_factory = ApiClientFactory(
            token=config.api_token,
            drive_url=config.drive_url,
            api_secrets_filename=os.path.join(os.getcwd(), "secrets.json"))

        cls.folder_api = cls.api_factory.build(FoldersApi)
        cls.files_api = cls.api_factory.build(FilesApi)

        cls.test_folder_name = "sdk-test-folder"
        cls.create_test_file_name = "create_test_stream_file.txt"
        cls.download_test_file_name = "download_test_stream_file.txt"
        cls.local_file_path = os.path.join(os.path.dirname(__file__), "data", "test_stream_file.txt")

        # create the test folder
        try:
            cls.folder_api.create_folder(models.CreateFolder(path="/", name=cls.test_folder_name))
        except ApiException as e:
            pprint(e)
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
                    raise ApiException(reason=reason)

            except ApiException as e:
                if json.loads(e.body)["code"] == 671:
                    # a file with this name already exists in the path
                    cls.logger.info(json.loads(e.body)["detail"])

        # create the test files for the download test
        create_file(cls.download_test_file_name, cls.test_folder_name, cls.local_file_path)

        # make sure the file to be created in the upload test does not already exist
        try:
            folder_id = get_folder_id(cls.api_factory, cls.test_folder_name)
            file_id = get_file_id(cls.api_factory, cls.create_test_file_name, folder_id)
            if file_id is not None:
                cls.files_api.delete_file(file_id)
            else:
                cls.logger.info("File does not exist")

        except ApiException as e:
            # either the folder or the file does not exist
            cls.logger.info("File or directory does not exist" + ":" + json.loads(e.body)["detail"])

    @classmethod
    def tearDownClass(cls) -> None:

        def delete_file(file_name, folder_name):
            _folder_id = get_folder_id(cls.api_factory, folder_name)
            _file_id = get_file_id(cls.api_factory, file_name, _folder_id)
            if _file_id is not None:
                cls.files_api.delete_file(_file_id)

        # delete upload test file
        delete_file(cls.create_test_file_name, cls.test_folder_name)

        # delete download test file
        delete_file(cls.download_test_file_name, cls.test_folder_name)

        # delete test folder
        folder_id = get_folder_id(cls.api_factory, cls.test_folder_name)
        cls.folder_api.delete_folder(folder_id)

    def test_stream_file_download(self):
        # arrange
        response = self.api_factory.build(SearchApi).search(
            search_body=SearchBody(with_path=f"/{self.test_folder_name}", name=self.download_test_file_name)
        )

        if response.values is None or len(response.values) != 1:
            self.fail(
                f"Unexpected result for path {'/'.join([self.test_folder_name, self.download_test_file_name])}, "
                f"{len(response.values)} results returned")

        with open(self.local_file_path, "r") as local_file:
            expected = local_file.read()

        # act
        with self.api_factory.build(FilesApi).download_file(response.values[0].id, _preload_content=False) as stream:

            # assert
            actual = stream.read().decode("utf-8")
            self.assertEqual(actual, expected)

    def test_stream_file_upload(self):
        # arrange
        with open(self.local_file_path, 'rb') as data:
            # act
            response = stream_file_upload(
                x_lusid_drive_filename=self.create_test_file_name,
                x_lusid_drive_path=f"/{self.test_folder_name}",
                content_length=os.stat(self.local_file_path).st_size,
                body=data,
                api_factory=self.api_factory
            )
            # assert
            self.assertEqual(self.create_test_file_name, response.name)


if __name__ == '__main__':
    unittest.main()
