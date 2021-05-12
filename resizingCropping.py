import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")

imgResize = cv2.resize(img, (400,300))
imgCropped = img[150:550, 50:650]

print(img.shape)
print(imgResize.shape)
print(imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)