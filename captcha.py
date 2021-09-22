
import ddddocr
import requests
import base64

def get_captcha():
    url = "http://192.168.44.54:8761/ezsale-auth/oauth/captcha"
    r = requests.get(url = url)
    resjson = r.json()
    #print(resjson)
    image = resjson['data']['image']
    #print(image)
    final_image = image[22:]
    #print(final_image)
    captcha = {}
    captcha['key'] = resjson['data']['key']

    with open(r'C:\Users\Administrator\Documents\python\test.png', 'wb') as f:
        f.write(base64.b64decode(final_image))

    ocr = ddddocr.DdddOcr()
    with open(r'C:\Users\Administrator\Documents\python\test.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    captcha['code'] = res
    print(captcha)
    return captcha

if __name__ == "__main__":
    yanzengma = get_captcha()

