
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    names = ["Blue", "Green", "Red"]

    hist_img = __import__("numpy").zeros((400, 512, 3), dtype="uint8")

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, 350, cv2.NORM_MINMAX)

        for x in range(1, 256):
            cv2.line(
                hist_img,
                (2 * (x - 1), 400 - int(hist[x - 1])),
                (2 * x, 400 - int(hist[x])),
                color, 2
            )

    cv2.imshow("Original Image", img)
    cv2.imshow("Color Histogram", hist_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
