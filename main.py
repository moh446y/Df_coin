import requests
import json
import time

url = "https://bfdcoin.org/api.php"

params = {
    'act': "collectCoin"
}

payload = json.dumps(89)

headers_template = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 13; M2101K9AG Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.82 Mobile Safari/537.36",
    'Accept': "application/json, text/plain, */*",
    'Content-Type': "application/json",
    'sec-ch-ua': "\"Android WebView\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    'sec-ch-ua-mobile': "?1",
    'sec-ch-ua-platform': "\"Android\"",
    'origin': "https://bfdcoin.org",
    'x-requested-with': "org.telegram.messenger",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://bfdcoin.org/",
    'accept-language': "ar,ar-EG;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
    'Cookie': "_ga=GA1.1.743556070.1717005512; _ga_108Z40HT1L=GS1.1.1717270254.5.1.1717271659.0.0.0"
}

# قائمة التوكينز
tokens = ["1606557047", "6880544702" ,"7052127034" ,"6380423966","7195822647", "6373998912","7191785097" ,"6972296537", "5628090158", "1306866443", "7447972445","5611407285","7158065365"]

while True:
    for token in tokens:
        headers = headers_template.copy()
        headers['token'] = token
        
        try:
            response = requests.post(url, params=params, data=payload, headers=headers)
            response_data = response.json()
            
            print(f"Response for token {token}: {response_data}")
            
            if response_data.get("code") == 0:
                print(f"Request successful for token {token}.")
            else:
                print(f"Request failed for token {token}. Waiting for 30 seconds.")
                time.sleep(30)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred for token {token}: {e}")
    
    time.sleep(20)