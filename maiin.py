
import cv2
from tkinter import Tk, filedialog

# Select a video
root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[
        ("Video files", "*.mp4 *.avi *.mov *.mkv"),
        ("All files", "*.*")
    ]
)
root.destroy()


def play_video(path, mode):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        print("Unable to open video!")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0 or fps > 240:
        fps = 25

    delay = max(1, int(1000 / fps))

    if mode == "Slow Motion":
        delay = delay * 2

    print("Playing:", mode)
    frame_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # In fast motion, skip alternate frames
        if mode == "Fast Motion":
            frame_number += 1

            if frame_number % 2 == 0:
                continue

        cv2.imshow(mode, frame)

        # Press q to stop current playback
        if cv2.waitKey(delay) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if video_path:
    # Play at normal speed
    play_video(video_path, "Normal Speed")

    # Play in slow motion
    play_video(video_path, "Slow Motion")

    # Play in fast motion
    play_video(video_path, "Fast Motion")

    print("Video processing completed!")
else:
    print("No video selected!")
