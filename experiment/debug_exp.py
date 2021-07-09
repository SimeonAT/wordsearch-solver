import cv2
import pytesseract
""" This file contains all of the debugging functions used by all of the
    other Python source files. """

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


def check_words(words_to_find, found_words):
    """ Debugging function that prints out the words that have not yet been
        found by the word search algorithm """
    words_to_find = set(words_to_find)
    found_words = set(found_words)

    # The set difference would give us all the words in words_to_find that 
    # are not in found_words
    # Got some help here: https://realpython.com/python-sets/
    # 
    not_found_words = words_to_find - found_words
    print(f"Not found words: {not_found_words}")
    print(f"Number of words to find: {len(words_to_find)}")
    print(f"Number of words found: {len(found_words)}")
    return
