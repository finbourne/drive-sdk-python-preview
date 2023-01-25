# lusid_drive.FilesApi

All URIs are relative to *https://fbn-ci.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /api/files | [EARLY ACCESS] CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /api/files/{id} | [EARLY ACCESS] DeleteFile: Deletes a file from Drive.
[**download_file**](FilesApi.md#download_file) | **GET** /api/files/{id}/contents | [EARLY ACCESS] DownloadFile: Download the file from Drive.
[**get_file**](FilesApi.md#get_file) | **GET** /api/files/{id} | [EARLY ACCESS] GetFile: Get a file stored in Drive.
[**update_file_contents**](FilesApi.md#update_file_contents) | **PUT** /api/files/{id}/contents | [EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.
[**update_file_metadata**](FilesApi.md#update_file_metadata) | **PUT** /api/files/{id} | [EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.


# **create_file**
> StorageObject create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body)

[EARLY ACCESS] CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/drive
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_drive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_drive.FilesApi(api_client)
    x_lusid_drive_filename = 'x_lusid_drive_filename_example' # str | File name.
x_lusid_drive_path = 'x_lusid_drive_path_example' # str | File path.
content_length = 56 # int | The size in bytes of the file to be uploaded
body = 'body_example' # str | 

    try:
        # [EARLY ACCESS] CreateFile: Uploads a file to Lusid Drive. If using an SDK, consider using the UploadAsStreamAsync function for larger files instead.
        api_response = api_instance.create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_lusid_drive_filename** | **str**| File name. | 
 **x_lusid_drive_path** | **str**| File path. | 
 **content_length** | **int**| The size in bytes of the file to be uploaded | 
 **body** | **str**|  | 

### Return type

[**StorageObject**](StorageObject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(id)

[EARLY ACCESS] DeleteFile: Deletes a file from Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/drive
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_drive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_drive.FilesApi(api_client)
    id = 'id_example' # str | Identifier of the file to be deleted.

    try:
        # [EARLY ACCESS] DeleteFile: Deletes a file from Drive.
        api_instance.delete_file(id)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be deleted. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(id)

[EARLY ACCESS] DownloadFile: Download the file from Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/drive
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_drive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_drive.FilesApi(api_client)
    id = 'id_example' # str | Identifier of the file to be downloaded.

    try:
        # [EARLY ACCESS] DownloadFile: Download the file from Drive.
        api_response = api_instance.download_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be downloaded. | 

### Return type

**file**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**410** | Malware detected, restricted from downloading file. |  -  |
**423** | Virus scan in progress, restricted from downloading file. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> StorageObject get_file(id)

[EARLY ACCESS] GetFile: Get a file stored in Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/drive
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_drive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_drive.FilesApi(api_client)
    id = 'id_example' # str | Identifier of the file to be retrieved.

    try:
        # [EARLY ACCESS] GetFile: Get a file stored in Drive.
        api_response = api_instance.get_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be retrieved. | 

### Return type

[**StorageObject**](StorageObject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_contents**
> StorageObject update_file_contents(id, content_length, body)

[EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/drive
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_drive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_drive.FilesApi(api_client)
    id = 'id_example' # str | The unique file identifier
content_length = 56 # int | The size in bytes of the file to be uploaded
body = 'body_example' # str | 

    try:
        # [EARLY ACCESS] UpdateFileContents: Updates contents of a file in Drive.
        api_response = api_instance.update_file_contents(id, content_length, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->update_file_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique file identifier | 
 **content_length** | **int**| The size in bytes of the file to be uploaded | 
 **body** | **str**|  | 

### Return type

[**StorageObject**](StorageObject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_metadata**
> StorageObject update_file_metadata(id, update_file)

[EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/drive
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_drive.Configuration(
    host = "https://fbn-ci.lusid.com/drive"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_drive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_drive.FilesApi(api_client)
    id = 'id_example' # str | Identifier of the file to be updated
update_file = {"path":"/New/parent/folder/path","name":"new-file-name"} # UpdateFile | Update to be applied to file

    try:
        # [EARLY ACCESS] UpdateFileMetadata: Updates metadata for a file in Drive.
        api_response = api_instance.update_file_metadata(id, update_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->update_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file to be updated | 
 **update_file** | [**UpdateFile**](UpdateFile.md)| Update to be applied to file | 

### Return type

[**StorageObject**](StorageObject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

