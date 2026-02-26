import argparse
import os
from openapi_python_client.test_api_client import Client
from openapi_python_client.test_api_client.api.db.get_db_test_field1 import sync as get_db_test_field1
from openapi_python_client.test_api_client.api.db.post_db_test_field1 import sync as post_db_test_field1
from openapi_python_client.test_api_client.api.db.get_db_test_testid_test2_field2 import sync as get_db_test_testid_test2_field2
from openapi_python_client.test_api_client.api.db.post_db_test_testid_test2_field2 import sync as post_db_test_testid_test2_field2
from openapi_python_client.test_api_client.models.test_post_request_json import TestPostRequestJson
from openapi_python_client.test_api_client.models.test_2_post_request_json import Test2PostRequestJson


class OpcClient():
  
  def __init__(self,url="http://127.0.0.1:5000"):
    self.url=url

class OpcTest():
  
  def __init__(self,client:OpcClient,field1:str):
    self.client=client
    self.field1=field1

  def post(self,field2:str):
    with Client(base_url=self.client.url) as client:
      body: TestPostRequestJson = TestPostRequestJson(field2)
      post_db_test_field1(client=client,field1=self.field1,body=body)

  def get(self) -> dict:
    with Client(base_url=self.client.url) as client:
      return get_db_test_field1(client=client,field1=self.field1)

  @classmethod
  def arg_post(cls,args):
    test = OpcTest(OpcClient(),args.field1)
    test.post(args.field2)
    
  @classmethod
  def arg_get(cls,args) -> dict:
    test = OpcTest(OpcClient(),args.field1)
    return test.get()

  @classmethod
  def argsp(cls, command):
    parser = command.add_parser("test",help="test endpoint",description="test endpoint")
    methods = parser.add_subparsers(dest="method",help="methods")
    post = methods.add_parser("post",help="post test2",description="post test2")
    post.set_defaults(func=cls.arg_post)
    post.add_argument("field1",help="post field1")
    post.add_argument("field2",help="post field2")
    get = methods.add_parser("get",help="get test2",description="get test2")
    get.set_defaults(func=cls.arg_get)
    get.add_argument("field1",help="get field1")
    
class OpcTest2():
  
  def __init__(self,test:OpcTest,field2:str):
    self.test=test
    self.field2=field2

  def post(self,field3:str):
    with Client(base_url=self.test.client.url) as client:
      body: Test2PostRequestJson = Test2PostRequestJson(field3)
      post_db_test_testid_test2_field2(client=client,
        testid=self.test.field1,
        field2=self.field2,
        body=body)
 
  def get(self) -> dict:
    with Client(base_url=self.test.client.url) as client:
      return get_db_test_testid_test2_field2(client=client,testid="value1",field2="value2")

  @classmethod
  def arg_post(cls,args):
    test = OpcTest(OpcClient(),args.field1)
    test2 = OpcTest2(test,args.field2)
    test2.post(args.field3)

  @classmethod
  def arg_get(cls,args) -> dict:
    test = OpcTest(OpcClient(),args.field1)
    test2 = OpcTest2(test,args.field2)
    return test2.get()

  @classmethod
  def argsp(cls, command):
    parser = command.add_parser("test2",help="test2 endpoint",description="test2 endpoint")
    methods = parser.add_subparsers(dest="method",help="methods")
    post = methods.add_parser("post",help="post test2",description="post test2")
    post.set_defaults(func=cls.arg_post)
    post.add_argument("field1",help="post field1")
    post.add_argument("field2",help="post field2")
    post.add_argument("field3",help="post field3")
    get = methods.add_parser("get",help="test2 get",description="test2 get")
    get.set_defaults(func=cls.arg_get)
    get.add_argument("field1",help="get field1")
    get.add_argument("field2",help="get field2")

def main():
  parser = argparse.ArgumentParser(description="OpcClient")
  command = parser.add_subparsers(dest="command",help="commands")
  OpcTest.argsp(command)
  OpcTest2.argsp(command)
  a = parser.parse_args()
  if not hasattr(a, 'func'):
    parser.print_help()
    os._exit(1)
  print(a.func(a))

if __name__ == "__main__":
  main()
