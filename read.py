import cv2
import pytesseract
import sys


def print_word_search(word_search):
    """ Debugging function that prints the contents of the word
        search matrix in a row major format. """
    for line in word_search:
        print(line)

pytesseract.pytesseract.tesseract_cmd = "tesseract"

# You need the ABSOLUTE PATH of tessdata for the "tessdata-dir" parameter
config = r"--tessdata-dir /home/simeon/wordsearch-solver/tessdata_old"

try:
    file_loc = sys.argv[1]
    word_search = cv2.imread(file_loc)
except:
    print("Please enter only 1 valid file location.\n")

# PyTesseract uses RGB, OpenCV uses BGR. Change BGR image read by OpenCV
# into an RGB image for Tesseract. 
word_search = cv2.cvtColor(word_search, cv2.COLOR_BGR2RGB)

# The word search will be represented as a 2D array
word_search_matrix = pytesseract.image_to_string(word_search, config=config).split()
for i in range(0, len(word_search_matrix)):
    word_search_matrix[i] = list(word_search_matrix[i])

print_word_search(word_search_matrix)
cv2.destroyAllWindows()
