import qrcode


qrData = 'www.naver.com'
qrImg = qrcode.make(qrData)

savePath = '.\\' + qrData + '.png'
qrImg.save(savePath)