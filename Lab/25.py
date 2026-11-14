import cv2
from tkinter import Tk, filedialog

# Select original image
root = Tk()
root.withdraw()

print("Select the image containing the watch")
img_path = filedialog.askopenfilename(
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Select watch reference image
print("Select the watch reference image")
watch_path = filedialog.askopenfilename(
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

img = cv2.imread(img_path)
template = cv2.imread(watch_path)

if img is None or template is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(
        gray, temp, cv2.TM_CCOEFF_NORMED
    )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    h, w = temp.shape

    if max_val > 0.7:
        cv2.rectangle(img, max_loc,
                      (max_loc[0] + w, max_loc[1] + h),
                      (0, 255, 0), 3)
        print("Watch detected!")
    else:
        print("Watch not detected!")

    cv2.imshow("Watch Recognition", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
