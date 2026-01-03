import os
import sys
import shlex

def handle_builtin(parsed):
    first_cmd=shlex.split(parsed["commmands"][0])
    if not first_cmd:
        return True
    

    cmd=first_cmd[0]
    if cmd=="exit":
        sys.exit(0)

    if cmd=="cd":
        path=first_cmd[1] if len(first_cmd) > 1 else os.path.expanduser("~")
        os.chdir(path)
        return True
    
    return False