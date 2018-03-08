#-*- coding: UTF-8 -*-
import time
import requests
import numpy as np
import functools


headers=[
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
]

class BishijieSpider(object):
    
    # 查询新闻
    def getNews(self, num = 50, startTime = int(time.time())):
        url = "http://www.bishijie.com/api/news?size=" + str(num) + "&timestamp=" + str(startTime)
        res = requests.get(url, headers=headers[np.random.randint(0,len(headers))])

        if (res.status_code >= 400):
            print('error')
            return

        json = res.json()

        if json["error"]:
            print('error')
            return 
        
        return functools.reduce(lambda prev, item: prev + item["buttom"], json["data"].values(), [])

    def filterNewsByRank(self, data, rank = 1):
        return list(filter(lambda item: item["rank"] == rank, data))

if __name__ == "__main__":
    news = BishijieSpider().getNews()
    print(len(news))
    