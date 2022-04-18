from ppadb.client import Client as AdbClient

import time

import cv2

import pytesseract

import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from PIL import Image

import pyscreeze

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from threading import Thread
import threading

import ctypes

import datetime

class GHCM:
    def __init__(self):
        self.ldata = []
        with open('data/listacc.txt', encoding = 'utf-8') as file:
            listdata = file.read()
        self.ldata = listdata.splitlines()
        self.listserver = []
        with open('data/listserver.txt', encoding = 'utf-8') as file:
            listdata = file.read()
        self.listserver = listdata.splitlines()
        self.listdev = []
    def giaodien(self):
        app = QApplication(sys.argv)
        f = QFile("style.qss")                         
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        style = ts.readAll()
        app.setStyleSheet(style)
        self.w = QWidget()
        self.w.layout = QHBoxLayout()
        self.w.layout.setContentsMargins(0,0,0,0)
        self.w.setWindowIcon(QIcon("icon-game.ico"))
        self.w.title = QLabel("My Own Bar")
        b = QLabel(self.w)
        s = QPushButton(self.w)
        self.e1 = QLineEdit(self.w)
        self.e3 = QLineEdit(self.w)
        # e1.setValidator(QIntValidator())
        # e1.setMaxLength(4)
        # e1.setAlignment(Qt.AlignRight)
        s.setText('Start')
        with open('data/listdevice.txt', encoding = 'utf-8') as file:
            listdata = file.read()
        self.listdev = listdata.splitlines()
        def runmain():
            if len(self.listdev) == 0:
                os.chdir(self.e2.text())
                os.system('NoxConsole.exe adb -index:0 -command:devices')
                al = os.popen('NoxConsole.exe adb -index:0 -command:devices').read()
                listdevi = []
                for a in range(1,len(al.splitlines())):
                    if al.splitlines()[a] != '':
                        devi = al.splitlines()[a][:al.splitlines()[a].find('\t')]  
                        listdevi.append(devi)
                print(listdevi)
                os.chdir(os.path.dirname(os.path.realpath(__file__)))
                with open('data/listdevice.txt', 'w', encoding = 'utf-8') as dev:
                    for d in listdevi:
                        dev.write(d + '\n')
            else:
                listdevi = self.listdev
            for l in listdevi:
                os.system('adb connect ' + l)
            solanchay = len(self.ldata) // int(self.e3.text())
            soluong = int(self.e3.text())
            def runluong(lan):
                thread = []
                tt = 0
                for a in range(int(soluong)*(lan - 1),int(soluong)*lan):
                    tkgame = self.ldata[a].split('|')
                    t = threading.Thread(target=self.main, args=(tkgame[0],tkgame[1],int(self.e1.text()),0,tt))
                    thread.append(t)
                    tt += 1
                for i in thread:
                    i.start()
                for c in thread:
                    c.join()
            def phanluong():
                for a in range(1,solanchay + 1):
                    autolist = threading.Thread(target=runluong , args=(a,))
                    autolist.start()
                    autolist.join()
            threading.Thread(target=phanluong, args=()).start()
        s.clicked.connect(runmain)
        self.w.setWindowTitle("Giang Hồ Chi Mộng Tool")
        b.setText("Tool design by developer Tài Nguyễn - Code tool & thiết kế website theo yêu cầu sdt/zalo 0387865006")
        self.w.setGeometry(0,0,700,500)
        b.move(50,20)
        tb1 = QLabel(self.w)
        tb1.setText("Nhập server mới nhất : ")
        tb1.move(50,50)
        self.e1.move(270,50)
        tb2 = QLabel(self.w)
        tb2.setText("Nhập đường dẫn giả lập nox : ")
        tb2.move(50,90)
        self.e2 = QLineEdit(self.w)
        self.e2.move(270,90)
        tb3 = QLabel(self.w)
        tb3.setText("Nhập số lượng giả lập : ")
        tb3.move(50,130)
        # tb4 = QLabel(self.w)
        # tb4.setText("Nhập thứ tự giả lập")
        # tb4.move(50,170)
        # self.e3 = QLineEdit(self.w)
        # self.e3.move(150,130)
        self.e3.move(270,130)
        s.move(50,170)
        self.w.setWindowTitle("Giang Hồ Chi Mộng Tool")
        self.w.show()
        sys.exit(app.exec_())
    def main(self,user,passw,vitri1,vitri2,thutu):
        os.system('adb devices')
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        device = client.device(devices[thutu].serial)
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract'
        # login
        device.input_tap(322,237)
        device.input_text(user)#0977008378
        device.input_tap(325,270)
        device.input_text(passw)#tienthanh
        device.input_tap(380,305)
        time.sleep(3)
        device.input_tap(475,430)
        time.sleep(1)
        nhanvat = 0
        def crophinh():
            img = cv2.imread('data/screen' + str(thutu) + '.png')
            img_crop = img[138:154,113:136, :]
            img_crop = cv2.resize(img_crop,(50,35))
            crop_name = 'data/lv' + str(thutu) + '.png'
            cv2.imwrite(crop_name, img_crop)
        def doclv():
            for i in range(3,14):
                text1 = pytesseract.image_to_string("data/lv" + str(thutu) + ".png",config = f'--psm {i} --oem 3 -c tessedit_char_whitelist=0123456789')
                # print(text1)
                try:
                    text1 =  int(text1.replace('.',''))
                    break
                except:
                    text1 = 0
                text1 = pytesseract.image_to_string("data/lv" + str(thutu) + ".gif",config = f'--psm {i} --oem 3 -c tessedit_char_whitelist=0123456789')
                # print(text1)
                try:
                    text1 =  int(text1.replace('.',''))
                    break
                except:
                    text1 = 0
            img = 'data/lv' + str(thutu)
            im = Image.open(img + ".png")
            im2 = Image.new("P",im.size,0)
            temp = {}

            for x in range(im.size[1]):
                for y in range(im.size[0]):
                    pix = im.getpixel((y,x))
                    temp[pix] = pix
                    if pix[0] > 130 and pix[1] > 145: # Đây là các màu được lấy_
                        im2.putpixel((y,x),255)
            im2.save(img + ".gif")
            for i in range(3,14):
                text2 = pytesseract.image_to_string("data/lv" + str(thutu) + ".gif",config = f'--psm {i} --oem 3 -c tessedit_char_whitelist=0123456789')
                # print(text1)
                try:
                    text2 =  int(text2.replace('.',''))
                    break
                except:
                    text2 = 0
            if text1 > text2:
                text = text1
            else:
                text = text2
            return text
        def taogif():
            img = 'data/lv' + str(thutu)
            im = Image.open(img + ".png")
            im2 = Image.new("P",im.size,0)
            temp = {}

            for x in range(im.size[1]):
                for y in range(im.size[0]):
                    pix = im.getpixel((y,x))
                    temp[pix] = pix
                    if pix[0] > 130 and pix[1] > 135: # Đây là các màu được lấy_
                        im2.putpixel((y,x),255)
            im2.save(img + ".gif")
        switch={
        0:[405,165],
        1:[645,165],
        2:[400,245],
        3:[645,245],
        4:[400,325],
        5:[650,325],
        6:[400,405],
        7:[660,405]
        }
        luot = 1
        lan = 1
        kiem = 1
        def loadgame():
            time.sleep(3)
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result) 
            img = cv2.imread('data/screen' + str(thutu) + '.png')
            img_crop = img[0:440,0:960, :]
            crop_name = 'data/loadgame' + str(thutu) + '.png'
            cv2.imwrite(crop_name, img_crop)
            kiemtra = pyscreeze.locate('data/loadgame' + str(thutu) + '.png','data/screen' + str(thutu) + '.png', confidence = 0.95)
            while kiemtra != None:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtra = pyscreeze.locate('data/loadgame' + str(thutu) + '.png','data/screen' + str(thutu) + '.png', confidence = 0.95)
            time.sleep(3)                
            return kiemtra            
        def kiemtraanh(src):
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result) 
            kiemtra = pyscreeze.locate(src,'data/screen' + str(thutu) + '.png', confidence = 0.8)
            return kiemtra
        for a in self.listserver:
            device.input_tap(600,377)
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result) 
            kiemtraloi = pyscreeze.locate(r'data/mangbaton.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
            if kiemtraloi != None:
                device.input_tap(480,350)
                time.sleep(1)
                device.input_tap(600,380)
                time.sleep(3)
            time.sleep(3)
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result) 
            kiemtraserver = pyscreeze.locate(r'data/server.png','data/screen' + str(thutu) + '.png')  
            if kiemtraserver != None:
                device.input_tap(215,230)
                time.sleep(1)
                device.input_tap(215,230)
            time.sleep(1)
            vitri = int(vitri1) - int(a) 
            if vitri > 7 and vitri < 16:
            #     if kiem == 1:
                device.input_swipe(510,470,510,170,5000)
                time.sleep(2)
                vitri = vitri - 8
            elif vitri > 15:
                device.input_swipe(510,470,510,170,5000)
                time.sleep(2)
                device.input_swipe(510,470,510,170,5000)
                time.sleep(2)
                vitri = vitri - 16
            device.input_tap(switch.get(vitri)[0],switch.get(vitri)[1])
            #     if lan == 9:
            #         lan = 1
            #         if kiem == 1:
            #             kiem = 2
            #     if lan == 8 and kiem == 2:
            #         luot = 2
            #     # device.input_tap(400,165)
            #     device.input_tap(switch.get(lan)[0],switch.get(lan)[1])
            #     time.sleep(1)
            #     device.input_tap(483,465)
            #     time.sleep(5)
            #     result = device.screencap()
            #     with open("data/screen" + str(thutu) + ".png", "wb") as fp:
            #         fp.write(result) 
            #     crophinh()
            #     taogif()
            #     lv = doclv()
            #     print(lv)
            #     if lv > 179:
            #         nhanvat = 1
            #     else:
            #         device.input_tap(926,30)
            #         time.sleep(3)
            #         device.input_tap(650,400)
            #         time.sleep(3)
            #     lan += 1
            # nhận event
            time.sleep(3)
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result) 
            kiemtraloi = pyscreeze.locate(r'data/mangbaton.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
            if kiemtraloi != None:
                device.input_tap(480,350)
            time.sleep(1)
            device.input_tap(482,470)
            dn = 0
            while dn == 0:
                ktdn = kiemtraanh('data/dangnhap.png')
                if ktdn != None:
                    dn = 1
            device.input_tap(830,470)
            time.sleep(5)
            device.input_tap(850,40)
            loadgame()
            time.sleep(3)
            device.input_tap(410,345)
            time.sleep(1)
            error = 0
            while error == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtraclose = pyscreeze.locate(r'data/close.png',r'data/screen' + str(thutu) + '.png', confidence=0.9)
                if kiemtraclose != None:
                    device.input_tap(kiemtraclose[0],kiemtraclose[1])
                    time.sleep(2)
                else:
                    error = 1
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result)
            kiemtraboss = pyscreeze.locate(r'data/boss.png',r'data/screen' + str(thutu) + '.png', confidence=0.9)
            if kiemtraboss == None:
                device.input_tap(850,25)
                time.sleep(1)
            error = 0
            while error == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtraevent = pyscreeze.locate(r'data/event.png',r'data/screen' + str(thutu) + '.png', confidence=0.9)
                # kiemtrafps = pyscreeze.locate(r'data/fpsthap.png',r'data/screen' + str(thutu) + '.png', confidence=0.9)
                if kiemtraevent != None:
                    device.input_tap(kiemtraevent[0],kiemtraevent[1])
                    error = 1
                else:
                    kiemtraevent2 = pyscreeze.locate(r'data/event2.png',r'data/screen' + str(thutu) + '.png', confidence=0.8)
                    if kiemtraevent2 != None:
                        device.input_tap(kiemtraevent2[0],kiemtraevent2[1])
                        error = 1
                    else:
                        kiemtraevent3 = pyscreeze.locate(r'data/event3.png',r'data/screen' + str(thutu) + '.png', confidence=0.7)
                        if kiemtraevent3 != None:
                            device.input_tap(kiemtraevent3[0],kiemtraevent3[1])
                            error = 1
                # if kiemtrafps != None:
                #     device.input_tap(kiemtrafps[0],kiemtrafps[1])
                kiemtraclose = pyscreeze.locate(r'data/close.png',r'data/screen' + str(thutu) + '.png', confidence=0.9)
                if kiemtraclose != None:
                    device.input_tap(kiemtraclose[0],kiemtraclose[1])
                    time.sleep(2)
            time.sleep(3)
            result = device.screencap()
            with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                fp.write(result)
            kiemtraqua = pyscreeze.locate(r'data/quadn.png',r'data/screen' + str(thutu) + '.png', confidence=0.9)
            if kiemtraqua != None:
                device.input_tap(kiemtraqua[0],kiemtraqua[1])
                time.sleep(1)
            device.input_tap(842,236)
            time.sleep(1)
            device.input_tap(842,316)
            time.sleep(1)
            device.input_tap(850,400)
            time.sleep(1)
            device.input_tap(930,25)
            time.sleep(1)
            error = 0
            while error == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtraboss = pyscreeze.locate(r'data/boss.png',r'data/screen' + str(thutu) + '.png', confidence=0.9)
                if kiemtraboss != None:
                    device.input_tap(kiemtraboss[0],kiemtraboss[1])
                    error = 1
            error = 0
            while error == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtraanc = pyscreeze.locate(r'data/acnhancoc.png',r'data/screen' + str(thutu) + '.png', confidence=0.8)
                if kiemtraanc != None:
                    device.input_tap(kiemtraanc[0],kiemtraanc[1])
                    error = 1
            error = 0
            while error == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtraanc = pyscreeze.locate(r'data/denngay.png',r'data/screen' + str(thutu) + '.png', confidence=0.8)
                if kiemtraanc != None:
                    device.input_tap(kiemtraanc[0],kiemtraanc[1])
                    error = 1
            error = 0
            while error == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtraanc = pyscreeze.locate(r'data/dongy.png',r'data/screen' + str(thutu) + '.png', confidence=0.8)
                if kiemtraanc != None:
                    device.input_tap(kiemtraanc[0],kiemtraanc[1])
                    error = 1       
            time.sleep(5)
            error = 0
            while error == 0:
                result = device.screencap()
                with open("data/screen" + str(thutu) + ".png", "wb") as fp:
                    fp.write(result)
                kiemtraboss = pyscreeze.locate(r'data/fullno.png',r'data/screen' + str(thutu) + '.png', confidence=0.65)
                if kiemtraboss != None:
                    device.input_tap(kiemtraboss[0],kiemtraboss[1])
                    error = 1
            time.sleep(2)
            device.input_tap(252,342)
            time.sleep(1)
            device.input_tap(840,55)
            time.sleep(1)
            device.input_tap(120,83)
            time.sleep(2)
            device.input_tap(101,106)
            time.sleep(5)
            device.input_tap(871,240)
            time.sleep(3)
            # doi full no
            error = 0
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
        time.sleep(1)
        result = device.screencap()
        with open("data/screen" + str(thutu) + ".png", "wb") as fp:
            fp.write(result) 
        kiemtraloi = pyscreeze.locate(r'data/mangbaton.png','data/screen' + str(thutu) + '.png' , confidence=0.8)
        if kiemtraloi != None:
            device.input_tap(480,350)
        device.input_tap(915,18)
        time.sleep(3)
        # def matmang():
        #     t = threading.Thread(target=framno , args=(user,passw,vitri1,vitri2))
        #     t.start()
        #     while True:
        #         result = device.screencap()
        #         with open("data/screen" + str(thutu) + ".png", "wb") as fp:
        #             fp.write(result) 
        #         kiemtramang = pyscreeze.locate(r'data/mangbaton.png',r'data/screen'+ str(thutu) + '.png')  
        #         if kiemtramang != None:
        #             device.input_tap(486,348)    
        #             thread_id = t.native_id
        #             res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
        #                 ctypes.py_object(SystemExit))
        #             if res > 1:
        #                 ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        #                 time.sleep(1)
        #             t = threading.Thread(target=framno , args=(user,passw,vitri1,vitri2))
        #             t.start()
        # luongdangchay = []
        # m = threading.Thread(target=matmang , args=())
        # luongdangchay.append(m)
        # luongdangchay[0].start()

GHCM().giaodien() # 276 111