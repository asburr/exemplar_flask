import argparse
import os
from fernclient.python.client import MineApi


class FernClient():
  
  def __init__(self,url="http://127.0.0.1:5000"):
    self.api = MineApi(base_url=url)

class FernTest():
  
  def __init__(self,client:FernClient,field1:str):
    self.client=client
    self.field1=field1

  def post(self,field2:str):
    self.client.api.db.add_row_into_test(field1=self.field1,field2=field2)

  def get(self) -> dict:
    return self.client.api.db.get_row_from_test(field1=self.field1)

  @classmethod
  def arg_post(cls,args):
    test = FernTest(FernClient(),args.field1)
    test.post(args.field2)
    
  @classmethod
  def arg_get(cls,args) -> dict:
    test = FernTest(FernClient(),args.field1)
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
    
class FernTest2():
  
  def __init__(self,test:FernTest,field2:str):
    self.test=test

  def post(self,field2:str,field3:str):
    self.test.client.db.add_row_to_test2with_foreign_key_to_test(
      testid=self.test.field1,
      field2=field2,
      field3=field3)
 
  def get(self) -> dict:
    return self.test.client.api.db.get_row_from_test2(testid="value1",field2="value2")

  @classmethod
  def arg_post(cls,args):
    test = FernTest(FernClient(),args.field1)
    test2 = FernTest2(test,args.field2)
    test2.post(args.field3)

  @classmethod
  def arg_get(cls,args) -> dict:
    test = FernTest(FernClient(),args.field1)
    test2 = FernTest2(test,args.field2)
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
  parser = argparse.ArgumentParser(description="FernClient")
  command = parser.add_subparsers(dest="command",help="commands")
  FernTest.argsp(command)
  FernTest2.argsp(command)
  a = parser.parse_args()
  if not hasattr(a, 'func'):
    parser.print_help()
    os._exit(1)
  print(a.func(a))

if __name__ == "__main__":
  main()