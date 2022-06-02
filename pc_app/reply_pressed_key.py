import keyboard

def reply_pressed_key():
    while True:
        cur = keyboard.read_key()
        if cur == 'enter':
            break
        print(cur, end = '')

reply_pressed_key()