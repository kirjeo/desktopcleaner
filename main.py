import re
import shutil
import os

# posix will match for unix and mac
if os.name == 'posix':
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# For Windows
else:
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)
list_of_shortcuts = os.listdir()


for shortcut in list_of_shortcuts:
    if 'cpt' in shortcut.lower():
        if os.path.isfile(shortcut):
            folder = re.search(r'JohnShay(.*?)-', shortcut).group(1)
            shutil.move(shortcut,folder)
            print(f'Moved {shortcut} to {folder}')
        else:
            pass
