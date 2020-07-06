# DSC 510
# Week 8
# Programming Assignment Week 8
# Author: Michael Hotaling
# 07/06/2020

import string


def add_words(words, word_dictionary):
    # We can use an iterative function to add each word to the library
    # If the word doesn't yet exist in the library, we can set the value equal to 1
    for word in words:
        if word != "":
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1


def process_line(line, word_dictionary):
    # We will first call strip to remove the leading and trailing spaces in the string
    line = line.strip()
    # Next, we convert all the characters to lower case.
    line = line.lower()
    # This ia bit more complicated. We need to remove special characters from our input.
    # We can use translate to covert the special characters to spaces
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Finally, we can split all the words in each line using spaces as the delimiter
    words = line.split(" ")
    # We can then call the process_add_words function to add the words to the dictionary
    add_words(words, word_dictionary)


def process_file(word_dictionary, output_filename):
    output = open(output_filename, "w")
    # output.write("Length of the dictionary: " + str(len(word_dictionary) + "\n"))
    output.write("-" * 34 + "\n")
    output.write("|{:<25} {:5} |".format("Word", "Count") + "\n")
    output.write("|" + ("-" * 32) + "|" + "\n")
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        output.write("|{:<15} {:15} |".format(key, word_dictionary[key]) + "\n")
    output.write("-" * 34 + "\n")
    output.close()


def main():
    gba_file = open('gettysburg.txt', 'r')
    output_filename = input("Enter the output file name: ")
    word_dictionary = dict()
    for line in gba_file:
        process_line(line, word_dictionary)
    gba_file.close()
    output = open(output_filename, "w")
    process_file(word_dictionary, output_filename)


if __name__ == "__main__":
    main()
