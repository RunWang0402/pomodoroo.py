from tkinter import *
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
CHECK_MARK="✓"
reps=0
marks=0
time=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(time)
    timer.config(text="Timer",fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps+=1
    if reps<9:
        if reps==8:
            timer.config(text="Break",fg=RED)
            count_down(long_break_sec)
        elif reps%2==1:
            timer.config(text="Work",fg=GREEN)
            count_down(work_sec)
        elif reps%2==0:
            timer.config(text="Break",fg=PINK)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    global time
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        time=window.after(1000,count_down,count-1)
    if count==0:
        if reps==1 or reps%2==1:
            global marks
            marks+=1
            check_mark.config(text=CHECK_MARK*marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(bg=YELLOW,padx=100,pady=50)





#Time_name
timer=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"normal"))
timer.grid(row=0,column=1)

#Tomato
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)



#Start Button
start=Button(text="Start",highlightbackground=YELLOW,command=start_timer)
start.grid(row=2,column=0)


#Reset Button
reset=Button(text="Reset",highlightbackground=YELLOW,command=reset_timer)
reset.grid(row=2,column=2)

#Check mark
check_mark=Label(fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)


window.mainloop()