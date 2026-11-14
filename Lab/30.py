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

    smile = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_smile.xml"
    )

    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]

        smiles = smile.detectMultiScale(
            roi, 1.7, 20
        )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(img, (x+sx, y+sy),
                          (x+sx+sw, y+sy+sh),
                          (0, 255, 0), 2)

    print("Smile detection completed!")
    cv2.imshow("Smile Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
