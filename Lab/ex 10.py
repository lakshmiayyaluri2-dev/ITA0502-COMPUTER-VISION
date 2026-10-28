import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated 90 Degrees", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or not found")
