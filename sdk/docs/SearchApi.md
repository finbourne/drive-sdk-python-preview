# lusid_drive.SearchApi

All URIs are relative to *https://fbn-ci.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /api/search | [EXPERIMENTAL] Search for a file or folder with a given name and path


# **search**
> PagedResourceListOfStorageObject search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] Search for a file or folder with a given name and path

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
api_instance = lusid_drive.SearchApi(lusid_drive.ApiClient(configuration))
search_body = {"withPath":"/some/path","name":"filename.pdf"} # SearchBody | Search parameters
page = 'page_example' # str |  (optional)
sort_by = ['sort_by_example'] # list[str] |  (optional)
limit = 56 # int |  (optional)
filter = '' # str |  (optional) (default to '')

try:
    # [EXPERIMENTAL] Search for a file or folder with a given name and path
    api_response = api_instance.search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_body** | [**SearchBody**](SearchBody.md)| Search parameters | 
 **page** | **str**|  | [optional] 
 **sort_by** | [**list[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

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

