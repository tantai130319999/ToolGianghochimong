import pytesseract

from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract'

import pyscreeze

import time

import os

from ppadb.client import Client as AdbClient

import subprocess

import cv2

# os.chdir('D:\\Program Files\\Nox\\bin')
# os.chdir(os.path.dirname(os.path.realpath(__file__)))
# os.system('NoxConsole.exe adb -index:0 -command:devices')
# al = os.popen('NoxConsole.exe adb -index:0 -command:devices').read()
# listdevi = []
# for a in range(1,len(al.splitlines())):
#     if al.splitlines()[a] != '':
#       devi = al.splitlines()[a][:al.splitlines()[a].find('\t')]  
#       listdevi.append(devi)
# print(listdevi)
# listdev = []
# with open('data/listdevice.txt', encoding = 'utf-8') as file:
#     listdata = file.read()
# listdev = listdata.splitlines()
# listaaa = ['127.0.0.1:62001', '127.0.0.1:62025']
# with open('data/listdevice.txt', 'w') as file:
#       for a in listaaa:
#         file.write(a + '\n')
kiemtraserver = pyscreeze.locate('data/offauto.png','data/screen.png',confidence = .8)
print(kiemtraserver)
# print(cv2.__file__)
# for i in range(3,14):
#     text1 = pytesseract.image_to_string("data/525.png",config = f' --psm {i} --oem 3 ')
#     print(text1)
# os.system('adb connect 127.0.0.1:62025')
# os.system('adb connect 127.0.0.1:62001')
# os.system('adb devices') 
# client = AdbClient(host="127.0.0.1", port=5037)
# devices = client.devices()
# device = client.device(devices[0].serial)
# error = 0
# while error == 0:
#     result = device.screencap()
#     with open("data/screen.png", "wb") as fp:
#         fp.write(result)
#     kiemtraclose = pyscreeze.locate(r'data/event.png',r'data/screen.png', confidence=.8)
#     if kiemtraclose != None:
#         device.input_tap(kiemtraclose[0],kiemtraclose[1])
#         error = 1
#     else:
#         pass
os.system('adb connect 127.0.0.1:62001')
os.system('adb devices')
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = client.device(devices[0].serial)
error = 0
thutu = 0
def loadgame():
    time.sleep(3)
    result = device.screencap()
    with open("data/screen" + str(thutu) + ".png", "wb") as fp:
        fp.write(result) 
    img = cv2.imread('data/screen' + str(thutu) + '.png')
    img_crop = img[0:440,0:960, :]
    crop_name = 'data/loadgame' + str(thutu) + '.png'
    cv2.imwrite(crop_name, img_crop)
    kiemtra = pyscreeze.locate('data/loadgame' + str(thutu) + '.png','data/screen' + str(thutu) + '.png', confidence = 0.9)
    while kiemtra != None:
        result = device.screencap()
        with open("data/screen" + str(thutu) + ".png", "wb") as fp:
            fp.write(result)
        kiemtra = pyscreeze.locate('data/loadgame' + str(thutu) + '.png','data/screen' + str(thutu) + '.png', confidence = 0.9)
    time.sleep(3)                
    return kiemtra            
def kiemtraanh(src):
    result = device.screencap()
    with open("data/screen" + str(thutu) + ".png", "wb") as fp:
        fp.write(result) 
    kiemtra = pyscreeze.locate(src,'data/screen' + str(thutu) + '.png', confidence = 0.8)
    return kiemtra
