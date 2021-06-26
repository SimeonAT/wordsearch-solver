# **Word Search Solver Algorithm**

# **Description**
A program that can solve any word search puzzle. 



The word search will be a 2D array, with each letter in word search in one spot. 

*    Use OpenCV to read an image of a word search and inputs to word_search() the 2D array representation of the word search 
*    Read one image of the words to find, read another image of the word search itself. 
*    Use output of word_search() to indicate where in the picture each of the words are. 
*    Create a computer and mobile application of this.

And BOOM, you just created your first app! 


# **Improvements to Make Later On**

*	For now, give the user two options: to scan an image of the word search, or to manually 
	enter each letter of the word search onto the terminal. Once you have a basic application working, 
	go back and figure out how to improve PyTesseract in regards to reading a word search.

## **Pseudocode for the "evaluate()" function**
```
def evaluate(grid, word, direction, row, column): 
    Start at location of first letter in word

    for letter in grid at direction: 
         if nth letter matches nth word in word
              continue
         else: 
              return False
              
    return True 
```

## **Pseudocode for the "word_search()" function**
```
def word_search(grid, words_to_find):
    found = [ ] 
    
    for row in grid: 
        for letter in row: 
            if letter == any first letter in words in words_to_find: 
                 evaluate(word in question, position of letter, direction)        

            If evaluate() found the word: 
                 found.append(word, location of first letter, direction)
                 
    return found 
    
```

# **Sources Used**
*    https://www.youtube.com/watch?v=6DjFscX4I_c
*    https://realpython.com/python-command-line-arguments/
*	 https://github.com/tesseract-ocr/tessdata_best
*	 https://stackoverflow.com/questions/60066481/recognize-single-characters-on-a-page-with-tesseract
*	 https://stackoverflow.com/questions/60009533/drawing-bounding-boxes-with-pytesseract-opencv
*	 https://docs.opencv.org/4.5.2/da/d6e/tutorial_py_geometric_transformations.html
* 	 https://www.kite.com/python/answers/how-to-catch-and-print-exception-messages-in-python
*    https://stackoverflow.com/questions/51143458/difference-in-output-with-waitkey0-and-waitkey1/51143586
*    https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html
*    https://docs.opencv.org/4.5.2/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
*    https://docs.opencv.org/3.4/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
*	 https://book.pythontips.com/en/latest/context_managers.html
*    https://www.w3schools.com/python/ref_string_strip.asp
*	 https://realpython.com/python-debugging-pdb/
*	 https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
*	 https://realpython.com/python-sets/
