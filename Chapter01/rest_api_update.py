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

data = {
  "description": "Updating the description for this gist",
  "files": {
    "file1.txt": {
      "content": "Updating file contents.."
    }
  }
}

url = "/gists/%s" % gist_id
r = requests.patch('%s%s' %(BASE_URL, url),
                 headers=header,
                 data=json.dumps(data))
print r.json()
