import lusid_drive
import lusid_drive.models as models
import json
import logging

logger = logging.getLogger("drive-logger")
logger.setLevel("INFO")


def create_folder(api_factory, folder_path, folder_name):
    """
    This function creates a new folder on LUSID Drive.

    param api_factory ApiClientFactory: A LUSID Drive API Factory
    param folder_path str: The folder path on LUSID Drive
    param folder_path str: The new folder name on LUSID Drive

    returns: a CreateFolder responses

    """

    folder_api = api_factory.build(lusid_drive.api.FoldersApi)

    try:

        create_folder_request = folder_api.create_folder(
            create_folder=models.CreateFolder(folder_path, folder_name))

        return create_folder_request

    except lusid_drive.ApiException as e:

        if json.loads(e.body)["code"] == 664:

            return json.loads(e.body)["detail"]


def create_all_folders_in_path(api_factory, folder_path):
    """
    This function create a folder recursively.
    For example, we can pass a new path "/a/b/c/d", and the function will recursively create the four API calls
    to create:
        /a
        /a/b
        /a/b/c
        /a/b/c/d

    :param api_factory ApiClientFactory: A LUSID Drive API Factory
    :param folder_path str: The new folder path on LUSID Drive

    returns: A list of CreateFolder responses
    """

    sub_dirs = [i for i in folder_path.split("/") if i != ""]

    path = "/"

    create_folder_requests = []

    for elem in sub_dirs:

        resp = create_folder(api_factory, path, elem)

        create_folder_requests.append(resp)

        path += elem + "/"

    return create_folder_requests


def path_to_drive_api_parms(drive_path):
    """
    Function to conver path of format /abc/def/text1 to a format suitable for the SearchApi

    :param drive_path str: The path on LUSID Drive

    returns: a tuple of (folder_path, folder_name). For example, the string "/abc/def/text1"
    would return ("/abc/def", "text1")
    """

    if drive_path.count("/") == 1:

        folder_path = "/"

        f_name = drive_path[1:]

    else:

        folder_path = drive_path[:drive_path.rfind("/")]

        f_name = drive_path[drive_path.rfind("/") + 1:]

    return (folder_path, f_name)


def delete_folder(api_factory, drive_path):
    """
    Function to delete folder on Drive

    :param api_factory ApiClientFactory: A LUSID Drive API Factory
    :param folder_path str: The folder path on LUSID Drive
    """

    if not drive_path.startswith("/"):
        logger.info("The folder_path must start with a forward slash /")

    paths = path_to_drive_api_parms(drive_path)

    folder_path = paths[0]
    folder_name = paths[1]

    folder_api = api_factory.build(lusid_drive.api.FoldersApi)
    search_api = api_factory.build(lusid_drive.api.SearchApi)

    search_file = search_api.search(search_body=models.SearchBody(with_path=folder_path, name=folder_name)).values

    if len(search_file) > 0:

        folder_ids = [i.id for i in search_file]

        folder_to_delete = []

        for i in folder_ids:

            delete_response = folder_api.delete_folder(id=i)

            folder_to_delete.append(delete_response)

        return folder_to_delete

    else:

        logger.info(f"The folder {drive_path} does not exist in LUSID Drive")



