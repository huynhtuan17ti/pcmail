from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from my_utils import finish_and_send

import subprocess
import winreg
import os

def reply_shutdown(original_email, USERNAME, PASSWORD):
    rep = MIMEMultipart('mixed')
    
    rep.attach(MIMEText('Shutting down the computer...'))
    
    finish_and_send(rep, original_email, USERNAME, PASSWORD)
    
    subprocess.run(['shutdown', '/s'])

# https://stackoverflow.com/questions/42605055/creating-new-value-inside-registry-run-key-with-python
def set_run_once_key(key, value):
    """
    Set/Remove Run Key in windows registry.

    :param key: Run Key Name
    :param value: Program to Run
    :return: None
    """
    # This is for the system run variable
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\RunOnce',
        0, winreg.KEY_SET_VALUE)

    with reg_key:
        if value is None:
            winreg.DeleteValue(reg_key, key)
        else:
            if '%' in value:
                var_type = winreg.REG_EXPAND_SZ
            else:
                var_type = winreg.REG_SZ
            winreg.SetValueEx(reg_key, key, 0, var_type, value)

def reply_restart(original_email, USERNAME, PASSWORD):
    rep = MIMEMultipart('mixed')
    
    rep.attach(MIMEText('Restarting the computer...'))
    
    finish_and_send(rep, original_email, USERNAME, PASSWORD)
    
    set_run_once_key('EmailRemoteControl', os.path.realpath('email_listener.py'))
    
    subprocess.run(['shutdown', '/r'])
    
    