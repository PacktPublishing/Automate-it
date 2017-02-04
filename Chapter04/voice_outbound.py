import config
from flask import Flask, Response, request
from twilio import twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
client = TwilioRestClient(config.TWILIO_ACCOUNT_SID,
                          config.TWILIO_AUTH_TOKEN)
 
#Flask app to make outbound calls
@app.route('/call', methods=['POST'])
def outbound_call():
    response = twiml.Response()
    call = client.calls.create(
        to=config.MYNUMBER,
        from_=config.CALLERID,
        record='true',
        url=config.BASE_URL + '/answer_url',
    )
    return Response(str(response), 200, mimetype="application/xml")

#Play a message to the person who picks up the call
@app.route('/answer_url', methods=['POST'])
def answer_url():
    response = twiml.Response()
    response.addSay("Hey! You are awesome. Thanks for answering.")
    return Response(str(response), 200, mimetype="application/xml")


if __name__ == '__main__':
    app.run(debug=True)

