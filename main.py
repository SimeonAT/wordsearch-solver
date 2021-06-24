from read import *
import sys

instructions = """ --- COMMAND LINE INSTRUCTIONS ---

Please note that the program uses PyTesseract to read a word search
from an image.

To read a word search from a text file:
    python3 main.py [file location] [rows] [columns]

To read a word search from an image:
    python3 main.py [file location] [tesseract executable] [training data]
"""

print(instructions)
