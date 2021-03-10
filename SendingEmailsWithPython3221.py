# substitute $ for variables
# Using this pathlib we can import html data
# email.set_content(html.substitute({'name': 'TinTin'}), 'html')
# Make the difference to show up the HTML code
# email.set_content(html.substitute(name= 'TinTin'))

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Mark'
email['to'] = 'fernanda_mgp@hotmail.com'
email['subject'] = 'GANHE 1 MILHAO AGORA'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('joyupenglish@gmail.com', 'JOBju19!')
    smtp.send_message(email)
    print('Done')

