import argparse
import os
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient
from openapi_client.api.db_api import DbApi
from openapi_client.models.test_post_request_json import TestPostRequestJson
from openapi_client.models.test2_post_request_json import Test2PostRequestJson


class OpClient():
  
  def __init__(self,url="http://127.0.0.1:5000"):
    self.configuration = Configuration( host = url )

class OpTest():
  
  def __init__(self,client:OpClient,field1:str):
    self.client=client
    self.field1=field1

  def post(self,field2:str):
    with ApiClient(self.client.configuration) as api_client:
      api = DbApi(api_client)
      body = TestPostRequestJson(field2=field2)
      api.db_test_field1_post(self.field1,body)

  def get(self) -> dict:
    with ApiClient(self.client.configuration) as api_client:
      api = DbApi(api_client)
      return api.db_test_field1_get(self.field1)

  @classmethod
  def arg_post(cls,args):
    test = OpTest(OpClient(),args.field1)
    test.post(args.field2)
    
  @classmethod
  def arg_get(cls,args) -> dict:
    test = OpTest(OpClient(),args.field1)
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
    
class OpTest2():
  
  def __init__(self,test:OpTest,field2:str):
    self.test=test
    self.field2=field2

  def post(self,field3:str):
    with ApiClient(self.test.client.configuration) as api_client:
      api = DbApi(api_client)
      body = Test2PostRequestJson(field3=field3)
      api.db_test_testid_test2_field2_post(
        self.test.field1,
        self.field2,
        body)
 
  def get(self) -> dict:
    with ApiClient(self.test.client.configuration) as api_client:
      api = DbApi(api_client)
      return api.db_test_testid_test2_field2_get("value1","value2")

  @classmethod
  def arg_post(cls,args):
    test = OpTest(OpClient(),args.field1)
    test2 = OpTest2(test,args.field2)
    test2.post(args.field3)

  @classmethod
  def arg_get(cls,args) -> dict:
    test = OpTest(OpClient(),args.field1)
    test2 = OpTest2(test,args.field2)
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
  parser = argparse.ArgumentParser(description="OpClient")
  command = parser.add_subparsers(dest="command",help="commands")
  OpTest.argsp(command)
  OpTest2.argsp(command)
  a = parser.parse_args()
  if not hasattr(a, 'func'):
    parser.print_help()
    os._exit(1)
  print(a.func(a))

if __name__ == "__main__":
  main()
