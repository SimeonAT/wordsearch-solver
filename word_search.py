""" Constant global variables to indicate which direction to navigate the word search. """
NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
NORTHWEST = 4
NORTHEAST = 5
SOUTHWEST = 6
SOUTHEAST = 7

# Debug flags that turns on debugging statements for the corresponding 
# function when set to 'True'
DEBUG_EVALUATE = False
DEBUG_WORD_SEARCH = False

def evaluate(word_search, word, direction, row, column):
    """ Helper function for find_words() that looks to see if
        the word in find is present starting at (row, column) and continuing
        in one of the cardinal directions.

        Parameters:
            the word search as a matrix
            the word to find
            the direction to look in using the format of the
                constant variables above
            the row and column of the letter of the word

        Returns:
            True if the word is at (row, column) and in the given direction,
            and False otherwise. """

    current_row, current_column = row, column

    # The dimensions of the word search
    WS_ROWS = len(word_search)
    WS_COLS = len(word_search[0])

    for i in range(0, len(word)):
        # Check if (current_row, current_column) is out of bounds. If so, return False.
        MAX_ROW = WS_ROWS - 1
        MAX_COL = WS_COLS - 1
        if (current_row < 0) or (current_row > MAX_ROW) or (current_column < 0) \
        or (current_column > MAX_COL):
                return False

        # Keep looping as long as the "ith" letter matches the letter at 
        # (current_row, current_column)
        if word[i] != word_search[current_row][current_column]:
            return False

        # Examining the next letter, depending on the direction we need to follow
        if direction == NORTH:
            current_row -= 1
        elif direction == SOUTH:
            current_row += 1
        elif direction == EAST:
            current_column += 1
        elif direction == WEST:
            current_column -= 1
        elif direction == NORTHWEST:
            current_row -= 1
            current_column -= 1
        elif direction == NORTHEAST:
            current_row -= 1
            current_column += 1
        elif direction == SOUTHWEST:
            current_row += 1
            current_column -= 1
        elif direction == SOUTHEAST:
            current_row += 1
            current_column += 1

        if DEBUG_EVALUATE:
            print("-" * 10)
            print(f"Currently looking at letter '{word_search[current_row][current_column]}'")
            print(f"Word to find: {word}")
            print(f"MAX_ROW: {MAX_ROW}")
            print(f"MAX_COL: {MAX_COL}")
            print(f"current_row: {current_row}")
            print(f"current_column: {current_column}")
            print(f"Direction: {direction}")
            print("-" * 10)

    return True


def find_words(word_search, list_of_words):
    """ This function contains the actual implementation of the
        word search program, looking for all the words in list_of_words
        in the word search.

        Parameters:
            the word search as a matrix
            the list of words to find

        Returns:
            A dictionary with all of the words in list_of_words as keys, with each
            key/value pair containing the following format:

            {word : ((x, y) coordinate of first letter, direction)}.

            Returns 'False' if the program fails to work. """
    found = {}

    for row in range(0, len(word_search)):
        for column in range(0, len(word_search[row])):
            for word in list_of_words:
                # If the word has already been found, skip it
                if word not in found.keys():
                    for direction in [NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST,
                                      SOUTHEAST, SOUTHWEST]:
                        evaluate_status = evaluate(word_search, word, direction, row, column)
                        if evaluate_status:
                            found[word] = ((row, column), direction)

                        if DEBUG_WORD_SEARCH:
                            print("-" * 10)
                            print("Currently looking at letter", end = " ")
                            print(f"'{word_search[row][column]}'")
                            print(f"Row {row}, Column {column}")
                            print(f"Looking for the word '{word}'")
                            print(f"Direction: {direction}")
                            print(f"Evaluate Status: {evaluate_status}")
                            print("-" * 10)

    return found
