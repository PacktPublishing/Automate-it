from datetime import datetime
import pytz
from pytz import timezone
from fpdf import FPDF, HTMLMixin
import calendar

#Representation of Users data
users = [{"id":12, "name":"John", "city":"New York", "timezone":"US/Eastern"}, 
         {"id":13, "name":"Johny", "city":"Indiana", "timezone":"US/Central"}]

#Payments done by the users. All time stamps are in UTC
payments = [{"id":12, "amount":12.00, "created_at":"2016-11-29T11:46:07.141Z"}, 
	    {"id":13, "amount":22.00, "created_at":"2016-11-30T23:46:07.141Z"}, 
	    {"id":12, "amount":5.00, "created_at":"2016-12-01T01:00:00.141Z"}]

#Platform usage from users
usage = [{"id":12, "charge":5.00, "created_at":"2016-11-29T11:46:07.141Z"}]

user_ids = []
user_names = []
for usr in users:
  user_ids.append(usr["id"])
  user_names.append(usr["name"])

#Get payments for user based on user_id and month
def get_payments(user_id, month):
  tz = [ x for x in users if x["id"] == user_id]
  tot_payment = 0.00
  for p in payments:
    dt = datetime.strptime(p["created_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
    dt = dt.replace(tzinfo=pytz.UTC)
    dt = dt.astimezone(timezone(tz[0]["timezone"])) 		
    if p["id"] == user_id and dt.month == month:
       tot_payment += p["amount"]
  return tot_payment

#Get platform usage for user based on user_id and month
def get_usage(user_id, month):
  tz = [ x for x in users if x["id"] == user_id]
  tot_usage = 0.00
  for u in usage:
    dt = datetime.strptime(u["created_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
    dt = dt.replace(tzinfo=pytz.UTC)
    dt = dt.astimezone(timezone(tz[0]["timezone"]))
    if u["id"] == user_id and dt.month == month:
      tot_usage += u["charge"]
  return tot_usage

#Generate invoice template in HTML
def get_invoice(user_name, user_id, month):
  html = """
    <p>Anzee Corporation</p><br>
    <b><p>Account Name: """ + user_name + """</p>
    <p>Invoice for month of: """ + str(calendar.month_name[month]) + """</p></b>
    <br><br>	
    <p><b>Payments and Usage:</b></p>	
    <table align="center" width="50%">
        <thead>
            <tr>
                <th align="left" width="50%">Charge Type</th>
                <th align="right" width="50%">Amount</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Payments Done</td>
                <td align="right">$""" + str(get_payments(user_id, month)) + """</td>
            </tr>
            <tr>
                <td>Total Usage</td>
                <td align="right">$""" + str(get_usage(user_id, month)) + """</td>
            </tr>
        </tbody>
    </table>
    <br><br>
  """
  return html

class MyFPDF(FPDF, HTMLMixin):
   pass

html = get_invoice("John", 12, 11)
pdf=MyFPDF()
pdf.add_page()
pdf.write_html(html)

#Generate invoice in PDF format
pdf.output('invoice.pdf','F')
