import cv2
import pytesseract
from sys import argv
from debug import *

# --- COMMAND LINE FORMAT --- 
# python3 read_exp.py [file loc] [tesseract exec] [training data] [output filename] [config file]

def read_from_image(file_loc, tesseract_location, training_data, config_file):
    pytesseract.pytesseract.tesseract_cmd = tesseract_location

    config = r"--tessdata-dir /home/simeon/wordsearch-solver/" + training_data \
            + " --oem 3 --psm 6 CONFIG_FILE " + config_file

    word_search = cv2.imread(file_loc)
    word_search = cv2.cvtColor(word_search, cv2.COLOR_BGR2RGB)

    for i in range(0, len(word_search_matrix)):
        word_search_matrix[i] = list(word_search_matrix[i].lower())

    return word_search_matrix


if __name__ == "__main__":
    word_search = read_from_image(argv[1], argv[2], argv[3], argv[5])
    with open(argv[4], "w") as output_file:
        for row in word_search:
            for letter in row:
                output_file.write(letter)
            output_file.write("\n")

