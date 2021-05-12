import cv2

print("CV Package imported")

img = cv2.imread("Resources/test_image.png")
cv2.imshow("Output", img)
cv2.waitKey(0)