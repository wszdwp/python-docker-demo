import json
import requests

class Price:    
    def __init__(self):
        self.baseUrl = "https://nc.mofcom.gov.cn/jghq/priceList"
        
    def getPrice(self, requestJson = {}):
        if requestJson is None:
            requestJson = {
                'craftIndex': 13235,
                'craftName': '牛肉',
                'pIndex': 50,
                'queryDateType': 0,
                'pageNo': 1
            }
        print("checking price with " + str(requestJson))
        res = requests.post(self.baseUrl, json = requestJson)
        return json(res)

