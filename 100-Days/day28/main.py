from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WIDTH = 200
HEIGHT = 224
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    global timer

    reps = 0
    checkmark_label.config(text="")
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        countdown(5)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        countdown(4)
    else:
        title_label.config(text="Work Time", fg=GREEN)
        countdown(3)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    count_mins = f"{math.floor(count/60):02}"
    count_secs = f"{count%60:02}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        timer_start()
        if reps % 2 == 0:
            checkmarks = "✔" * int(reps / 2)
            checkmark_label.config(text=checkmarks)
# ---------------------------- UI SETUP ------------------------------- #
fg_color = GREEN
bg_color = YELLOW

window = Tk()
window.title("Pomodoro")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=WIDTH, height=HEIGHT, bg=bg_color, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=fg_color, bg=bg_color, font=(FONT_NAME, 20, "bold"))
title_label.grid(row=0, column=1)

checkmark_label = Label(text="", fg=fg_color, bg=bg_color)
checkmark_label.grid(row=3, column=1)

start_button = Button(text="Start", command=timer_start, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=timer_reset, highlightthickness=0)
reset_button.grid(row=2, column=2)



window.mainloop()