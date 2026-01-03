def parse_command(command):
    return(
        "background": command.endswith("&")
        "commands": command.rstrip("&").strip().split("|")
    )