import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imshow("Original", img)
    cv2.imshow("Gaussian Blur", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
