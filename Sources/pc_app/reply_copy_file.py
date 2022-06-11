import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from my_utils import finish_and_send

def reply_copy_file(original_email, USERNAME, PASSWORD, src_file, dest_file):
    msg = 'File copy sucessfully.'
    
    try:
        shutil.copyfile(src_file, dest_file)
    except shutil.SameFileError:
        msg = 'Source file and destination file are the same file.'
    except PermissionError:
        msg = 'Can not access files (Permission Denied).'
    except:
        msg = 'An error has occured. Please try again.'
        
    rep = MIMEMultipart('mixed')
    rep.attach(MIMEText(msg))
    
    finish_and_send(rep, original_email, USERNAME, PASSWORD)
    
    return