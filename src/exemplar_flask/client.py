import requests
import argparse
import os

class Client():
  
  def __init__(self,url="http://127.0.0.1:5000"):
    self.url = url
  
  @classmethod
  def raise_for_status(cls,response):
    try:
      response.raise_for_status()
    except Exception:
      if "application/json" in response.headers.get("Content-Type", ""):
        j = response.json()
        if isinstance(j,str):
          msg = j
        else:
          msg = response.json().get("msg", "No message provided")
      else:
        msg = response.text
      raise Exception(msg)


class Test():
  
  def __init__(self,client:Client,field1:str):
    self.url = f"{client.url}/db/test/{field1}"

  def post(self,field2:str):
    response = requests.post(self.url, params={"field2":field2})
    Client.raise_for_status(response)
 
  def get(self) -> dict:
    response = requests.get(self.url)
    Client.raise_for_status(response)
    return response.json()

  @classmethod
  def arg_post(cls,args):
    test = Test(Client(),args.field1)
    test.post(args.field2)
    
  @classmethod
  def arg_get(cls,args) -> dict:
    test = Test(Client(),args.field1)
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
    
class Test2():
  
  def __init__(self,test:Test,field2:str):
    self.url = f"{test.url}/test2/{field2}"

  def post(self,field3:str):
    response = requests.post(self.url, params={"field3":field3})
    Client.raise_for_status(response)
 
  def get(self) -> dict:
    response = requests.get(self.url)
    Client.raise_for_status(response)
    return response.json()

  @classmethod
  def arg_post(cls,args):
    test = Test(Client(),args.field1)
    test2 = Test2(test,args.field2)
    test2.post(args.field3)

  @classmethod
  def arg_get(cls,args) -> dict:
    test = Test(Client(),args.field1)
    test2 = Test2(test,args.field2)
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
  parser = argparse.ArgumentParser(description="Client")
  command = parser.add_subparsers(dest="command",help="commands")
  Test.argsp(command)
  Test2.argsp(command)
  a = parser.parse_args()
  if not hasattr(a, 'func'):
    parser.print_help()
    os._exit(1)
  print(a.func(a))

if __name__ == "__main__":
  main()