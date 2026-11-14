import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.png *.jpeg")]
)

img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    text = input("Enter text: ")

    cv2.putText(img, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    cv2.imshow("Text on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
