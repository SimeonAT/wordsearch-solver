#!/bin/bash
# Bash Script that runs all of the word search test cases.
# I used the same sources mentioned in createTests.sh.

for i in 1 2 3 4 5 6 7
do
	echo " --- Test Case $i --- "
	python3 main.py ./tests/test${i}/test${i}.txt ./tests/test${i}/test${i}words.txt
	echo " --- Done Test Case $i --- "
done
