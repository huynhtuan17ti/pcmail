import imaplib
import email
import time
import sys

from reply_screenshot import reply_screenshot

USERNAME = 'networkingass20120015@gmail.com'
PASSWORD = 'DummyPassword123'
    
if __name__ == '__main__':
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    
    try:
        retcode, capabilities = conn.login(USERNAME, PASSWORD)
    except:
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
                    
                    body_message = ''
                    
                    for elem in email_message.walk():
                        if elem.get_content_type() == 'text/plain' or elem.get_content_type() == 'text/html':
                            body_message = elem.get_payload(decode=True).decode()
                            break
                    
                    body_message = body_message.lower()
                    
                    print(body_message)
                    
                    if 'screenshot' in body_message:
                        reply_screenshot(email_message, USERNAME, PASSWORD)
                    
                    retcode, data = conn.store(num, '+FLAGS', '(\\Seen)')
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print('Bye')
