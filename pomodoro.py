import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
Timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def count_reset():
    # TODO 7 : it cancel the delay time created by after [it frezze the time]
    window.after_cancel(Timer)
    my_label.config(text="Timer")
    my_checkmark.config(text="")
    canvas.itemconfig(canvas_timer,text=f"00:00")
    global  reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_start():
    global reps
    reps = reps + 1

    work_min = WORK_MIN*60
    short_Break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    if reps % 8==0:                                                          # 20min long break[8]
            count_down(long_break)
            my_label.config(text="LONG BREAK",fg=RED)                        # updating label
    elif reps % 2 ==0:                                                       # 5 min break[2,4,6]
            count_down(short_Break)
            my_label.config(text="BREAK",fg=PINK)                            # updating label
    else:                                                                    # 25min working hrs[1,3,5,7]
        count_down(work_min)
        my_label.config(text="WORKING HOURS", fg=GREEN)                      # updating label




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:         #TODO 7 : dynamic typing
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
        # TODO 6 : update of convas using itemconfig
    canvas.itemconfig(canvas_timer,text=f"{count_min}:{count_sec}")

    if count>0:
        global  Timer
        # TODO 5 : window delay [after 1sec,display count,after delay reduce the count ]
        Timer = window.after(1000,count_down,count-1)
        print(count)
    else:
        count_start()
        mark = ""
        work_session = math.floor(reps/2)
        for _in in range(work_session) :
            mark = mark + "✔️"
            my_checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# TODO 1 : window setup
window = tkinter.Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)

# TODO 2 : Canvas :- its a widget templete or drawing it is used to import img,text,decoration,etc..
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

# TODO 2.1 : photoimage :- it helps to import image
import_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = import_img)
canvas.grid(row=1,column=1)

# TODO 2.2 : canvas_text :- [x-axis = 100 , y-axis = 128 place a text in this direction, fill = color of text]
canvas_timer = canvas.create_text(100,128,text="00:00",font=(FONT_NAME,30,"bold" ),fill="white")

# TODO 3 : creating label
my_label = tkinter.Label(text="Timer",font=(FONT_NAME,30,"bold" ),fg=GREEN,bg=YELLOW)
my_label.grid(row=0,column=1)
check_mark =" ️✓ "
my_checkmark = tkinter.Label(text="",font=(FONT_NAME,15,"bold" ),highlightthickness=0,bg=YELLOW,fg="#C8E4B2")
my_checkmark.grid(row=3,column=1)

# TODO 4 : create buttons
my_button = tkinter.Button(text="Start",font=(FONT_NAME,10,"bold"),command=count_start)
my_button.grid(row=2,column=0)

my_button_1 = tkinter.Button(text="Reset",font=(FONT_NAME,10,"bold" ),command=count_reset)
my_button_1.grid(row=2,column=2)

# TODO 4 : create checkbox
# check_mark =" ✔️ "
# my_checkmark = tkinter.Checkbutton(text="",highlightthickness=0,bg=YELLOW)
# my_checkmark.grid(row=3,column=1)


















window.mainloop()