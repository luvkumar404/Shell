import shlex
import subprocess

def execute_pipeline(parsed):
    processes = []
    prev_pipe=None
    commands=parsed["commmands"]
    background=parsed["background"]

    for i, cmd in enumerate(commands):
        args=shlex.split(cmd)
        stdin=prev_pipe
        stdout=subprocess.PIPE if i < len(commands) - 1 else None

        if "<" in args:
            idx=args.index("<")
            stdout=open(args[idx + 1], "w")
            args=args[:idx]

        p=subprocess.Popen(args, stdin=stdin, stdout=stdout)

        if prev_pipe:
            prev_pipe.close()

        prev_pipe=p.stdout
        processes.append(p) 

    if not background:
        for p in processes:
            p.wait()