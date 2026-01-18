from threading import Thread
import keyboard
from orjson import loads

PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    '"': '"',
    "'": "'",
    "<": ">",
}

with open("abbreviations.json") as file:
    ABS = loads(file.read())


def _insert_closing_pair(event):
    """
    Called whenever a key is pressed.
    If the key is an opening character, schedule the
    insertion of the matching closing character.
    """
    if event.event_type != "down":
        return

    key = event.name

    if key not in PAIRS:
        return

    def _type_closing():
        closing = PAIRS[key]
        keyboard.write(closing)
        keyboard.release("shift")
        keyboard.send("left")

    Thread(target=_type_closing, daemon=True).start()


print("AutoEase is running.")
keyboard.hook(_insert_closing_pair)
for ab in ABS:
    keyboard.add_abbreviation(ab, ABS[ab])

keyboard.wait()
print("\nShutting down. Bye!")
