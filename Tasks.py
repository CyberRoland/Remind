import webbrowser
from pynput.keyboard import Key, Controller
import time as tm
from datetime import time, timedelta, datetime
import schedule
import pyautogui

keyboard = Controller()

def sched_school():
    schedule.every().day.at("09:45").do(school)

def sched_sleep():
    schedule.every().day.at("22:00").do(sleep)

def sched_code():
     schedule.every().day.at("09:45").do(code)

def school():
        webbrowser.open("https://docs.google.com/presentation/d/1xX6MvUPy4WQyEYmxv4A_g4gAHzb61BC6zqsCKTxNvww/present?slide=id.p")
        keyboard.press(Key.f11)

def reset_school():
    pass

def code():
    webbrowser.open("https://cyberroland.github.io/My-Website/Projects/")
    keyboard.press(Key.f11)

def reset_code():
    pass

def sleep():
    webbrowser.open("https://docs.google.com/presentation/d/1Maggi1Qe9hTwSwaWfqOkem601VezLYRXasEIUOuAqks/present?slide=id.p")
    keyboard.press(Key.f11)

def reset_sleep():
    pass