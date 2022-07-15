import cv2  # Read image / camera/video input
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 -Width
cap.set(4, 480)  # 4 -Height
camera = True
while camera:
    success, frame = cap.read()

    for code in decode(frame):
        qr_id = code.data.decode('utf-8')
        print(qr_id)
        exit()

    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)
