
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("Original Image", img)
    cv2.imshow("Erosion Image", erosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or not found")
