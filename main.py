from read import *
import sys

instructions = """ --- COMMAND LINE INSTRUCTIONS --- \n
Please note that the program uses PyTesseract to read a word search
from an image.

To read a word search from a text file:
    python3 main.py -f [file location] [rows] [columns]

To read a word search from an image:
    python3 main.py -i [file location] [tesseract executable] [training data]
"""

TEXT_FILE = "-f"
IMAGE = "-i"

if __name__ == "__main__":
    word_search = None
    print(sys.argv)

    try:
        if sys.argv[1] == TEXT_FILE:
            word_search = read_from_file(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
        elif sys.argv[1] == IMAGE:
            word_search = read_word_search(sys.argv[2], sys.argv[3], sys.argv[4])
    except Exception as error:
        # Resource Used: https://www.kite.com/python/answers/how-to-catch-and-print
        #                -exception-messages-in-python
        print(instructions)
        print(error)

    print(word_search)
