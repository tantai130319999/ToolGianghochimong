from ppadb.client import Client as AdbClient
import os
os.system('NoxConsole.exe adb -index:0 -command:devices')
al = os.popen('NoxConsole.exe adb -index:0 -command:devices').read()
listdevi = []
for a in range(1,len(al.splitlines())):
    if al.splitlines()[a] != '':
        devi = al.splitlines()[a][:al.splitlines()[a].find('\t')]  
        listdevi.append(devi)
print(listdevi)
with open('data/listdevice.txt', 'w', encoding = 'utf-8') as dev:
    for d in listdevi:
        dev.write(d + '\n')