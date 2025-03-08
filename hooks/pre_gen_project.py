import os
import sys

project_slug = '{{ cookiecutter.project_slug }}'

ERROR_COLOR = '\033[91m'
MESSAGE_COLOR = '\033[94m'
RESET_COLOR = '\033[0m'

if project_slug.startswith('x'):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} cannot start with 'x'{RESET_COLOR}")
    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_COLOR}")