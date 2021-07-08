import cv2
import pytesseract
from sys import argv
from debug import *

error_message = """--- Command Line Format ---
python3 read.py [file loc] [tesseract exec] [training data] [output filename] [config file]\n"""

def read_from_image(file_loc, tesseract_location, training_data, config_file):
    """ This function utilizes Tesseract to read in a word search and
        stores it as a 2D array.

        Parameter(s):
            the file location of the image.
            the file location of the Tesseract executable
            the Tesseract training data folder to utilize.
            the Tesseract config file to use.

        Returns:
            a 2D matrix representation of the word search. """

    pytesseract.pytesseract.tesseract_cmd = tesseract_location

    # You need the ABSOLUTE PATH of tessdata for the "tessdata-dir" parameter.
    # 
    # Whitelisting only alphabetical letters in the config file helped make it so
    # Tesseract doesn't accidentally detect numbers in the word search (when they
    # should all be letters). 
    # 
    # Helpful links:
    # - https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html
    #   #dictionaries-word-lists-and-patterns
    # - https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
    # 
    config = r"--tessdata-dir /home/simeon/wordsearch-solver/" + training_data \
            + " --oem 3 --psm 6 CONFIG_FILE " + config_file

    word_search = cv2.imread(file_loc)

    # PyTesseract uses RGB, OpenCV uses BGR. Change BGR image read by OpenCV
    # into an RGB image for Tesseract. I learned about this insight from 
    # https://www.youtube.com/watch?v=6DjFscX4I_c.i
    # 
    word_search = cv2.cvtColor(word_search, cv2.COLOR_BGR2RGB)

    word_search_matrix = pytesseract.image_to_string(word_search, config=config).split()
    for i in range(0, len(word_search_matrix)):
        # NOTE: Make each letter in the word search lowercase so we can easily compare 
        # it with the list of words, where each word is all in lowercase letters.
        # 
        word_search_matrix[i] = list(word_search_matrix[i].lower())

    return word_search_matrix


def read_from_file(file_loc):
    """ This function reads a word search that is stored in a text file.
        Ideal for word searches that could have been read by PyTesseract.

        Parameter(s):
            the file location of the text file
            the number of rows and columns of the word search

        Returns:
            A 2D array representation of the word search

        Sources Used:
            https://book.pythontips.com/en/latest/context_managers.html
            https://www.w3schools.com/python/ref_string_strip.asp """

    with open(file_loc, "r") as word_search_file:
        word_search = word_search_file.readlines()

    # Convert each line into a list of letters
    for i in range(0, len(word_search)):
        # Remove the newlines gathered from readlines()
        word_search[i] = word_search[i].strip("\n")

        # 1. Remove the extra whitespace created by stripping '\n'
        # 2. Remove all whitespace between each letter by replacing whitespace
        #    with an empty string; Got some help from this link:
        #    https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
        # 3. Convert all letters to lowercase letters
        #
        word_search[i] = word_search[i].strip(" ").replace(" ", "")
        word_search[i] = list(word_search[i].lower())

    return word_search


if __name__ == "__main__":
    # Read word search image and place the text of the word search
    # into an external text file.
    # Command line format: 
    #   read.py [file loc] [tesseract exec] [training data] [output filename] [config file]
    try:
        word_search = read_from_image(argv[1], argv[2], argv[3], argv[5])
        with open(argv[4], "w") as output_file:
            for row in word_search:
                for letter in row:
                    output_file.write(letter)
                output_file.write("\n")
    except Exception as error:
        print(error_message)
        print(error)
