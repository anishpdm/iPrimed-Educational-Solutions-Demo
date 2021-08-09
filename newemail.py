import secure-smtplib as smtplib1111

server = smtplib1111.SMTP_SSL('smtp.gmail.com', 465)
server.login("anish.vilayil.s@gmail.com", "developer12345")


if(__name__=='__main__'):
  server.sendmail(
  "anish.vilayil.s@gmail.com", 
  "anish@logixspace.com", 
  "this message is from python")
  server.quit()
