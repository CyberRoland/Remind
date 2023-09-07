from customtkinter import *
from tkinter import *
import time as tm
from datetime import time, timedelta, datetime
import schedule
from Tasks import *
import threading

def sched():
    while True:
        schedule.run_pending()
        tm.sleep(1)

run_sched = threading.Thread(target=sched)
run_sched.start()

root = CTk()
root.title("Reminders")
root.geometry("800x600")

# Task

school_work = CTkButton(root, corner_radius=6.5, height=45, text="HW", font=("Lexend", 30), command=sched_school)
school_work.place(relx=0.5, rely=0.4 ,anchor='center')

code_remind = CTkButton(root, corner_radius=6.5, height=45, font=("Lexend", 30), text="Code", command=sched_code)
code_remind.place(relx=0.5, rely=0.5 ,anchor='center')

slep = CTkButton(root, corner_radius=6.5, height=45, font=("Lexend", 30), text="Sleep", command=sched_sleep)
slep.place(relx=0.5, rely=0.3 ,anchor='center')


root.mainloop()