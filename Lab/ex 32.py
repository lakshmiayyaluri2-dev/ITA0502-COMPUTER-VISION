import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

img = np.ones((height, width, 3), dtype=np.uint8) * 255

w = width // 10
h = height // 10

# Four colored boxes
cv2.rectangle(img, (0, 0), (w, h), (0, 0, 0), -1)
cv2.rectangle(img, (width-w, 0), (width-1, h), (255, 0, 0), -1)
cv2.rectangle(img, (0, height-h), (w, height-1), (0, 255, 0), -1)
cv2.rectangle(img, (width-w, height-h),
              (width-1, height-1), (0, 0, 255), -1)

cv2.imshow("Four Colored Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
