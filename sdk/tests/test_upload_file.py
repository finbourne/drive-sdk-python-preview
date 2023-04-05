import unittest
import lusid_drive
import os
from unittest import mock
from lusid_drive.utilities import upload_file
from lusid_drive.rest import ApiException



class TestDriveFileUpload(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.local_file_path = os.path.join(os.path.dirname(__file__), "data", "test_file.txt")
    
    def test_upload_file_positive(self) -> None:
        """
        Test that a file can be created successfully

        :return: None
        """
        api_client_mock = lusid_drive.FilesApi()
        api_client_mock.create_file = mock.MagicMock()

        with open(self.local_file_path, mode="r") as file:
            body = file.read()

        x_lusid_drive_filename = 'test_file.txt' # str | File name.
        x_lusid_drive_path = '/' # str | Drive path.
       
        upload_file(api_client_mock,x_lusid_drive_filename, x_lusid_drive_path, body)
        api_client_mock.create_file.assert_called_once_with(x_lusid_drive_filename='test_file.txt', x_lusid_drive_path='/', content_length=77018, body=body)

    def test_upload_file_already_exists(self) -> None:
        """
        Test uploading a file when it already exists

        :return: None
        """
        api_client_mock = lusid_drive.FilesApi()

        http_resp = mock.MagicMock()
        http_resp.data = '{"code": 671}'

        api_client_mock.create_file = mock.MagicMock()
        api_client_mock.create_file.side_effect = lusid_drive.ApiException(http_resp= http_resp)

        with open(self.local_file_path, mode="r") as file:
            body = file.read()

        x_lusid_drive_filename = 'test_file.txt' # str | File name.
        x_lusid_drive_path = '/' # str | Drive path.
       
        upload_file(api_client_mock,x_lusid_drive_filename, x_lusid_drive_path, body)
        api_client_mock.create_file.assert_called_once_with(x_lusid_drive_filename='test_file.txt', x_lusid_drive_path='/', content_length=77018, body=body)

    def test_upload_file_exception(self) -> None:
        """
        Test uploading a file which raises any other exception other than file_already_exists

        :return: None
        """
        api_client_mock = lusid_drive.FilesApi()
        http_resp = mock.MagicMock()

        #Testing any code other than 671 (File already exists)
        http_resp.data = '{"code": 111}'
        api_client_mock.create_file = mock.MagicMock()

        api_client_mock.create_file.side_effect = lusid_drive.ApiException(http_resp= http_resp)
        
        with open(self.local_file_path, mode="r") as file:
            body = file.read()

        x_lusid_drive_filename = 'test_file.txt' # str | File name.
        x_lusid_drive_path = '/' # str | Drive path.
        with self.assertRaises(ApiException):
            upload_file(api_client_mock,x_lusid_drive_filename, x_lusid_drive_path, body)