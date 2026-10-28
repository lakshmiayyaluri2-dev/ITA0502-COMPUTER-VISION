
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    rows, cols = img.shape[:2]

    src = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    dst = np.float32([
        [cols * 0.1, rows * 0.1],
        [cols * 0.9, rows * 0.1],
        [cols * 0.2, rows * 0.9],
        [cols * 0.8, rows * 0.9]
    ])

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (cols, rows))

    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformation", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or not found")
