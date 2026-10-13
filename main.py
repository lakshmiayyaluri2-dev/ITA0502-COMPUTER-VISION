

import cv2
from tkinter import Tk, filedialog
import os

# Select an image from your computer
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp"),
        ("All files", "*.*")
    ]
)

root.destroy()

# Check whether an image was selected
if not image_path:
    print("No image selected!")
else:
    # Read the image
    img = cv2.imread(image_path)

    if img is None:
        print("Unable to read the image!")
    else:
        print("Image loaded successfully!")

        # Display the original image
        cv2.imshow("Original Image", img)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Display the grayscale image
        cv2.imshow("Grayscale Image", gray)

        # Save the grayscale image in the same folder
        folder = os.path.dirname(image_path)
        output_path = os.path.join(folder, "gray_image.png")
        cv2.imwrite(output_path, gray)

        print("Grayscale image saved at:", output_path)

        # Wait for a key press and close windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
