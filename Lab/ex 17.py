
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename()
img = cv2.imread(path)

if img is not None:
    result = img.copy()

    text = "MY WATERMARK"
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    thickness = 2

    h, w = result.shape[:2]

    size = cv2.getTextSize(
        text, font, scale, thickness
    )[0]

    x = max(10, w - size[0] - 20)
    y = max(size[1] + 10, h - 20)

    cv2.putText(
        result, text, (x, y), font, scale,
        (255, 255, 255), thickness, cv2.LINE_AA
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", result)

    cv2.imwrite("watermarked_image.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Watermarked image saved successfully")
else:
    print("Image not selected or not found")
