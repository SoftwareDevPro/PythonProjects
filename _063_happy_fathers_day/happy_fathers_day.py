

import pyfiglet
import random

fonts = ['smscript','slant','digital','banner3','standard']
colors = ['cyan','magenta','blue','yellow','green','red']

selected_color = random.choice(colors)
selected_font = random.choice(fonts)

message = pyfiglet.figlet_format("Happy Fathers Day!!",font=selected_font)
print(f"\033[1;{colors.index(selected_color)+31}m{message}\033[0m")


