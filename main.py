from read import *
from word_search import *
import sys

instructions = """ --- COMMAND LINE INSTRUCTIONS --- \n
Please note that the program uses PyTesseract to read a word search
from an image.

To read a word search from a text file:
    python3 main.py -f [file location] [rows] [columns] [list of words]

To read a word search from an image:
    python3 main.py -i [file location] [tesseract executable] [training data] [list of words]

"""

TEXT_FILE = "-f"
IMAGE = "-i"

def main(arguments):
    """ This function contains the actual implementation of the word search program,
        utilizing the functions from the other Python files in order to do so.

        Parameter:
            The list of command line arguments, excluding the filename. This means that
            the flag is at index 0 of the "arguments" list.

        Returns:
            A dictionary with all of the words in list_of_words as keys, with each
            key/value pair containing the following format:

            {word : ((x, y) coordinate of first letter, direction)}.

            Returns 'False' if the program fails to work. """

    word_search = None

    try:
        if arguments[0] == TEXT_FILE:
            word_search = read_from_file(arguments[1], int(arguments[2]), int(arguments[3]))
        elif arguments[0] == IMAGE:
            word_search = read_word_search(arguments[1], arguments[2], arguments[3])
    except Exception as error:
        # Resource Used: https://www.kite.com/python/answers/how-to-catch-and-print
        #                -exception-messages-in-python
        print(instructions)
        print(error)
        return False

    list_of_words = read_words(arguments[4])

    return find_words(word_search, list_of_words)


if __name__ == "__main__":
    # Create an array that has the command line arguments except for the filename,
    # and pass that into the word search algorithm function
    args = sys.argv[1:]
    locations = main(args)
    for key, value in locations.items():
        coordinates, direction = value

        # Find the actual direction using the integer/direction format used
        # in word_search.py
        direction_string = None
        mini_hash_table = ["NORTH", "SOUTH", "EAST", "WEST", "NORTHWEST",
                           "NORTHEAST", "SOUTHWEST", "SOUTHEAST"]
        direction_string = mini_hash_table[direction]

        print(f"The word '{key}' found at coordinate {coordinates}", end = " ")
        print(f"with direction {direction_string}")
