import threading
import keyboard

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '"': '"',
    "'": "'",
    "<": '>',
}

def _insert_closing_pair(event):
    """
    Called whenever a key is pressed.
    If the key is an opening character, schedule the
    insertion of the matching closing character.
    """
    if event.event_type != 'down':
        return

    key = event.name

    if key not in PAIRS:
        return

    def _type_closing():
        closing = PAIRS[key]
        keyboard.write(closing)
        keyboard.release('shift')
        keyboard.send('left')

    threading.Thread(target=_type_closing, daemon=True).start()


def main():
    print("AutoEase is running.")
    keyboard.hook(_insert_closing_pair)

    keyboard.wait()
    print("\nShutting down. Bye!")


if __name__ == "__main__":
    main()