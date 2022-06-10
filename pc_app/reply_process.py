import psutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tabulate import tabulate
import pandas as pd

from my_utils import finish_and_send

def reply_list_running_app(original_email, USERNAME, PASSWORD):
    ans = {'Pid' : [], 'Name' : []}
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_id = proc.pid
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        ans['Pid'].append(process_id)
        ans['Name'].append(process_name)

    df = pd.DataFrame(ans)
    ans = tabulate(df, headers = 'keys', tablefmt = 'fancy_grid')
    rep = MIMEMultipart('mixed')
    rep.attach(MIMEText(ans))

    finish_and_send(rep, original_email, USERNAME, PASSWORD)
        
################################################################################

def reply_stop_app(original_email, USERNAME, PASSWORD, pid):
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
