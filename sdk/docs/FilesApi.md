# lusid_drive.FilesApi

All URIs are relative to *https://fbn-ci.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /api/files | [EXPERIMENTAL] Uploads a file to Lusid Drive.
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /api/files/{id} | [EXPERIMENTAL] Deletes a file from Drive.
[**download_file**](FilesApi.md#download_file) | **GET** /api/files/{id}/contents | [EXPERIMENTAL] Download the file from Drive.
[**get_file**](FilesApi.md#get_file) | **GET** /api/files/{id} | [EXPERIMENTAL] Get a file stored in Drive.
[**update_file_contents**](FilesApi.md#update_file_contents) | **PUT** /api/files/{id}/contents | [EXPERIMENTAL] Updates contents of a file in Drive.
[**update_file_metadata**](FilesApi.md#update_file_metadata) | **PUT** /api/files/{id} | [EXPERIMENTAL] Updates metadata for a file in Drive.


# **create_file**
> StorageObject create_file(x_lusid_drive_filename, x_lusid_drive_path, content_length, body)

[EXPERIMENTAL] Uploads a file to Lusid Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
configuration = lusid_drive.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/drive
configuration.host = "https://fbn-ci.lusid.com/drive"
# Create an instance of the API class
api_instance = lusid_drive.FilesApi(lusid_drive.ApiClient(configuration))
x_lusid_drive_filename = 'x_lusid_drive_filename_example' # str | File name.
x_lusid_drive_path = 'x_lusid_drive_path_example' # str | File path.
content_length = 56 # int | The size in bytes of the file to be uploaded
body = '/path/to/file' # file | 

try:
    # [EXPERIMENTAL] Uploads a file to Lusid Drive.
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
 **body** | **file**|  | 

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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(id)

[EXPERIMENTAL] Deletes a file from Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
configuration = lusid_drive.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/drive
configuration.host = "https://fbn-ci.lusid.com/drive"
# Create an instance of the API class
api_instance = lusid_drive.FilesApi(lusid_drive.ApiClient(configuration))
id = 'id_example' # str | Identifier of the file to be deleted.

try:
    # [EXPERIMENTAL] Deletes a file from Drive.
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
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(id)

[EXPERIMENTAL] Download the file from Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
configuration = lusid_drive.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/drive
configuration.host = "https://fbn-ci.lusid.com/drive"
# Create an instance of the API class
api_instance = lusid_drive.FilesApi(lusid_drive.ApiClient(configuration))
id = 'id_example' # str | Identifier of the file to be downloaded.

try:
    # [EXPERIMENTAL] Download the file from Drive.
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
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> StorageObject get_file(id)

[EXPERIMENTAL] Get a file stored in Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
configuration = lusid_drive.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/drive
configuration.host = "https://fbn-ci.lusid.com/drive"
# Create an instance of the API class
api_instance = lusid_drive.FilesApi(lusid_drive.ApiClient(configuration))
id = 'id_example' # str | Identifier of the file to be retrieved.

try:
    # [EXPERIMENTAL] Get a file stored in Drive.
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

[EXPERIMENTAL] Updates contents of a file in Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
configuration = lusid_drive.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/drive
configuration.host = "https://fbn-ci.lusid.com/drive"
# Create an instance of the API class
api_instance = lusid_drive.FilesApi(lusid_drive.ApiClient(configuration))
id = 'id_example' # str | The unique file identifier
content_length = 56 # int | The size in bytes of the file to be uploaded
body = '/path/to/file' # file | 

try:
    # [EXPERIMENTAL] Updates contents of a file in Drive.
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
 **body** | **file**|  | 

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

[EXPERIMENTAL] Updates metadata for a file in Drive.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_drive
from lusid_drive.rest import ApiException
from pprint import pprint
configuration = lusid_drive.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/drive
configuration.host = "https://fbn-ci.lusid.com/drive"
# Create an instance of the API class
api_instance = lusid_drive.FilesApi(lusid_drive.ApiClient(configuration))
id = 'id_example' # str | Identifier of the file to be updated
update_file = {"path":"/New/parent/folder/path","name":"new-file-name"} # UpdateFile | Update to be applied to file

try:
    # [EXPERIMENTAL] Updates metadata for a file in Drive.
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

