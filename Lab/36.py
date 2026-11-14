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

    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    result = img.copy()
    result[mask > 0] = [255, 255, 255]

    cv2.imshow("Original Image", img)
    cv2.imshow("Background Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
