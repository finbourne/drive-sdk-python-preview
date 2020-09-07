# lusid_drive.ApplicationMetadataApi

All URIs are relative to *https://fbn-ci.lusid.com/drive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_access_controlled_resources**](ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | [EARLY ACCESS] Get resources available for access control


# **list_access_controlled_resources**
> ResourceListOfAccessControlledResource list_access_controlled_resources()

[EARLY ACCESS] Get resources available for access control

Get the comprehensive set of resources that are available for access control

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
api_instance = lusid_drive.ApplicationMetadataApi(lusid_drive.ApiClient(configuration))

try:
    # [EARLY ACCESS] Get resources available for access control
    api_response = api_instance.list_access_controlled_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationMetadataApi->list_access_controlled_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

