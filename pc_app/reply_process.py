import psutil
import ssl, email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from my_utils import finish_and_send

def reply_list_running_app(original_email, USERNAME, PASSWORD):
    ans = ['Running Apps:']
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_id = proc.pid
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        ans.append('{:<20} {:<20}'.format('Pid: ' + str(process_id), 'Name: ' + process_name))
    ans = '\n'.join(ans)
    
    rep = MIMEMultipart('mixed')
    rep.attach(MIMEText(ans))

    finish_and_send(rep, original_email, USERNAME, PASSWORD)
        
################################################################################

def reply_stop_app(original_email, USERNAME, PASSWORD, pid):
    print('adu cai nay hay vl')
    try:
        proc = psutil.Process(pid)
        process_name = proc.name()
        proc.terminate()
        mess = process_name + ' has been terminated'
    except:
        mess = 'Invalid pid'

    rep = MIMEMultipart('mixed')
    rep.attach(MIMEText(mess))
    
    finish_and_send(rep, original_email, USERNAME, PASSWORD)