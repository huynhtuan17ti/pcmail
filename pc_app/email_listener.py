import imaplib
import smtplib
import ssl
import email
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

username = 'networkingass20120015@gmail.com'
password = 'DummyPassword123'

def reply_email(original_email):
    rep = MIMEMultipart('mixed')
    
    body = MIMEMultipart('alternative')
    body.attach(MIMEText('Ok gotchu', 'plain'))
    body.attach(MIMEText('<html>Ok gotchu</html>', 'html'))
    
    rep.attach(body)
    
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
    rep['From'] = username
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as conn:
        print('Processing ... ', end='')
        conn.login(username, password)
        conn.sendmail(username, rep['To'], rep.as_string())
        conn.quit()
        print('Done')
    
if __name__ == '__main__':
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    
    try:
        retcode, capabilities = conn.login(username, password)
    except:
        print(sys.exec_info()[1])
        sys.exit(1)
    
    try:
        while True:
            conn.select("Inbox")
            retcode, messages = conn.search(None, '(UNSEEN)')
            if retcode == 'OK':
                for num in messages[0].split():
                    retcode, data = conn.fetch(num, '(RFC822)')
                    
                    _, bytes_data = data[0]
                    
                    email_message = email.message_from_bytes(bytes_data)
                    
                    """
                    print(f'Subject: {email_message["subject"]}')
                    print(f'To: {email_message["to"]}')
                    print(f'From: {email_message["from"]}')
                    
                    for elem in email_message.walk():
                        if elem.get_content_type()=='text/plain' or elem.get_content_type()=='text/html':
                            message = elem.get_payload(decode=True)
                            print(message.decode())
                            break
                    
                    print('-'*30)
                    """
                    
                    reply_email(email_message)
                    
                    retcode, data = conn.store(num, '+FLAGS', '(\\Seen)')
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print('Bye')
