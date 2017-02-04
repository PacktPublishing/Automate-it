import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = '<username>'
api_token = '<api_token>'
gist_id = '<gist_id>'

header = {  'X-Github-Username': '%s' % username,
            'Content-Type': 'application/json',
            'Authorization': 'token %s' % api_token,
}

url = "/gists/%s" % gist_id
r = requests.delete('%s%s' %(BASE_URL, url),
                 headers=header,
)
print r
