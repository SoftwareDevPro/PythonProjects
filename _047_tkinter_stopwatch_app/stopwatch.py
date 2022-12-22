
from tkinter import Tk, Frame, Label, Button, TOP, BOTTOM, LEFT, X, NO

main_win = Tk()
main_win.title("Stopwatch")
main_win.config(bg="midnightblue")

width, height = 550, 325
screen_width = main_win.winfo_screenwidth()
screen_height = main_win.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
main_win.geometry("%dx%d+%d+%d" % (width, height, x, y))

millisec = second = minute = 0

def Start():
    global time, timer, minute, second, millisec
    millisec += 1
    if millisec == 100:
         millisec, second = 0, second + 1
    if second == 60:
        second, minute = 0, minute + 1
    timer.config(text=f'{minute:02}:{second:02}:{millisec:02}')
    time = timer.after(100, Start)

def Stop():
    global time
    timer.after_cancel(time)

def Reset():
    global minute, second, millisec
    millisec = second = minute = 0
    timer.config(text=f"{minute:02}:{second:02}:{millisec:02}")
    timer.after_cancel(time)

def Exit():
    main_win.destroy()

if __name__ == "__main__":

    Top = Frame(main_win, width=400, bg="green2")
    Top.pack(side=TOP)

    Bottom = Frame(main_win, width=400,bg="black")
    Bottom.pack(side=BOTTOM)

    Title = Label(Top,
                 text="Stopwatch",
                 font=("Arial 24 bold"),
                 fg="plum2",
                 bg="black")
    Title.pack()

    timer = Label(Top, 
                  ont=("Times New Roman", 50),
                  fg="white",
                  bg="black")
    timer.pack(fill=X, expand=NO, pady=10)

    start_button = Button(Bottom,
                          text="Start",
                          font=("Arial 22 bold"),
                          fg="purple3",
                          width=8,
                          command=Start)
    start_button.pack(side=LEFT, padx=2, pady=5)

    stop_button = Button(Bottom,
                         text="Stop",
                         font=("Arial 22 bold"),
                         fg="purple3",
                         width=8,
                         command=Stop)
    stop_button.pack(side=LEFT, padx=2, pady=5)

    reset_button = Button(Bottom,
                          text="Reset",
                          font=("Arial 22 bold"),
                          fg="purple3",
                          width=8,
                          command=Reset)
    reset_button.pack(side=LEFT, padx=2, pady=5)

    exit_button = Button(Bottom,
                         text="Exit",
                         font = ("Arial 22 bold"),
                         fg="purple3",
                         width=8,
                         command=Exit)
    exit_button.pack(side=LEFT, padx=2, pady=5)

    main_win.mainloop()
