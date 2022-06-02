import ssl
import email
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pyautogui

from my_utils import finish_and_send

def reply_screenshot(original_email, USERNAME, PASSWORD):
    rep = MIMEMultipart('mixed')
    
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save('reply_image.jpg')
    
    with open('reply_image.jpg', 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        
    encoders.encode_base64(part)
    
    part.add_header(
        'Content-Disposition',
        f'attachment; filename= reply_image.jpg',
    )
    
    rep.attach(part)
    finish_and_send(rep, original_email, USERNAME, PASSWORD)