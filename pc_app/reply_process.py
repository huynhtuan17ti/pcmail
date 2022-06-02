import psutil
import ssl, email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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