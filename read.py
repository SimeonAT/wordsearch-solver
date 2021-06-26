import cv2
import pytesseract
import sys

def display_image(image):
    """ Debugging function that uses OpenCV to display
        a given image until any key has been pressed.

        I learned that cv2.waitKey() function closed when a key has been
        pressed from the following link:
        https://docs.opencv.org/3.4/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
    """
    cv2.imshow("Debugging Image", image)
    cv2.waitKey(0)
    return


def bounding_boxes(image, config):
    """ Debugging function that displays the bounding boxes
        of each detected character in the given OpenCV image.

        Parameter(s):
            OpenCV image object
            the Pytesseract configuration string

        Returns:
            None; displays the image with the bounding boxes
            of the detected characters. """
    img_height, img_width, channels = image.shape
    boxes = pytesseract.image_to_boxes(image, config=config)

    print(boxes)
    for box in boxes.splitlines():
        char, x, y, width, height, _ = box.split(" ")

        # The bounding box coordinates are in a different format that I couldn't
        # fully figure out. As a result, I used the code for the top left and bottom
        # coordinates in the video https://www.youtube.com/watch?v=6DjFscX4I_c to build
        # the bounding boxes.
        # 
        top_left = (int(x), int(img_height) - int(y))
        bottom_right = (int(width), int (img_height) - int(height))

        cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
        cv2.circle(image, top_left, 3, (0, 0, 255), -1)
        cv2.circle(image, bottom_right, 3, (0, 255, 0), -1)

    cv2.imshow("Bounding Boxes Debug", image)
    cv2.waitKey(0)
    return


def print_word_search(word_search):
    """ Debugging function that prints the contents of the word
        search matrix in a row major format. """
    for line in word_search:
        for letter in line:
            print(letter, end = " ")
        print()
    return


def print_words(list_of_words):
    """ Debugging function that prints the list of words
        to find in the word search. """
    for word in list_of_words:
        print(word)
    return


def read_words(file_loc):
    """ Reads in the list of words to find in the word
        search from a file.

        Parameter(s):
            The file location of the list of words

        Returns:
            The list of words to find in the word search """
    with open(file_loc, "r") as word_file:
        list_of_words = word_file.readlines()

        # - Remove the '\n' character from each word 
        # - Make each letter is lowercase for easy comparision with the word search
        # - Remove all " " characters in string, as they won't be apart of the word in 
        #   the wordsearch; Got some help here:
        #   https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
        for i in range(0, len(list_of_words)):
            list_of_words[i] = list_of_words[i].strip("\n").strip().lower().replace(" ", "")

        return list_of_words


def read_word_search(file_loc, tesseract_location, training_data):
    """ This function utilizes Tesseract to read in a word search and
        stores it as a 2D array.

        Parameter(s):
            the file location of the image.
            the file location of the Tesseract executable
            the Tesseract training data folder to utilize.

        Returns:
            a 2D matrix representation of the word search. """

    pytesseract.pytesseract.tesseract_cmd = tesseract_location

    # You need the ABSOLUTE PATH of tessdata for the "tessdata-dir" parameter
    config = r"--tessdata-dir /home/simeon/wordsearch-solver/" + training_data \
            + " --oem 3 --psm 6 load_system_dawg=false load_freq_dawg=false"

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


def read_from_file(file_loc, rows, columns):
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
    word_search = read_word_search(sys.argv[1], sys.argv[2], sys.argv[3])
    # word_search = read_from_file(sys.argv[1], sys.argv[2], sys.argv[3])
    print_word_search(word_search)
