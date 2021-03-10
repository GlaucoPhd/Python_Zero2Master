# Download the helper library from https://www.twilio.com/docs/python/install
# Import os
# from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
from twilio.rest import Client

account_sid = 'AC8671297861b0eb4af2402db1507cac70'
auth_token = '69fa806b4fd4813c21514c22e129438d'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+15109534558',
    body='HELOOOOOO',
    to='+5519994857081'
)

print(message.sid)