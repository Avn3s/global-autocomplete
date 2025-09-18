import keyboard
from time import sleep

# hello world
def comment():
    keyboard.send("home, #, space,end")


closes = {"(": ")", "{": "}", "[": "]", '"': '"', "'": "'", "<": ">"}


def close(open):
    keyboard.write(closes[open])
    keyboard.send("left")

print("Welcome to AutoCloser")
# add_word_listener("(", insert_closed_bracket,triggers=['typing'])
#keyboard.add_hotkey("(", close, args=["("])
for open_bracket in closes.keys():
    keyboard.on_press_key(open_bracket, lambda e, b=open_bracket: close(b))

keyboard.add_abbreviation("@@", "astarcys7@proton.me")
keyboard.wait()