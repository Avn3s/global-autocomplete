import keyboard
from time import sleep

# hello world
def comment():
    keyboard.send("home, #, space,end")


closes = {"(": ")", "{": "}", "[": "]", '"': '"', "'": "'", "<": ">"}


def close(open):
    keyboard.write(')')
    keyboard.release("shift")
    keyboard.send("left")
    keyboard.press("shift")

print("Welcome to AutoCloser")
# add_word_listener("(", insert_closed_bracket,triggers=['typing'])
keyboard.add_hotkey("shift+9", close, args=["("])

keyboard.add_abbreviation("*mail", "astarcys7@proton.me")
keyboard.wait()