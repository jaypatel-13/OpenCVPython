import cv2

print("CV Package imported")

"""
Reading and showing an image using OpenCV

img = cv2.imread("Resources/lenna.png")
cv2.imshow("Output", img)
cv2.waitKey(0)


Create an object to read and show a video

cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


Use web cam

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
"""