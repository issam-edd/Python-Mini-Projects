import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Karim Shrif'
email['to'] = 'mouradshrif123@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

# email.set_content('I am a Python Master if you care!')
email.set_content(html.substitute({'name' : 'testest'}),'html') #if ther is more than one var you can use dict

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('mourad123eddine@gmail.com', 'Mourad089@')
    smtp.send_message(email)
    print('all good boos!')
    # https: // www.google.com / settings / security / lesssecureapps
