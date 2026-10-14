
import cv2
import numpy as np
from tkinter import Tk, filedialog
import os

# Select an image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
)
root.destroy()

if not image_path:
    print("No image selected.")
else:
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not read image.")
    else:
        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Convert grayscale image to float32
        gray = np.float32(gray)

        # Apply Harris Corner Detection
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)

        # Dilate corner responses for better visibility
        dst = cv2.dilate(dst, None)

        # Mark detected corners in red
        result = img.copy()
        result[dst > 0.01 * dst.max()] = [0, 0, 255]

        # Display images
        cv2.imshow("Original Image", img)
        cv2.imshow("Harris Corner Detection", result)

        # Save output in the program folder
        folder = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(folder, "harris_corners.png")
        cv2.imwrite(output_path, result)

        print("Harris corner detection completed!")
        print("Saved as:", output_path)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
