# Test2GetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**test_id** | **str** |  | 
**created** | **str** |  | 
**field2** | **str** |  | 
**field3** | **str** |  | 

## Example

```python
from openapi_client.models.test2_get_response import Test2GetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Test2GetResponse from a JSON string
test2_get_response_instance = Test2GetResponse.from_json(json)
# print the JSON string representation of the object
print(Test2GetResponse.to_json())

# convert the object into a dict
test2_get_response_dict = test2_get_response_instance.to_dict()
# create an instance of Test2GetResponse from a dict
test2_get_response_from_dict = Test2GetResponse.from_dict(test2_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


