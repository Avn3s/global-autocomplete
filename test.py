import keyboard
from time import sleep
from pyperclip import paste


def comment():
    keyboard.send("home, #, space,end")


closes = {"(": ")", "{": "}", "[": "]", '"': '"', "'": "'", "<": ">"}


def close(open):
    keyboard.write(')')
    keyboard.release("shift")
    keyboard.send("left")
    keyboard.press("shift")


# add_word_listener("(", insert_closed_bracket,triggers=['typing'])
keyboard.add_hotkey("shift+9", close, args=["("])

keyboard.add_abbreviation("*mail", "astarcys7@proton.me")
keyboard.wait()
