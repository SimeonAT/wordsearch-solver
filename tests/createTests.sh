#!/bin/bash
# Bash Script to create the files for each test case. 
# Sources used:
# - https://linuxhint.com/bash-variable-name-rules-legal-illegal/
# - https://www.cyberciti.biz/faq/bash-for-loop/
# - https://bash.cyberciti.biz/guide/Shell_Comments
# 
for i in 1 2 3 4 5 6 7 8 9 10
do
	mkdir test$i
	cd test$i
	touch test${i}.txt
	touch test${i}words.txt
	rm -f test.txt
	cd $OLDPWD
done
echo "Finish creating files for test cases."
	
