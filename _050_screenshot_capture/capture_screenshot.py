
from tkinter import Tk, Button
import pyautogui

main_win = Tk()
main_win.title("Screenshot")

def ss_cb():
    screenshot = pyautogui.screenshot()
    screenshot.save(f"C:\\temp\\screenshot.jpg")

def exit_cb():
    main_win.destroy()

button = Button(main_win, text = "Take Screenshot", command=ss_cb)
button.grid(row = 100, column = 100)

exit_button = Button(main_win, text = "Exit", command=exit_cb)
exit_button .grid(row = 100, column = 200)

main_win.mainloop()