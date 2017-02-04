from lxml import html
import requests

#Get call on pricing page of Github
page = requests.get('https://github.com/pricing/')

#Get the page contents in a HTML tree format
tree = html.fromstring(page.content)
print("Page Object:", tree)

#Select HTML elements and get data
plans = tree.xpath('//h2[@class="pricing-card-name alt-h3"]/text()')
pricing = tree.xpath('//span[@class="default-currency"]/text()')

#Print the extracted data
print("Plans:", plans, "\nPricing:", pricing)
