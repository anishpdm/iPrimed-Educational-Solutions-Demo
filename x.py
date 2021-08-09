import smtplib


  
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("anish.vilayil.s@gmail.com", "developer12345")
  
# message to be sent
message = "Message_you_need_to_send"
  
# sending the mail
s.sendmail("anish.vilayil.s@gmail.com", "anish@logixspace.com", message)
  
# terminating the session
s.quit()