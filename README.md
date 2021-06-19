# **Word Search Solver Algorithm**

# **Sources Used**
*    https://www.youtube.com/watch?v=6DjFscX4I_c
*    https://realpython.com/python-command-line-arguments/
*	 https://github.com/tesseract-ocr/tessdata_best
*	 https://stackoverflow.com/questions/60066481/recognize-single-characters-on-a-page-with-tesseract


# **Description**
A program that can solve any word search puzzle. 



The word search will be a 2D array, with each letter in word search in one spot. 


## **Pseudocode for the "evaluate()" function**
```
def evaluate(grid, word, direction): 

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

            if letter == any first letter in

            words in words_to_find: 

                 evaluate(word in question,

                 position of letter, direction) 

            

            If evaluate() found the word: 

                 found.append((word,

                 location of first letter, direction)

       

    return found 
```
   
   
*    Use OpenCV to read an image of a word search and inputs to word_search() the 2D array representation of the word search 
*    Read one image of the words to find, read another image of the word search itself. 
*    Use output of word_search() to indicate where in the picture each of the words are. 
*    Create a computer and mobile application of this.

And BOOM, you just created your first app! 
