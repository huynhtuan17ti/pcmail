import imaplib
import email
import time
import sys
import re

from reply_screenshot import reply_screenshot
from reply_process import reply_list_running_app, reply_stop_app
from reply_shutdown_restart import reply_shutdown, reply_restart

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
                    elif 'running app' in body_message:
                        reply_list_running_app(email_message, USERNAME, PASSWORD)
                    elif 'stop app pid:' in body_message:
                        try:
                            pid = int(re.match(r'.*stop app pid: (\d+).*', body_message).group(0))
                            reply_stop_app(email_message, USERNAME, PASSWORD, pid)
                            print(pid)
                        except:
                            pass
                    elif 'shutdown' in body_message:
                        reply_shutdown(email_message, USERNAME, PASSWORD)
                    elif 'restart' in body_message:
                        reply_restart(email_message, USERNAME, PASSWORD)

                    retcode, data = conn.store(num, '+FLAGS', '(\\Seen)')
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print('Bye')
