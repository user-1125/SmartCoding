import cv2

face_cascade = \
            cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img = cv2.imread(r'OpenCV\group.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 5)

for (x,y,w,h) in faces:

    face_img = img[y:y + h, x:x+ w]

    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.05, fy = 0.05)

    face_img = cv2.resize(face_img, (w, h), interpolation = cv2.INTER_AREA)

    img [ y : y + h, x : x + w] = face_img

cv2.imshow('face find', img)

cv2.waitKey(0)

cv2.destroyAllWindows()