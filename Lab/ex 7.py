
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
path = askopenfilename(
    filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
)

cap = cv2.VideoCapture(path)

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30

    print("Press 1 for Normal Video")
    print("Press 2 for Slow Motion")
    print("Press 3 for Fast Motion")
    choice = input("Enter your choice: ")

    if choice == "1":
        delay = int(1000 / fps)
        title = "Normal Video"
        step = 1
    elif choice == "2":
        delay = int(2000 / fps)
        title = "Slow Motion"
        step = 1
    elif choice == "3":
        delay = int(500 / fps)
        title = "Fast Motion"
        step = 2
    else:
        print("Invalid choice")
        cap.release()
        raise SystemExit

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow(title, frame)

        if cv2.waitKey(max(1, delay)) & 0xFF == ord('q'):
            break

        if choice == "3":
            for _ in range(step - 1):
                cap.grab()

    cap.release()
    cv2.destroyAllWindows()

else:
    print("Video not selected or not found")
