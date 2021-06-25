NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

def evaluate(word_search, word, direction, row, column):
    """ Helper function for find_words() that looks to see if
        the word in find is present starting at (row, column) and continuing
        in the direction North, South, East, or West.

        Parameters:
            the word search as a matrix
            the word to find
            the direction to look in
              - NORTH = 1
              - SOUTH = 2
              - EAST = 3
              - WEST = 4
            the row and column of the letter of the word

        Returns:
            True if the word is at (row, column) and in the given direction,
            and False otherwise. """
    raise NotImplementedError


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
    return False
