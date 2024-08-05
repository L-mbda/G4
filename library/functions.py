import sys, os

def clear():
  if (sys.platform == 'linux' or sys.platform == 'darwin'):
    os.system("clear")
  elif sys.platform == 'win32':
    os.system("cls")