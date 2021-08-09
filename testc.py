import smtplib 
from email.message import EmailMessage

EmailAdd = "Email id" #senders Gmail id over here
Pass = "Email Password" #senders Gmail's Password over here 

msg = EmailMessage()
msg['Subject'] = 'Subject of the Email' # Subject of Email
msg['From'] = EmailAdd
msg['To'] = 'abc@mail.com','xyz@mail.com' # Reciver of the Mail
msg.set_content('Mail Body') # Email body or Content

#### >> Code from here will send the message << ####
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #Added Gmails SMTP Server
    smtp.login(EmailAdd,Pass) #This command Login SMTP Library using your GMAIL
    smtp.send_message(msg) #This Sends the message