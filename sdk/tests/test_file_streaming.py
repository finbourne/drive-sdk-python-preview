import logging
import unittest

from lusid_drive import ApiConfigurationLoader, SearchApi, SearchBody
from lusid_drive.utilities import ApiClientFactory, stream_file_download


class FileStreaming(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        config = ApiConfigurationLoader.load("secrets.json")

        cls.api_factory = ApiClientFactory(token=config.api_token, api_url=config.drive_url,
                                           api_secrets_filename="secrets.json")

    def test_stream_file_download(self):

        file_root = "/"
        filename = "55e09fdd-ea50-4561-b68c-0ed9b31a0ff9"

        response = self.api_factory.build(SearchApi).search(
            search_body=SearchBody(with_path=file_root, name=filename)
        )

        if response.values is None or len(response.values) != 1:
            self.fail(f"Unexpected result for path {'/'.join([file_root, filename])}, {len(response.values)} results returned")

        stream = stream_file_download(self.api_factory, response.values[0].id)



if __name__ == '__main__':
    unittest.main()
