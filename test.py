import keyboard
from time import sleep
from pyperclip import paste


def comment():
    keyboard.send("home, #, space,end")


closes = {"(": ")", "{": "}", "[": "]", '"': '"', "'": "'", "<": ">"}


def close(open):
    keyboard.write(closes[open])
    sleep(0.2)
    keyboard.send("left")


# add_word_listener("(", insert_closed_bracket,triggers=['typing'])
keyboard.add_hotkey("shift+9", close, args=["("])

keyboard.add_abbreviation("*mail", "astarcys7@proton.me")
keyboard.wait()
