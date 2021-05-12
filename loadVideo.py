import cv2

print("CV Package imported")


cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break