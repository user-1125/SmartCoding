import qrcode

filePath = 'QRcode\\qrList.txt'

f = open(filePath, 'r', encoding='UTF-8')
lines = f.readlines()

for line in lines : 
    line = line.strip()
    qrImg = qrcode.make(line)

    savePath = './/' + line + ".png"
    qrImg.save(savePath)
    
f.close()