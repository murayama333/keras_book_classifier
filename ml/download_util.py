import os.path
import urllib
from pyquery import PyQuery as pq

def download(url, path="download"):
    img = urllib.request.urlopen(url)
    filename = path + "/" + os.path.basename(url)
    print(filename)
    localfile = open(filename, 'wb')
    localfile.write(img.read())
    img.close()
    localfile.close()
