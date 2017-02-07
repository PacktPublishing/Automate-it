from flask import Flask
from flask import request
import requests, json

app = Flask(__name__)

def send_weburl(payload, recipient_id):
    headers = {
        "Content-Type": "application/json"
    }
    token = {
        "access_token":
        "TOKEN"
    }

    if payload == 'Python':
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message":{
                "attachment":{
                  "type":"template",
                  "payload":{
                    "template_type":"generic",
                    "elements":[
                      {
                        "title":"Learn Python Design Patterns: Chetan Giridhar",
                        "item_url":"https://www.amazon.com/Learning-Python-Design-Patterns-Second/dp/178588803X",
                        "image_url":"https://images-na.ssl-images-amazon.com/images/I/51bNOsKpItL._SX404_BO1,204,203,200_.jpg",
                        "subtitle":"Python Book for software architects and developers",
                        "buttons":[
                          {
                            "type":"web_url",
                            "url":"https://www.amazon.com/Learning-Python-Design-Patterns-Second/dp/178588803X",
                            "title":"Buy",
                            "webview_height_ratio":"full"
                          }
                        ]
                      }
                    ]
                  }
                }
            }
        })

    if payload == 'Java':
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message":{
                "attachment":{
                  "type":"template",
                  "payload":{
                    "template_type":"generic",
                    "elements":[
                      {
                        "title":"RESTful Java Patterns and Best Practices: Bhakti Mehta",
                        "item_url":"https://www.amazon.com/RESTful-Java-Patterns-Best-Practices/dp/1783287969",
                        "image_url":"https://images-na.ssl-images-amazon.com/images/I/51YnSP6uqeL._SX403_BO1,204,203,200_.jpg",
                        "subtitle":"Python Book for software architects and developers",
                        "buttons":[
                          {
                            "type":"web_url",
                            "url":"https://www.amazon.com/RESTful-Java-Patterns-Best-Practices/dp/1783287969",
                            "title":"Buy",
                            "webview_height_ratio":"full"
                          }
                        ]
                      }
                    ]
                  }
                }
            }
        })

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params=token, headers=headers, data=data)

def send_postback(recipient_id):
    headers = {
        "Content-Type": "application/json"
    }
    token = {
        "access_token":
        "TOKEN"
    }

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        'message': {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Hey there, Welcome to MyBooks. What are you interested in?",
                    "buttons": [
                          {
                            "type":"postback",
                            "title":"Java",
                            "payload":"Java"
                          },
                          {
                            "type":"postback",
                            "title":"Python",
                            "payload":"Python"
                          }
                    ]
                }
            }
        }
    })

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params=token, headers=headers, data=data)


@app.route("/bot/", methods=['GET', 'POST'])
def hello():
    print request.data
    if request.method == 'GET':
        return request.args.get('hub.challenge')

    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("postback"):
                    sender_id = messaging_event["sender"]["id"]
                    payload = messaging_event["postback"]["payload"]
                    send_weburl(payload, sender_id)

                if messaging_event.get("message"):  # readers send us a message
                    sender_id = messaging_event["sender"]["id"]
                    send_postback(sender_id)


    return "ok", 200


if __name__ == "__main__":
    app.run()