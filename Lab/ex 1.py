import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()

img = cv2.imread(path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Image", img)
    cv2.imshow("Gray Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or not found")
