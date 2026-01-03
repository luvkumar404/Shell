# A Mini Shell in Python

PySh is a lightweight, cross-platform **Unix-like mini shell** implemented in Python.  
It demonstrates core shell concepts such as command parsing, built-in commands, process execution, pipes, redirection, and background jobs.

This project is suitable for:
- Operating Systems learning
- Python intern / fresher portfolios
- Understanding how shells work internally
- Resume and GitHub projects

---

## Features

### Built-in Commands
Handled directly by the shell:
- `cd [dir]` – change directory
- `pwd` – print current directory
- `echo [text]` – print text
- `clear` – clear terminal
- `mkdir [dir]` – create directory
- `rmdir [dir]` – remove directory
- `touch [file]` – create empty file
- `help` – list available commands
- `exit` – exit the shell

### External Commands
Executed using the host OS:
- Windows: `dir`, `type`, `ping`, etc.
- Linux (WSL): `ls`, `grep`, `cat`, etc.

### Shell Capabilities
- Pipes: `dir | find "py"`
- Input redirection: `type < file.txt`
- Output redirection: `echo hello > file.txt`
- Background execution: `sleep 5 &`
- Graceful `Ctrl+C` handling


---

## Installation & Usage

### Prerequisites
- Python 3.8 or higher
- Windows, Linux, or macOS

### Run the Shell

```bash
cd Pysh
python main.py
```

## Author
Love Kumar Chaudhary
