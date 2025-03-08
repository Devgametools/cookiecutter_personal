import subprocess

MESSAGE_COLOR = '\033[94m'
RESET_COLOR = '\033[0m'

print(f"{MESSAGE_COLOR} Almost done")
print(f"Initializing git repository...{RESET_COLOR}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}All done!{RESET_COLOR}")