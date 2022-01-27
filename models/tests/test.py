import sys
import os
  
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)


import random

from model import is_unique, save_data_if_unique, retrieve_data, retrieve_messages


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def test_retrieve_messages():
	"""The output should list of strings"""
	data = retrieve_messages()
	if type(data) == type(list()) and len(data) > 0:
		print("retrieve_messages is Successful")
	else:
		print("ERROR in retrieve_messages")


def test_is_unique():
	"""If the input_data = hello, then output should be False"""
	input_data = 'hello'
	if is_unique(input_data):
		print("ERROR in is_unique")
	else:
		print("is_unique is Successful")


def test_save_data_if_unique(l_words):
	data = random.choice(l_words)
	resp = save_data_if_unique(data)
	if resp == "success":
		print("save_data_if_unique is Successful")	
	else:
		print("ERROR in save_data_if_unique")

def test_save_data_if_unique_2():
	data = 'hello'
	resp = save_data_if_unique(data)
	if resp == "success":
		print("ERROR in save_data_if_unique_2")
	elif resp == "duplicate":
		print("save_data_if_unique_2 is Successful")	


if __name__ == '__main__':
	l_words = load_words()

	# Runing the tests
	print("RUNNING THE TESTS")
	print('#################################################')
	test_retrieve_messages()
	print('#################################################')
	test_is_unique()
	print('#################################################')
	test_save_data_if_unique(l_words)
	print('#################################################')
	test_save_data_if_unique_2()
	print('#################################################')
