import requests
import json
import captcha


def login():
    yanzheng = captcha.get_captcha()
    url = 'http://192.168.44.54:8761/ezsale-auth/oauth/login/token'
    headers = {
        'content-type': "application/json",
        'Captcha-Code':yanzheng['code'],
        'Captcha-Key':yanzheng['key'],
        'Authorization':'Basic MTIzNDU2OjEyMzQ1NjQ3Nzc3Nw=='
    }
    body = {
        "account": "chubin-th1",
        "password": "3f11b25ee9461d86cb45af37e8a35e22",
        "tenantId": "00000001",
        "grantType": "captcha"
    }
    response = requests.post(url, data = json.dumps(body), headers = headers)
    resjson = response.json()
    print(resjson)
    token = "bearer " + resjson['data']['accessToken']
    print(token)
    with open(r"C:\Users\Administrator\Documents\python\token.txt","w") as f:
        f.write(token)


def gettoken():
    with open(r"C:\Users\Administrator\Documents\python\token.txt", "r") as f:
        token = f.read()
        return token

accesstoken = gettoken()
headers = {
    'ezsale-auth': accesstoken,
    'Content-Type': 'application/json;charset=UTF-8'
}


def jianhuozhong():
    url = 'http://192.168.44.54:8761/ezsale-order/outbound-order/page'
    body = {
        "current":1,
        "size":500,
        "state":"1",
        "warehouseType":"self"
    }
    response = requests.post(url, data = json.dumps(body), headers = headers)
    resjson = response.json()
    #print("resjson:{}".format(resjson))
    records = resjson['data']['records']
    outids = []
    for outid in records:
        outids.append(outid['id'])
    print(outids)
    return outids

def biaojiyichang():
    url = 'http://192.168.44.54:8761/ezsale-order/outbound-order/mark-abnormal'
    body = {
        "state":1,
        "remark":"1212",
        #"outboundOrderId":outid
    }
    outids = jianhuozhong()
    for outid in outids:
        body['outboundOrderId'] = outid
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(response)

def jianhuoyichang():
    url = 'http://192.168.44.54:8761/ezsale-order/outbound-order/page'
    body = {
        "current":1,
        "size":500,
        "state":"3",
        "warehouseType":"self"
    }
    response = requests.post(url, data = json.dumps(body), headers = headers)
    resjson = response.json()
    #print("resjson:{}".format(resjson))
    records = resjson['data']['records']
    outids = []
    for outid in records:
        outids.append(outid['id'])
    print(outids)
    return outids

def huigun():
    outids = jianhuoyichang()
    for outid in outids:
        print(type(outid))
        url = 'http://192.168.44.54:8761/ezsale-order/outbound-order/cancel/order-ship/'
        url += outid
        print(url)
        response = requests.post(url,data=None, headers=headers)
        resjson = response.json()
        print("resjson:{}".format(resjson))





if __name__ == "__main__":
    # login()
    # jianhuozhong()
    biaojiyichang()
    huigun()




