import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'Glauco'
email['to'] = 'glaucoph@gmail.com'
email['subject'] = 'GANHE 1 MILHAO AGORA'

email.set_content('Hi Glauco you will be one of the best developers at Hortolandia site.'
                  'will got a chance 2021 to work with Kaizen team. Also i pray to be choosed to be part of the Lab CI Tech Team')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('joyupenglish@gmail.com', 'JOBju19!')
    smtp.send_message(email)
    print('Done')