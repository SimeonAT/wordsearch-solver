import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "tesseract"

file_loc = input("Enter file location of word search: ")
word_search = cv2.imread(file_loc)

# PyTesseract uses RGB, OpenCV uses BGR. Change BGR image read by OpenCV
# into an RGB image for Tesseract. 
word_search = cv2.cvtColor(word_search, cv2.COLOR_BGR2RGB)

height, width, channels = word_search.shape
print(pytesseract.image_to_string(word_search))

cv2.destroyAllWindows()
