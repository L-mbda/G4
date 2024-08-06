# Modules
from colorama import Fore, init
from pathlib import Path
import sys, os, hashlib

# Functions
def clear():
  if (sys.platform == 'linux' or sys.platform == 'darwin'):
    os.system("clear")
  elif sys.platform == 'win32':
    os.system("cls")

def createAccount(username, password, user_type):
  user_dir_check = Path('user').is_dir()
  if (not user_dir_check):
    os.makedirs('user')
  else:
    pass
  os.chdir((os.getcwd() + '/user'))
  if user_type == 'owner':
    if (not Path(username).is_dir()):
      os.makedirs(username)
    masterUser = open('privileges.g4', 'w')
    masterUser.write(f'{username}\n')
    masterUser.close()
    os.chdir(f'./{username}')
    passwordWriter = open('credentials.g4','w')
    sha = hashlib.new('sha3_512')
    sha.update(password.encode())
    passwordWriter.write(sha.hexdigest())
    passwordWriter.close()
    roleSetter = open('account.g4', 'w')
    roleSetter.write('owner'.encode().hex())
    roleSetter.close()
    os.chdir(os.getcwd())
    print(f"\n{Fore.BLUE}Created owner account successfully.")
  elif user_type == 'admin':
    if (not Path(username).is_dir()):
      os.makedirs(username)
    privileges = open('privileges.g4', 'a')
    privileges.write(f'{username}\n')
    privileges.close()
    os.chdir(f'./{username}')
    passwordWriter = open('credentials.g4','w')
    sha = hashlib.new('sha3_512')
    sha.update(password.encode())
    passwordWriter.write(sha.hexdigest())
    passwordWriter.close()
    roleSetter = open('account.g4', 'w')
    roleSetter.write('admin'.encode().hex())
    roleSetter.close()
    os.chdir(os.getcwd())
    print(f"\n{Fore.BLUE}Created administrator account successfully.")
  else:
    if (not Path(username).is_dir()):
      os.makedirs(username)
    os.chdir(f'./{username}')
    passwordWriter = open('credentials.g4','w')
    sha = hashlib.new('sha3_512')
    sha.update(password.encode())
    roleSetter = open('account.g4', 'w')
    roleSetter.write('user'.encode().hex())
    roleSetter.close()
    os.chdir(os.getcwd())
    passwordWriter.write(sha.hexdigest())
    passwordWriter.close()
    print(f"\n{Fore.BLUE}Created account successfully.")