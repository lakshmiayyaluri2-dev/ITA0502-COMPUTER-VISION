
import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[("Video files", "*.mp4 *.avi *.mov")]
)
root.destroy()

if video_path:
    for mode, delay, skip in [
        ("Normal Speed", 25, False),
        ("Slow Motion", 60, False),
        ("Fast Motion", 25, True)
    ]:
        cap = cv2.VideoCapture(video_path)
        print("Playing:", mode)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow(mode, frame)

            if cv2.waitKey(delay) & 0xFF == ord("q"):
                break

            if skip:
                cap.grab()

        cap.release()
        cv2.destroyAllWindows()
else:
    print("No video selected.")
