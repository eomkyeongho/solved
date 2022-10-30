import requests
import re
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
url = "https://solved.ac/profile/"

def getRating(id):
    req_url = url + id
    res = requests.get(req_url, headers=headers)
    res.raise_for_status()
    index = res.text.find("\"tier\"")
    subStr = res.text[index:index+50]
    index = subStr.find("\"rating\"") + 9
    rating = subStr[index:index+4]
    rating = rating.replace(',', '')
    rating = rating.replace('\"','')
    rating = rating.replace('r','')

    if rating is '':
        return -1
    else:
        return int(rating)


