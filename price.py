
import requests

class Price:
    baseUrl = ""
    
    def __init__(self):
        self.baseUrl = "https://nc.mofcom.gov.cn/jghq/priceList"
        
    def getPrice(self, form = {}):
        form = {
            'craftIndex': 13235,
            'craftName': None,
            'pIndex': 50,
            'queryDateType': 0,
            'pageNo': 1
        }
        res = requests.post(self.baseUrl, json = form)
        print(res)
        return res

