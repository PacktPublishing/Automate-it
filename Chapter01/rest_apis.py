import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = '<username>'
api_token = '<api_token>'
header = {  'X-Github-Username': '%s' % username,
            'Content-Type': 'application/json',
            'Authorization': 'token %s' % api_token,
}


url = "/users/%s/gists" % username
r = requests.get('%s%s' % (BASE_URL, url),
                 headers=header)
gists = r.json()
for gist in gists:
    data = gist['files'].values()[0]
    print data['filename'], data['raw_url'], data['language']



