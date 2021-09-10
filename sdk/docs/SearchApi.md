# lusid_drive.SearchApi

All URIs are relative to *https://fbn-ci.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /api/search | [BETA] Search for a file or folder with a given name and path


# **search**
> PagedResourceListOfStorageObject search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter)

[BETA] Search for a file or folder with a given name and path

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
    api_instance = lusid_drive.SearchApi(api_client)
    search_body = {"withPath":"/some/path","name":"filename.pdf"} # SearchBody | Search parameters
page = 'page_example' # str |  (optional)
sort_by = ['sort_by_example'] # list[str] |  (optional)
limit = 56 # int |  (optional)
filter = '' # str |  (optional) (default to '')

    try:
        # [BETA] Search for a file or folder with a given name and path
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

