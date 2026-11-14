import cv2
from tkinter import Tk, filedialog
import numpy as np

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 40, 40])
    upper = np.array([20, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original Image", img)
    cv2.imshow("Foreground", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
