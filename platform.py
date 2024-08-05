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

setup_check = Path('user').is_dir()
if (not setup_check):
  print(f"""{Fore.GREEN}Welcome to {Fore.CYAN}G4{Fore.RESET}.

  Let's create your account.
  """)
  while True:
    username = input(f"{Fore.MAGENTA} Username{Fore.RESET}: ")
    password = pwinput.pwinput(f"{Fore.YELLOW} Password{Fore.RESET}: ")
    confirm_password = pwinput.pwinput(f"{Fore.YELLOW} Confirm Password{Fore.RESET}: ")
    if password == confirm_password:
      break
    else:
      print(f"\n{Fore.GREEN}The password isn\'t confirmed. Please reconfirm the password before continuing.")