"""
  G4 Platform Manager
  ©2024 de-y.
  Licensed under the MIT License
"""

# Modules to import
from colorama import Fore, init
from pathlib import Path
import library.functions
import pwinput, random, os

# Flags
setup = False
working_directory = os.getcwd()
logged_in = False
credentials = []
sys_name = ""

try:
  nameService = open('system.g4','r')
  sys_name = nameService.readlines()[0]
except:
  sys_name = 'G4'

# Functions to clear and for checking setup
library.functions.clear()
init()

setup_check = Path('user').is_dir()

if (not setup_check):
  print(f"""{Fore.GREEN}Welcome to {Fore.CYAN}G4{Fore.RESET}.

  Let's create your account.
  """)
  credentials = []
  while True:
    system_name = input(f"{Fore.CYAN}Enter a name for your system{Fore.RESET}: ")
    username = input(f"{Fore.MAGENTA} Username{Fore.RESET}: ")
    password = pwinput.pwinput(f"{Fore.YELLOW} Password{Fore.RESET}: ")
    confirm_password = pwinput.pwinput(f"{Fore.YELLOW} Confirm Password{Fore.RESET}: ")
    if username == '' or username == ' ':
      print(f"\n{Fore.GREEN}You haven\'t inputted a username, please input one before continuing.'")
    elif password == confirm_password and (username != '' or username != ' '):
      credentials.append([username, password])
      break
    else:
      print(f"\n{Fore.GREEN}The password isn\'t confirmed. Please reconfirm the password before continuing.")
  # Setup process continues here
  print(f"\n{Fore.LIGHTYELLOW_EX}Confirmed credentials, please wait while your account is created.{Fore.RESET}")
  system = library.functions.createAccount(credentials[0][0], credentials[0][1], 'owner')
  if system == 'CREATED_OWNER':
    os.chdir(working_directory)
    sys_name = open('system.g4','w')
    sys_name.write(system_name)
    sys_name.close()
    print(f"\n{Fore.BLUE}Moving onto login...\n\n")
    setup_check = True

# Work login
if not not setup_check and not logged_in:
  os.chdir(working_directory)
  splashes = open('splashes.txt','r')
  splash_list = splashes.readlines()
  splash = random.choice(splash_list)
  print(f"{Fore.CYAN}G4{Fore.RESET}.\n\n{Fore.LIGHTRED_EX}{splash}{Fore.RESET}\n")
  chances = 10
  while chances != 0:
    username = input(f"{Fore.MAGENTA}Username{Fore.RESET}: ")
    password = input(f"{Fore.LIGHTWHITE_EX}Password{Fore.RESET}: ")
    login_status = library.functions.login(username, password)
    if login_status[0] == 'LOGIN_SUCCESS':
      credentials.append(username)
      logged_in = True
      break
    else:
      chances-=1
      print(f"{Fore.LIGHTRED_EX}Your username or password was incorrect, you have {chances} chances left.{Fore.RESET}")
    if chances == 0:
      print(f"{Fore.LIGHTRED_EX}You do not have any chances to login left. Have a good day!{Fore.RESET}")

if logged_in:
  library.functions.clear()
  print(f"{Fore.LIGHTGREEN_EX}Hello, {credentials[0]}!{Fore.RESET}\n")
  print(f"{Fore.CYAN}G4{Fore.RESET} System.\n\nRun the command \"help\" if you need help.\n===================\n")
  while True:
    command = input(f"{Fore.GREEN}{credentials[0][0]}@{sys_name}> ")
    if command == 'help':
      print(f"{Fore.RESET}HELP!")
    else:
      print(f'{Fore.LIGHTYELLOW_EX}\"{command}\" is not a valid command or service.{Fore.RESET}')