#Python将base64解码以字节流形式写成zip
import base64

with open('data2.txt','rb') as file:
    with open('res.zip','wb') as new_file:
        new_file.write(base64.b64decode(file.read()))
