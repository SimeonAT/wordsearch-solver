# **SOURCES**
*	https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html

# **PLAN**
*	Use OpenCV threshold functions to turn any screenshot of a word search into a purely black
	and white image, where the letters are black and everything else is white.
*	Use OpenCV to get create subimages/bounding boxes for each individual letter in the
	word search.
*	Use PyTesseract to read each letter individually. My hope is that PyTesseract will be
	more accurate in reading the letters individually, rather than reading the whole
	word search at once.
