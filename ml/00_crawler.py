import time
from download_util import download
from bottlenose import api
from bs4 import BeautifulSoup

AMAZON_ACCESS_KEY_ID="AMAZON_ACCESS_KEY_ID"
AMAZON_SECRET_KEY="AMAZON_SECRET_KEY"
AMAZON_ASSOC_TAG="AMAZON_ASSOC_TAG"

amazon = api.Amazon(AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region="JP")

for i in range(10):
    try:
        response = amazon.ItemSearch(SearchIndex="Books", Keywords="PHP", ItemPage=i+1, ResponseGroup="Large")
        soap = BeautifulSoup(response, "lxml")
        [download(x.string.strip()) for x in soap.select("imageset[category=primary] smallimage url")]
    except:
        i = i - 1
        print("except:" + str(i))
    print(i + 1)
    time.sleep(1)
