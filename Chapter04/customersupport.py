import config
from flask import Flask, Response, request
from twilio import twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
client = TwilioRestClient(config.TWILIO_ACCOUNT_SID,
                          config.TWILIO_AUTH_TOKEN)

#Receive incoming call from customer
@app.route('/call', methods=['POST'])
def inbound_call():
    call_sid = request.form['CallSid']
    response = twiml.Response()
    response.dial().conference(call_sid)
    #Transfer call to customer support engineer	
    call = client.calls.create(to=config.MYNUMBER,
                               from_=config.CALLERID,
                               url=config.BASE_URL + '/conference/' + call_sid)
    return Response(str(response), 200, mimetype="application/xml")

#Add the call to the conference once answered
@app.route('/conference/<conference_name>', methods=['GET', 'POST'])
def conference_line(conference_name):
    response = twiml.Response()
    response.dial(hangupOnStar=True).conference(conference_name)
    return Response(str(response), 200, mimetype="application/xml")

if __name__ == '__main__':
    app.run(debug=True)
