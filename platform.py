"""
  G4 Platform Manager
  ©2024 de-y.
  Licensed under the MIT License
"""

# Modules to import
from colorama import Fore, init
from pathlib import Path
import library.functions
import pwinput

# Flags
setup = False

# Functions to clear and for checking setup
library.functions.clear()
init()

# setup_check = Path('user').is_dir()
setup_check = False

if (not setup_check):
  print(f"""{Fore.GREEN}Welcome to {Fore.CYAN}G4{Fore.RESET}.

  Let's create your account.
  """)
  credentials = []
  while True:
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
  library.functions.createAccount(credentials[0][0], credentials[0][1], 'owner')
  