from flask import Flask
import twilio.twiml

app = Flask(__name__)

#flask route to work on callback url for incoming SMS
@app.route("/insms", methods=['GET', 'POST'])
def respond_sms():
    resp = twilio.twiml.Response()
    resp.message("Thanks for your query. We will get back to you soon")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
