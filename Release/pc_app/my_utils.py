import ssl
import smtplib
import email

def finish_and_send(reply_email, original_email, USERNAME, PASSWORD):
    reply_email['Message-ID'] = email.utils.make_msgid()
    reply_email['In-Reply-To'] = original_email['Message-ID']
    reply_email['Subject'] = 'Re: ' + original_email['Subject']
    reply_email['To'] = original_email['Reply-To'] or original_email['From']
    reply_email['From'] = USERNAME
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as conn:
        print('Processing ... ', end='')
        conn.login(USERNAME, PASSWORD)
        conn.sendmail(USERNAME, reply_email['To'], reply_email.as_string())
        conn.quit()
        print('Done')