# commands.py

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

def cmd_ls(args):
    path = args[0] if args else '.'
    print(os.listdir(path))

def cmd_cd(args):
    if args:
        os.chdir(args[0])
    else:
        print("Usage: cd <directory>")

def cmd_pwd(args):
    print(os.getcwd())

def cmd_mkdir(args):
    if args:
        os.mkdir(args[0])
    else:
        print("Usage: mkdir <foldername>")

def cmd_touch(args):
    if args:
        Path(args[0]).touch(exist_ok=True)
    else:
        print("Usage: touch <filename>")

def cmd_rm(args):
    if args:
        target = args[0]
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)
    else:
        print("Usage: rm <filename|foldername>")

def cmd_rename(args):
    if len(args) == 2:
        os.rename(args[0], args[1])
    else:
        print("Usage: rename <old_name> <new_name>")

def cmd_edit(args):
    if not args:
        print("Usage: edit <filename>")
        return
    filename = args[0]
    if not os.path.exists(filename):
        Path(filename).touch()
    print("Enter text (type '.save' on a new line to finish):")
    with open(filename, 'a+') as file:
      a = 1
      while True :
      	line = input(f'{a} ')
      	if line == ".save":
      		print(f'{filename} has been saved')
      		break
      	else:
      		file.write(f'\n{line}')
      	a = a+1

def cmd_runpy(args):
    if args:
        subprocess.run(['python', args[0]])
    else:
        print("Usage: runpy <script.py>")

def cmd_pipinstall(args):
    if args:
        subprocess.run(f"pip install {args[0]}", shell=True)
    else:
        print("Usage: pipinstall <package>")

def cmd_clear(args):
    os.system('cls' if os.name == 'nt' else 'clear')

def cmd_date(args):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
 
def cmd_help(self):
    print("Available commands:")
    print("  ls [dir]              - List files")
    print("  cd <dir>              - Change directory")
    print("  pwd                   - Show current path")
    print("  mkdir <name>          - Make directory")
    print("  touch <file>          - Create empty file")
    print("  edit <file>           - Edit a file")
    print("  rm <file>             - Delete file")
    print("  rename <old> <new>    - Rename file or folder")
    print("  runpy <script>        - Run Python script")
    print("  pipinstall <package>  - Install pip package")
    print("  date                  - Show date/time")
    print("  echo <text>           - Print text")
    print("  clear                 - Clear screen")
    print("  help                  - Show commands")
    print("  exit                  - Quit PyOS")


def cmd_echo(args):
    print(' '.join(args))

def cmd_exit(args):
    print("Exiting PyOS...")
    exit()