while error == 0:
    result = device.screencap()
    with open("data/screen"  + str(thutu) +  ".png", "wb") as fp:
        fp.write(result)
    kiemtraclose = pyscreeze.locate(r'data/fullno.png','data/screen' + str(thutu) + '.png', confidence=.65)
    kiemtrahoisinh = pyscreeze.locate(r'data/hoisinh.png','data/screen' + str(thutu) + '.png', confidence=.8)
    kiemtraloi = pyscreeze.locate(r'data/mangbaton.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
    kiemtralogout = pyscreeze.locate(r'data/icon-game.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
    kiemtraload = pyscreeze.locate(r'data/loading.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
    kiemtraboss = pyscreeze.locate(r'data/lammoiboss.png','data/screen' + str(thutu) + '.png' , confidence=0.9)
    kiemtratab = pyscreeze.locate(r'data/close.png','data/screen' + str(thutu) + '.png' , confidence=0.9)
    kiemtraoff = pyscreeze.locate(r'data/offauto.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
    if kiemtraboss != None:
        device.input_tap(432,286)
        time.sleep(1)
        device.input_tap(550,333)
    elif kiemtratab != None:
        device.input_tap(kiemtratab[0],kiemtratab[1])
    elif kiemtraload != None:
        while kiemtralogout == None:
            result = device.screencap()
            with open("data/screen"  + str(thutu) +  ".png", "wb") as fp:
                fp.write(result)
            kiemtralogout = pyscreeze.locate(r'data/icon-game.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
        device.input_tap(kiemtralogout[0],kiemtralogout[1])
        loadgamee = kiemtraanh('data/dn2.png')
        while loadgamee == None:
            loadgamee = kiemtraanh('data/dn2.png')
        device.input_tap(485,465)
        time.sleep(3)
        device.input_tap(830,475)
        time.sleep(30)
        device.input_tap(911,23)
        time.sleep(1)
        device.input_tap(252,342)
        time.sleep(1)
        device.input_tap(840,55)
        time.sleep(1)
        device.input_tap(120,83)
        time.sleep(2)
        device.input_tap(101,106)
        time.sleep(30)
        device.input_tap(871,240)
    elif  kiemtralogout != None:
        device.input_tap(kiemtralogout[0],kiemtralogout[1])
        loadgamen = kiemtraanh('data/dn2.png')
        while loadgamen == None:
            loadgamen = kiemtraanh('data/dn2.png')
        device.input_tap(485,465)
        time.sleep(3)
        device.input_tap(830,475)
        time.sleep(3)
        loadgame()
        device.input_tap(911,23)
        time.sleep(1)
        device.input_tap(252,342)
        time.sleep(1)
        device.input_tap(840,55)
        time.sleep(1)
        device.input_tap(120,83)
        time.sleep(2)
        device.input_tap(101,106)
        time.sleep(10)
        device.input_tap(871,240)
    elif kiemtraloi != None:
        device.input_tap(480,350)
        time.sleep(1)
        device.input_tap(480,465)
        time.sleep(3)
        device.input_tap(830,475)
        time.sleep(3)
        loadgame()
        device.input_tap(911,23)
        time.sleep(1)
        device.input_tap(252,342)
        time.sleep(1)
        device.input_tap(840,55)
        time.sleep(1)
        device.input_tap(120,83)
        time.sleep(2)
        device.input_tap(101,106)
        time.sleep(10)
        device.input_tap(871,240)
    elif kiemtrahoisinh != None:
        time.sleep(10)
        device.input_tap(911,23)
        time.sleep(1)
        device.input_tap(252,342)
        time.sleep(1)
        device.input_tap(840,55)
        time.sleep(10)
        device.input_tap(871,240)
    elif kiemtraclose == None:
        error = 1
        nhanvat = 0
        # dang xuat
        loadgame()
        error = 0
        while error == 0:
            device.input_tap(48,45)
            time.sleep(3)
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result) 
            kiemtraloi = pyscreeze.locate(r'data/sanhcho.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
            if kiemtraloi != None:
                device.input_tap(98,508)
                error = 1
        time.sleep(3)
        loadgame()
        device.input_tap(925,30)
        time.sleep(3)
    elif kiemtraoff != None:
        time.sleep(1)
        device.input_tap(911,23)
        time.sleep(1)
        device.input_tap(252,342)
        time.sleep(1)
        device.input_tap(840,55)
        time.sleep(10)
        result = device.screencap()
        with open("data/screen" + str(thutu) + ".png", "wb") as fp:
            fp.write(result) 
        kiemtraloi = pyscreeze.locate(r'data/offauto.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
        if kiemtraloi != None:
            device.input_tap(kiemtraloi[0],kiemtraloi[1])
        time.sleep(3)
    else:
        pass

# img = cv2.imread('data/screen.png')
# img_crop = img[138:155,113:136, :]
# crop_name = 'data/lv.png'
# img_crop = cv2.resize(img_crop,(50,35))
# cv2.imwrite(crop_name, img_crop)
# # resize = Image.open("data/lv.png")
# # lvnew = resize.resize((50,35))
# # Image.save()
# img = 'data/lv1'
# im = Image.open(img + ".png")
# im2 = Image.new("P",im.size,0)

# temp = {}

# for x in range(im.size[1]):
#     for y in range(im.size[0]):
#         pix = im.getpixel((y,x))
#         temp[pix] = pix
#         if pix[0] > 130 and pix[1] > 145: # Đây là các màu được lấy_
#             im2.putpixel((y,x),255)
# im2.save(img + ".gif")
# for i in range(3,14):
#     text1 = pytesseract.image_to_string("data/lv0.png",config = f'-c tessedit_char_whitelist=0123456789 --psm {i} --oem 3 ')
#     print(text1.replace('Lv.',''))
#     try:
#         text1 =  int(text1)
#         print(text1)
#         break
#     except:
#         pass
