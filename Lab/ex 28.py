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
    # Background subtraction
    bg = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Apply background subtraction
        mask = bg.apply(frame)

        # Find contours
        contours, hierarchy = cv2.findContours(
            mask, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Detect moving objects
        for c in contours:
            area = cv2.contourArea(c)

            if area > 1000:
                x, y, w, h = cv2.boundingRect(c)

                cv2.rectangle(
                    frame, (x, y),
                    (x+w, y+h), (0, 255, 0), 2
                )

                cv2.putText(
                    frame, "Vehicle",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2
                )

        # Display output
        cv2.imshow("Vehicle Detection", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
