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


def pickinginfo(ordernumber):
    url = 'http://192.168.44.54:8761/ezsale-order/outbound-order/page'
    body = {
        "current": 1,
        "size": 50,
        "state": "1",
        "warehouseType": "self",
        "platformOrderId": ordernumber
    }
    response = requests.post(url, data = json.dumps(body), headers = headers)
    resjson = response.json()
    print("resjson:{}".format(resjson))
    if len(resjson['data']['records']) == 0:
        print("该订单号不存在拣货中列表")
    else:
        id = resjson['data']['records'][0]['id']
        print("id:{}".format(id))
        return id


def pickingrecord(ordernumber):
    id = pickinginfo(ordernumber)
    url = 'http://192.168.44.54:8761/ezsale-warehouse/wh/pick/list/record'
    body = {"id":id}
    response = requests.post(url, data=json.dumps(body), headers=headers)
    #print(response.json())
    resjson = response.json()
    pickListRecords = resjson['data']['pickListRecords']

    pickdatalist = []
    for i in pickListRecords:
        pickListRecord = {}
        pickListRecord['outboundOrderId'] = i['outboundOrderId']
        pickListRecord['sku'] = i['sku']
        pickListRecord['num'] = i['num']
        pickListRecord['encode'] = i['encode']
        pickdatalist.append(pickListRecord)
    print("pickdatalist:{}".format(pickdatalist))
    return pickdatalist


def get_good_shelve_info(sku):
    url = 'http://192.168.44.54:8761/ezsale-warehouse/wh/goods/page'
    data = {
        'current': 1,
        'size': 50,
        'goodsType': 2,
        'state': 0,
        'sku': sku
    }
    r = requests.get(url, headers = headers, params = data)
    resjson = r.json()
    #print(resjson)
    #获取货架编号和id
    shelve = resjson['data']['records'][0]['encodeList']
    print("shelve:{}".format(shelve))
    return shelve

# 单次拣货
def pick(goodsShelvesId):
    url = 'http://192.168.44.54:8761/ezsale-warehouse/wh/pick/list/pick'
    body = {
        "outboundOrderId":outboundOrderId,
        "goodsShelvesId":goodsShelvesId
    }
    response = requests.post(url, data=json.dumps(body), headers=headers)
    resjson = response.json()
    print(resjson)

#根据商户订单号进行批量拣货
def batchpick(ordernumber):
    pickdatalist = pickingrecord(ordernumber)
    for i in pickdatalist:
        outboundOrderId = i['outboundOrderId']
        sku = i['sku']
        encode =i['encode']
        print("encode:{}".format(encode))
        num = i['num']
        shelves = get_good_shelve_info(sku)
        for shelve in shelves:
            if shelve['encode'] == encode:
                for count in range(num):
                    print("outboundOrderId:{}".format(outboundOrderId),"shelve['id']:{}".format(shelve['id']))
                    pick(shelve['id'])

if __name__ == "__main__":
    # login()
    #gettoken()
    #pickinginfo('chubin2021918001')
    #pickingrecord()
    #get_good_shelve_info()
    batchpick('chubin20210715th140')




