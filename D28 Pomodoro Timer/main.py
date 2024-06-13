from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#C70A80"
PURPLE = "#590696"
BLUE = "#37E2D5"
YELLOW = "#FBCB0A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
checks = []
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(count_text, text="00:00")
    title.config(text="Timer")
    global checks
    checks = []
    check.config(text=checks)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps > 8:
        return
    elif reps % 8 == 0:
        minutes = LONG_BREAK_MIN
        title.config(text="Break", fg=YELLOW)
    elif reps % 2 == 0:
        minutes = SHORT_BREAK_MIN
        title.config(text="Break", fg=PINK)
    else:
        minutes = WORK_MIN
        title.config(text="Work", fg=PURPLE)
        global checks
        checks.append("✔")
        check.config(text=checks)

    count_down(minutes * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{count}"

    canvas.itemconfig(count_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=30, bg=BLUE)
# window.minsize(height=500, width=500)


canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=BLUE, foreground=YELLOW)
start = Button(text="Start", bg=YELLOW, fg="black", highlightthickness=0, command=start_timer)
check = Label(bg=BLUE, fg=PURPLE, font=(FONT_NAME, 20, "normal"))
reset = Button(text="Reset", bg=YELLOW, fg="black", highlightthickness=0, command=reset_timer)

title.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
check.grid(column=1, row=3)
reset.grid(column=2, row=2)


window.mainloop()
