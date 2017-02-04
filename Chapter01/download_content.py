from bs4 import BeautifulSoup
import re
import urllib2
import os

## Download paramters
image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"

##Create Soup Object and find images from the search
header = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)), "lxml")
images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})][:5]
for img in images:
    print "Image Source:", img

# Go through all the urls and download images
for img in images:
    raw_img = urllib2.urlopen(img).read()
    cntr = len([i for i in os.listdir(".") if image_type in i]) + 1
    f = open(image_type + "_"+ str(cntr)+".jpg", 'wb')
    f.write(raw_img)
    f.close()
