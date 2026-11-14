
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(
        img, cv2.MORPH_CLOSE, kernel
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Closing Image", closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or not found")
