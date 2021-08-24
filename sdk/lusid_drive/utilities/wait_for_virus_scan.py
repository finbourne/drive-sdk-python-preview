from lusid_drive.utilities import ApiClientFactory
from lusid_drive.utilities.lusid_drive_retry import lusid_drive_retry
import lusid_drive


class WaitForVirusScan():

    def __init__(self, files_api):
        self.files_api = self.api_factory.build(lusid_drive.api.FilesApi)

    @lusid_drive_retry
    def download_file_with_retry(self, filename_id):
        retry = self.files_api.download_file(filename_id)
        return retry