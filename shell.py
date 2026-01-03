from parser import parse_command
from executor import execute_pipeline
from shell_builtins import handle_builtin

def run_shell():
    while True:
        try:
            command = input("pysh> ").strip()
            if not command:
                continue

            parsed = parse_command(command)

            # Handle built-in commands (cd, exit)
            if handle_builtin(parsed):
                continue

            execute_pipeline(parsed)

        except KeyboardInterrupt:
            print()
        except FileNotFoundError:
            print("Command not found")
        except Exception as e:
            print(f"Error: {e}")
