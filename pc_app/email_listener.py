import imaplib
import email
import time
import sys
import re

from reply_screenshot import reply_screenshot
from reply_process import reply_list_running_app, reply_stop_app
from reply_shutdown_restart import reply_shutdown, reply_restart
from reply_pressed_key import reply_pressed_key
from reply_camera_capture import reply_camera_capture
from reply_copy_file import reply_copy_file
from reply_registry import reply_modify_reg

import config as ui

USERNAME = 'networkingass20120015@gmail.com'
PASSWORD = '<NONE>'

if __name__ == '__main__':
    ui.getAllMail()
    
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    
    try:
        retcode, capabilities = conn.login(USERNAME, PASSWORD)
    except Exception as e:
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
                    
                    sender = email.utils.parseaddr(email_message['From'])[1]
                    
                    if sender not in ui.mailList:
                        continue
                    
                    body_message = ''
                    
                    for elem in email_message.walk():
                        if elem.get_content_type() == 'text/plain' or elem.get_content_type() == 'text/html':
                            body_message = elem.get_payload(decode=True).decode()
                            break
                
                    body_message = body_message.strip()
                    
                    if 'SCREENSHOT' in body_message:
                        reply_screenshot(email_message, USERNAME, PASSWORD)
                    elif 'LIST PROCESSES' == body_message:
                        reply_list_running_app(email_message, USERNAME, PASSWORD)
                    elif 'KILL ' in body_message:
                        try:
                            pid = int(re.match(r'KILL (\d+)', body_message).group(1))
                            print(f'Gui cuu {pid}')
                            reply_stop_app(email_message, USERNAME, PASSWORD, pid)
                            print(pid)
                        except:
                            pass
                    elif 'SHUTDOWN' in body_message:
                        reply_shutdown(email_message, USERNAME, PASSWORD)
                    elif 'RESTART' in body_message:
                        reply_restart(email_message, USERNAME, PASSWORD)
                    elif 'CATCH KEYBOARD' in body_message:
                        reply_pressed_key(email_message, USERNAME, PASSWORD)
                    elif 'VIDEO' in body_message:
                        reply_camera_capture(email_message, USERNAME, PASSWORD)
                    elif 'COPY' in body_message:
                        ls = body_message.split()
                        pos = ls.index('COPY')
                        
                        if pos + 2 < len(ls):
                            reply_copy_file(email_message, USERNAME, PASSWORD, ls[pos + 1], ls[pos + 2])
                    elif 'REG' in body_message:
                        ls = body_message.split()
                        pos = ls.index('REG')
                        
                        if pos + 3 < len(ls):
                            reply_modify_reg(email_message, USERNAME, PASSWORD, ls[pos + 1], ls[pos + 2], ls[pos + 3])
                        
                        
                    retcode, data = conn.store(num, '+FLAGS', '(\\Seen)')
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print('Bye')
