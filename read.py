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
        print(line)
    return


def read_word_search(file_loc, training_data):
    """ This function utilizes Tesseract to read in a word search and
        stores it as a 2D array.

        Parameter(s):
            the file location of the image.
            the Tesseract training data folder to utilize.

        Returns:
            a 2D matrix representation of the word search. """

    pytesseract.pytesseract.tesseract_cmd = "tesseract"

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
        word_search_matrix[i] = list(word_search_matrix[i])

    return word_search_matrix


if __name__ == "__main__":
    word_search = read_word_search(sys.argv[1], sys.argv[2])
    print_word_search(word_search)
