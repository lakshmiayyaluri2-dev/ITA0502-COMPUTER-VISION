import cv2

# Read the image
img = cv2.imread("image.png")

# Check image
if img is None:
    print("Image not found!")
else:
    print("Image loaded successfully!")

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # Display original image
    cv2.imshow("Original Image", img)

    # Display blurred image
    cv2.imshow("Gaussian Blur", blur)

    # Wait for key
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
