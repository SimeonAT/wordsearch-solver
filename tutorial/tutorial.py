import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
img = cv2.imread("test.png")

# PyTesseract using RGB values, but OpenCV using BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detecting Characters
"""
heightImg, widthImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for box in boxes.splitlines():
    box = box.split(" ")
    x, y, width, height = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, heightImg - y), (width, heightImg - height), (0, 0, 255), 1)
    cv2.putText(img, box[0], (x, heightImg - y + 25), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
"""

# Detecting Words
"""
heightImg, widthImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
print(boxes)
for count, box in enumerate(boxes.splitlines()):
    if count != 0:
        box = box.split()
        print(box)
        if len(box) == 12:
            x, y, width, height = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (width + x, height + y), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
"""

heightImg, widthImg, _ = img.shape
config = r" --oem 3 --psm 6 outputbase digits"
boxes = pytesseract.image_to_boxes(img, config=config)
for box in boxes.splitlines():
    box = box.split(" ")
    x, y, width, height = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, heightImg - y), (width, heightImg - height), (0, 0, 255), 1)
    cv2.putText(img, box[0], (x, heightImg - y + 25), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
