
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    roi = img[50:250, 50:250]
    copied = img.copy()

    h, w = roi.shape[:2]
    copied[0:h, 0:w] = roi

    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Copied and Pasted ROI", copied)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or not found")
