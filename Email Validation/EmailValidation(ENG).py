#  1. input for email verification

#  2. verifying the characters

#  3. validating email (true or false)

#  4. if true, function for sending messages 

import re #  for email validation
import smtplib as sl #  for sending emails
from email.mime.text import MIMEText # for capturing message info

# pattern of email character verification
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,7}\b'

# function for email validation
def validarEmail(email):
    if re.match(email_pattern, email):
        print('Valid E-mail')
        return True
    else:
        print('Invalid E-mail')
        return False
     
# function for sending messages 
def enviarmsg(message, email, subject, recipient, password):

    # opening a GMAIL server
    server = sl.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email, password)  

    # getting the email message
    msg = MIMEText(message)
    msg['Subject'] = (subject)
    msg['From'] = (email)
    msg['To'] = (recipient)

    # sending message
    server.sendmail(email, msg.as_string())

    # closing the server 
    server.quit()
    
# main program
email = input('Type your e-mail: ')
password = input('Type your password: ')
msg = input('Type your message: ')
subject = input('Type the message subject: ')
recipient = input('Type the recipient e-mail: ')

# if the validations returns True, send the email
if validarEmail(email) == True and validarEmail(recipient) == True:
    enviarmsg(msg, email, recipient, subject, password)

else:
    print('Invalid E-mail, please try again.')