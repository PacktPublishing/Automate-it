import config
from flask import Flask
from twilio.rest import TwilioRestClient

#Create a flask app and twilio client object
app = Flask(__name__)
client = TwilioRestClient(config.TWILIO_ACCOUNT_SID,
                          config.TWILIO_AUTH_TOKEN)

#Send a message from Twilio
message = client.messages.create(
    to=config.MYNUMBER,
    from_=config.CALLERID,
    body="Hey, this is cool!")

