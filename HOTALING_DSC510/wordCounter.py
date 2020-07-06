# DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Michael Hotaling
# 07/06/2020

import string
import re

def process_add_words(words, word_dictionary):
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1


def process_line(line, word_dictionary):
    line = line.strip()
    line = line.lower()
    line = line.translate((line.maketrans("", "", string.punctuation)))
    words = line.split(" ")
    process_add_words(words, word_dictionary)


def format_print(word_dictionary):
    print()
    print("The number of words in the dictionary is " + str(len(word_dictionary)))
    print()
    print("{:<25} {:10} ".format("Word", " Count"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        if key.strip() != "": # Need this statement or we get spaces back. (not sure why)
            print("{:<15} {:15} ".format(key, word_dictionary[key]))


def main():
    gba_file = open('gettysburg.txt', 'r')
    word_dictionary = dict()
    for line in gba_file:
        process_line(line, word_dictionary)
    gba_file.close()
    format_print(word_dictionary)


if __name__ == "__main__":
    main()
