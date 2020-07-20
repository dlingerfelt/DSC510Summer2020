# DSC 510
# Week 8
# Programming Assignment Week 8
# Author: Michael Hotaling
# 07/20/2020

import string
import os
import webbrowser


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


def process_file(word_dictionary, output_filename, title=""):
    output = open(output_filename, "w")
    # output.write("Length of the dictionary: " + str(len(word_dictionary) + "\n"))
    output.write("{:^35}\n".format(title + ": " + str(len(word_dictionary)) + " unique words"))
    output.write("{:-^35}\n".format("-"))
    output.write("| {:>5} | {:<15}|{:>7} |\n".format("Index", "Word", "Count"))
    output.write("{:-^35}\n".format("-"))
    index = 1
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        output.write("| {:>5} | {:<15}|{:>7} |\n".format(index, key, word_dictionary[key]))
        index += 1
    output.write("{:-^35}\n".format("-"))


def csv_process_file(word_dictionary, output_filename, title=""):
    output = open(output_filename, "w")
    # output.write("Length of the dictionary: " + str(len(word_dictionary) + "\n"))
    output.write("{:^35}\n".format(title + ": " + str(len(word_dictionary)) + " unique words"))
    output.write("{},{},{}\n".format("Index", "Word", "Count"))
    index = 1
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        output.write("{},{},{}\n".format(index, key, word_dictionary[key]))
        index += 1


def main():
    path = os.getcwd()
    file = "gettysburg.txt"
    # file = input("What is the file name?: ")
    gba_file = open(file, 'r')
    output_filename = input("Enter the output file name: ")
    word_dictionary = dict()
    for line in gba_file:
        process_line(line, word_dictionary)
    gba_file.close()
    format_finder = output_filename.split(".")
    
    # This block could probably be optimized
    if output_filename[-4:] == ".csv":
        print("Exporting file as {0}".format(format_finder[len(format_finder)-1]))
        csv_process_file(word_dictionary, output_filename, title=file)
    elif "." in output_filename:
        print("Exporting file as {0}".format(format_finder[len(format_finder)-1]))
        process_file(word_dictionary, output_filename, title=file)
    else:
        print("No file format selected. Defaulting to txt")
        output_filename = output_filename+".txt"
        process_file(word_dictionary, output_filename, title=file)
        
    print("{0} exported to {1}".format(output_filename, path))
    if input("Would you like to open the file now? [y/n]: ").lower() == "y":
        webbrowser.open(output_filename)


if __name__ == "__main__":
    main()
