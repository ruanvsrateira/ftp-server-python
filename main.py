import os
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

users = [ 
  {"username":"ruan", "password":"ruan", "perm":"elradfmwMT"},
  {"username":"root", "password":"root", "perm":"elradfmwMT"},
  {"username":"administration", "password":"administration123", "perm":"elradfmwMT"},
  {"username":"ronald", "password":"ronald", "perm":"elradfmwMT"},
]

authorizer = DummyAuthorizer()
handler = FTPHandler
handler.authorizer = authorizer

def initizalize_users():
  create_dirs_of_users()
  for user in users:
   authorizer.add_user(username=user["username"], password=user["password"], homedir=f"./{user["username"]}", perm=user["perm"])

def create_dirs_of_users():
  for user in users:
    if os.path.exists(user["username"]):
      continue
    os.mkdir(user["username"])

server = FTPServer(("localhost", 21), handler=handler)

if __name__ == '__main__':
  initizalize_users()
  logging.basicConfig(filename="logging.log", level=logging.DEBUG)
  server.serve_forever()