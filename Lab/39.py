import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Videos", "*.mp4 *.avi *.mov")]
)

cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Video not found!")
else:
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Reverse the frames
    frames.reverse()

    print("Playing video in reverse slow motion")

    for frame in frames:
        cv2.imshow("Reverse Slow Motion", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
