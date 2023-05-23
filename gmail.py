import smtplib
# SMTP_SSL Example
server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo() # optional, called by login()
server_ssl.login('getfreecertificate.team@gmail.com', 'change me')  
# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
server_ssl.sendmail('getfreecertificate.team@gmail.com', 'luckyrathore03@gmail.com', 'hello world')
#server_ssl.quit()
server_ssl.close()
print( 'successfully sent the mail')

