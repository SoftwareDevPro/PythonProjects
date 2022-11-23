

import winshell

try:
    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
    print("Recycle bin emptied")
except:
    print("Recycle bin already empty")

