import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# coloring image
# img[:] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# write cv2.FILLED in place of thickness to fill rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 100), 70, (255, 255, 0), 2)
cv2.putText(img, " OPENCV ", (250, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
