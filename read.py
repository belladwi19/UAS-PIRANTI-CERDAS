import serial
import requests

urls = "http://192.168.147.235/savedb.php"
arduino = serial.Serial("COM4", timeout=1, baundrate=9600)

while True:
    a = arduino.readline().decode("utf-8").strip('\n').strip('\r')
    if(a!=''):
        temp = a.split(';')
        data = {
            'Tt':float(temp[1]),
            'Hh':float(temp[0]),
            'Pp':float(temp[2]),
        }
        res = requests.post(url = urls, data = data)
        print(res.text)