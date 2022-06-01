import ssl
import email
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pyautogui

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
    
    rep['Message-ID'] = email.utils.make_msgid()
    rep['In-Reply-To'] = original_email['Message-ID']
    rep['Subject'] = 'Re: ' + original_email['Subject']
    rep['To'] = original_email['Reply-To'] or original_email['From']
    rep['From'] = USERNAME
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as conn:
        print('Processing ... ', end='')
        conn.login(USERNAME, PASSWORD)
        conn.sendmail(USERNAME, rep['To'], rep.as_string())
        conn.quit()
        print('Done')