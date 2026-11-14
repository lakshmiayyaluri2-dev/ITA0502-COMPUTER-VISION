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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    eye = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_eye.xml"
    )

    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        eyes = eye.detectMultiScale(roi)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x+ex, y+ey),
                          (x+ex+ew, y+ey+eh),
                          (0, 255, 0), 2)

    print("Eye detection completed!")
    cv2.imshow("Eye Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
