import re
import shutil
import os

# posix will match for unix and mac
if os.name == 'posix':
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# For Windows
elif os.name == 'nt':
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# If the OS is not supported by Progam
else:
    print(f"OS not supported: {os.name}")

os.chdir(desktop)
list_of_shortcuts = os.listdir()

for shortcut in list_of_shortcuts:
    if 'cpt' in shortcut.lower():
        if os.path.isfile(shortcut):
            try:
                folder = re.search(r'-(.*?)-', shortcut).group(1)
                shutil.move(shortcut,folder)
                print(f'Moved {shortcut} to {folder}')
            except AttributeError:
                print(f"File: \"{shortcut}\" is formatted wrong")

        else:
            pass

