import os
import sys
import shlex
import platform

IS_WINDOWS = platform.system() == "Windows"

def handle_builtin(parsed):
    first_cmd = shlex.split(parsed["commands"][0])
    if not first_cmd:
        return True

    cmd = first_cmd[0]
    args = first_cmd[1:]

    if cmd == "exit":
        sys.exit(0)

    elif cmd == "cd":
        path = args[0] if args else os.path.expanduser("~")
        os.chdir(path)
        return True

    elif cmd == "pwd":
        print(os.getcwd())
        return True

    elif cmd == "echo":
        print(" ".join(args))
        return True

    elif cmd == "clear":
        os.system("cls" if IS_WINDOWS else "clear")
        return True

    elif cmd == "mkdir":
        for d in args:
            os.makedirs(d, exist_ok=True)
        return True

    elif cmd == "rmdir":
        for d in args:
            os.rmdir(d)
        return True

    elif cmd == "touch":
        for f in args:
            open(f, "a").close()
        return True

    elif cmd == "help":
        print("""
Built-in commands:
  cd [dir]      Change directory
  pwd           Print current directory
  echo [text]   Print text
  clear         Clear screen
  mkdir [dir]   Create directory
  rmdir [dir]   Remove directory
  touch [file]  Create empty file
  exit          Exit shell
""")
        return True

    return False
