# TestGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**field1** | **str** |  | 
**field2** | **str** |  | 

## Example

```python
from openapi_client.models.test_get_response import TestGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestGetResponse from a JSON string
test_get_response_instance = TestGetResponse.from_json(json)
# print the JSON string representation of the object
print(TestGetResponse.to_json())

# convert the object into a dict
test_get_response_dict = test_get_response_instance.to_dict()
# create an instance of TestGetResponse from a dict
test_get_response_from_dict = TestGetResponse.from_dict(test_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


