from ppadb.client import Client as AdbClient
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

os.system('adb connect 127.0.0.1:62025')
os.system('adb devices')
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = client.device(devices[0].serial)
result = device.screencap()
with open("data/screen.png", "wb") as fp:
    fp.write(result) 
print("Đã chụp")