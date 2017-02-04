import config
from flask import Flask, Response, request
from twilio import twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
client = TwilioRestClient(config.TWILIO_ACCOUNT_SID,
                          config.TWILIO_AUTH_TOKEN)

#Clask app to receive incoming calls
@app.route('/incall', methods=['POST'])
def inbound_call():
    response = twiml.Response()
    #Once the call is received, respond with the below message to the caller
    response.addSay("Thanks for calling our customer service."
                    "Please hold while we connect you to our advisors.")
    return Response(str(response), 200, mimetype="application/xml")

if __name__ == '__main__':
    app.run(debug=True)

