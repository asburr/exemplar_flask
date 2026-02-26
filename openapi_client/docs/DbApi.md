# openapi_client.DbApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_test_field1_get**](DbApi.md#db_test_field1_get) | **GET** /db/test/{field1} | Get row from test.
[**db_test_field1_post**](DbApi.md#db_test_field1_post) | **POST** /db/test/{field1} | Add row into test.
[**db_test_testid_test2_field2_get**](DbApi.md#db_test_testid_test2_field2_get) | **GET** /db/test/{testid}/test2/{field2} | Get row from test2.
[**db_test_testid_test2_field2_post**](DbApi.md#db_test_testid_test2_field2_post) | **POST** /db/test/{testid}/test2/{field2} | Add row to test2 with foreign key to test.


# **db_test_field1_get**
> Generated2 db_test_field1_get(field1)

Get row from test.

### Example


```python
import openapi_client
from openapi_client.models.generated2 import Generated2
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DbApi(api_client)
    field1 = 'field1_example' # str | 

    try:
        # Get row from test.
        api_response = api_instance.db_test_field1_get(field1)
        print("The response of DbApi->db_test_field1_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DbApi->db_test_field1_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field1** | **str**|  | 

### Return type

[**Generated2**](Generated2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_test_field1_post**
> object db_test_field1_post(field1, generated)

Add row into test.

### Example


```python
import openapi_client
from openapi_client.models.generated import Generated
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DbApi(api_client)
    field1 = 'field1_example' # str | 
    generated = openapi_client.Generated() # Generated | 

    try:
        # Add row into test.
        api_response = api_instance.db_test_field1_post(field1, generated)
        print("The response of DbApi->db_test_field1_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DbApi->db_test_field1_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field1** | **str**|  | 
 **generated** | [**Generated**](Generated.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_test_testid_test2_field2_get**
> Generated5 db_test_testid_test2_field2_get(testid, field2)

Get row from test2.

### Example


```python
import openapi_client
from openapi_client.models.generated5 import Generated5
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DbApi(api_client)
    testid = 'testid_example' # str | 
    field2 = 'field2_example' # str | 

    try:
        # Get row from test2.
        api_response = api_instance.db_test_testid_test2_field2_get(testid, field2)
        print("The response of DbApi->db_test_testid_test2_field2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DbApi->db_test_testid_test2_field2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testid** | **str**|  | 
 **field2** | **str**|  | 

### Return type

[**Generated5**](Generated5.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_test_testid_test2_field2_post**
> object db_test_testid_test2_field2_post(testid, field2, generated3)

Add row to test2 with foreign key to test.

### Example


```python
import openapi_client
from openapi_client.models.generated3 import Generated3
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DbApi(api_client)
    testid = 'testid_example' # str | 
    field2 = 'field2_example' # str | 
    generated3 = openapi_client.Generated3() # Generated3 | 

    try:
        # Add row to test2 with foreign key to test.
        api_response = api_instance.db_test_testid_test2_field2_post(testid, field2, generated3)
        print("The response of DbApi->db_test_testid_test2_field2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DbApi->db_test_testid_test2_field2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testid** | **str**|  | 
 **field2** | **str**|  | 
 **generated3** | [**Generated3**](Generated3.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

