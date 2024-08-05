"""
  G4 Platform Manager
  ©2024 de-y.
  Licensed under the MIT License
"""

# Modules to import
from colorama import Fore, Back, Style, init
from datetime import datetime
from pathlib import Path
import library.functions
import library.game
import questionary

# Flags
saveCheck = False

# Functions to clear and for saves
library.functions.clear();
init()
saveFolderCheck = Path('saves').is_dir()
if saveFolderCheck:
  saveCheck = True

# Saved applications and functions
print(f"""{Fore.BLUE}𝐆𝟒
{Fore.RESET}==========================
{Fore.LIGHTGREEN_EX}©{datetime.now().strftime('%Y')} de-y. All Rights Reserved.{Fore.RESET}
""")

menu_choice = questionary.select(
    "What would you like to do?",
    choices=["Start a new game" if not saveCheck else "Continue playing", "Settings", "Credits"],
).ask()

if menu_choice == "Start a new game":
  print()
  library.game.startGame()
elif menu_choice == 'Credits':
  library.functions.clear();
  print(f"{Fore.BLUE}𝐆𝟒\n{Fore.RESET}A cli text-based game that replicates the experience of original games. Created and developed with ❤️  from de-y.\n\n")
elif menu_choice == 'Settings':
  library.functions.clear();
  print(f"{Fore.BLUE}𝐆𝟒{Fore.RESET} | Settings\n\n")