import smtplib as smtp
from dotenv import load_dotenv,find_dotenv
import os 

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
    

def send_mail(sender,msg):
    email_host = os.environ['EMAIL']
    email_password = os.environ['EMAIL_PASSWORD']
    email_target = os.environ['TARGET_EMAIL']

    # Email settings
    email_connection = smtp.SMTP_SSL(EMAIL_HOST,EMAIL_PORT)
    email_connection.login(email_host, email_password)
    EMAIL_USE_SSL = True
    formated_message="""
    Email from: {sender} \n

    Message: \n
    {msg}
    """.format(sender=sender, msg=msg)
    email_connection.sendmail(from_addr=email_host, to_addrs=email_target, msg=formated_message)
    email_connection.close()
