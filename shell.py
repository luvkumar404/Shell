import shlex
from parser import parse_command
from executor import execute_pipeline
from builtins import handle_builtin


def run_shell():
    while True:
        try:
            command=input("sh> ").strip()
            if not command:
                continue

                parsed=parse_command(command)

                if handle_builtin(parsed):
                    continue
                execute_pipeline(parsed)

        except KeyboardInterrupt:
            print()
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error: {e}")
            