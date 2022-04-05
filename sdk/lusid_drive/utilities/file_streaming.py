import urllib3

from lusid_drive import ApiException


def stream_file_download(files_api, id):

    if id is None or id == "":
        raise ApiException(400, "Missing required parameter 'id")

    urllib3.request(
        "GET",
        f"/api/files/{id}/contents"
    )
