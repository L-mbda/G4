# Modules
from colorama import Fore, init
from pathlib import Path
import os, hashlib, binascii, sys

working_directory = os.getcwd()

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
    salt = binascii.b2a_hex(os.urandom(20))
    # Password
    passwordWriter = open('credentials.g4','w')
    sha = hashlib.new('sha3_512')
    sha.update(f'{str(salt)}{password}'.encode())
    passwordWriter.write(sha.hexdigest())
    passwordWriter.close()
    saltWriter = open('salt.g4', 'w')
    saltWriter.write(str(salt))
    saltWriter.close()
    roleSetter = open('account.g4', 'w')
    roleSetter.write('owner'.encode().hex())
    roleSetter.close()
    os.chdir(os.getcwd())
    print(f"\n{Fore.BLUE}Created owner account successfully.")
    return 'CREATED_OWNER'
  elif user_type == 'admin':
    if (not Path(username).is_dir()):
      os.makedirs(username)
    privileges = open('privileges.g4', 'a')
    privileges.write(f'{username}\n')
    privileges.close()
    os.chdir(f'./{username}')
    salt = binascii.b2a_hex(os.urandom(20))
    # Password
    passwordWriter = open('credentials.g4','w')
    sha = hashlib.new('sha3_512')
    sha.update(f'{str(salt)}{password}'.encode())
    passwordWriter.write(sha.hexdigest())
    passwordWriter.close()
    saltWriter = open('salt.g4', 'w')
    saltWriter.write(str(salt))
    saltWriter.close()
    roleSetter = open('account.g4', 'w')
    roleSetter.write('admin'.encode().hex())
    roleSetter.close()
    os.chdir(os.getcwd())
    print(f"\n{Fore.BLUE}Created administrator account successfully.")
    return 'CREATED_ADMIN'
  else:
    if (not Path(username).is_dir()):
      os.makedirs(username)
    os.chdir(f'./{username}')
    salt = binascii.b2a_hex(os.urandom(20))
    # Password
    passwordWriter = open('credentials.g4','w')
    sha = hashlib.new('sha3_512')
    sha.update(f'{str(salt)}{password}'.encode())
    passwordWriter.write(sha.hexdigest())
    passwordWriter.close()
    saltWriter = open('salt.g4', 'w')
    saltWriter.write(str(salt))
    saltWriter.close()
    roleSetter = open('account.g4', 'w')
    roleSetter.write('user'.encode().hex())
    roleSetter.close()
    os.chdir(os.getcwd())
    print(f"\n{Fore.BLUE}Created account successfully.")
    return 'CREATED_USER'

def login(username, password):
  os.chdir('./user')
  user_check = Path(username).is_dir()
  if username == '' or username == ' ':
    os.chdir(working_directory)
    return ['LOGIN_FAILED']
  if not user_check:
    os.chdir(working_directory)
    return ['LOGIN_FAILED']
  os.chdir(f'./{username}')
  saltManager = open('salt.g4','r')
  salt = saltManager.readlines()[0]
  saltManager.close()
  passwordManager = open('credentials.g4','r')
  password_linear = passwordManager.readlines()[0]
  passwordManager.close()
  sha = hashlib.new('sha3_512')
  sha.update(f'{str(salt)}{password}'.encode())
  if sha.hexdigest() == password_linear:
    os.chdir(working_directory)
    return ['LOGIN_SUCCESS']
  else:
    os.chdir(working_directory)
    return ['LOGIN_FAILED']