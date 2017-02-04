from flask import Flask, request
import twilio.twiml

#Pizza class to manage status
class Pizza:
    def __init__(self):
        self.status = None

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

#Incoming message routes served by flask app
app = Flask(__name__)
@app.route("/insms", methods=['GET', 'POST'])
def respond_sms():
    content = request.POST['Body']
    resp = twilio.twiml.Response()
    #If incoming SMS is to place an order
    if content == 'ORDER':
        resp.message("Thanks! We're already on your order!")
        pizza = Pizza()
        pizza.setStatus('complete')
        return str(resp)
    #If incoming SMS is to query the order
    if content == 'STATUS':
        pizza = Pizza()
        status = pizza.getStatus()
        if status == 'complete':
            resp.message("Your order is ready!")
            return str(resp)
        else:
            resp.message("Sorry! could not locate your order!")
            return str(resp)
    #Wrong message format
    else:
        resp.message("Sorry! Wrong selection")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
