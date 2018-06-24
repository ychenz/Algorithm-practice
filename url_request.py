import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json

def getMovieTitles(substr):
    item_list = []

    req = Request("https://jsonmock.hackerrank.com/api/movies/search/?Title=" + substr)
    response = urlopen(req).read()
    data = json.loads(response.decode('utf-8'))

    total = data["total"]
    total_result = [""]*total

    page_count = data["total_pages"]
    page = int(data["page"])
    item_list += data["data"]

    while page < page_count:
        page += 1
        req = Request("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(substr, page))
        response = urlopen(req).read()
        data = json.loads(response.decode('utf-8'))
        item_list += data["data"]

    for i in range(0,len(item_list)):
        total_result[i] = item_list[i]["Title"]

    return total_result


if __name__ == '__main__':
    print(getMovieTitles("spiderman"))