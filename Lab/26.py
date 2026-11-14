import cv2
from tkinter import Tk, filedialog

# Select video
root = Tk()
root.withdraw()

print("Select a video")
path = filedialog.askopenfilename(
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Video not found!")
else:
    frames = []

    # Read all frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Reverse frames
    frames.reverse()

    # Get video properties
    height, width, _ = frames[0].shape
    fps = 25

    # Save reversed video
    out = cv2.VideoWriter(
        "reverse_video.mp4",
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    for frame in frames:
        out.write(frame)

    out.release()

    print("Reverse video created successfully!")

    # Play reversed video
    cap = cv2.VideoCapture("reverse_video.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Reverse Video", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
