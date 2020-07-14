# DSC 510
# Week 7
# Programming Assignment Week 7
# Author: Michael Hotaling
# 07/13/2020

import string
import matplotlib.pyplot as plt


def add_words(words, word_dictionary):
    # We can use an iterative function to add each word to the library
    # If the word doesn't yet exist in the library, we can set the value equal to 1
    for word in words:
        if word != "":  # I need this because there are some empty lines that aren't parsed correctly and return ""
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
    # We can use translate to convert the special characters to spaces
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Finally, we can split all the words in each line using spaces as the delimiter
    words = line.split(" ")
    # We can then call the add_words function to add the words to the dictionary
    add_words(words, word_dictionary)


def pretty_print(word_dictionary, title=""):
    print()
    print("{:^34}".format(title + ": " + str(len(word_dictionary)) + " unique words"))
    print("-" * 34)
    print("| {:>5}| {:<15}|{:>7} |".format("Index", "Word", "Count"))
    print("-" * 34)
    index = 1
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        print("| {:>5}| {:<15}|{:>7} |".format(index, key, word_dictionary[key]))
        index += 1
    print("-" * 34)


def word_plotter(word_dictionary, title="", show_grids=True):
    # https://stackoverflow.com/questions/37266341/plotting-a-python-dict-in-order-of-key-values/37266356
    # I'd rather use MSPaint than use matplotlib :'(
    # This is so unintuitive
    lists = sorted(word_dictionary.items(), key=lambda kv: kv[1], reverse=True)
    x, y = zip(*lists)
    plt.bar(x, y)
    plt.title(title)
    plt.xticks(fontsize=8, rotation=90)
    plt.grid(b=show_grids)
    plt.show()


def main():
    # Added a separate variable assignment to test other txt files
    file = "gettysburg.txt"
    # file = input("What is the file name?: ")
    text_file = open(file, 'r')
    word_dictionary = dict()
    for line in text_file:
        process_line(line, word_dictionary)
    text_file.close()
    pretty_print(word_dictionary, title=file)
    word_plotter(word_dictionary, title=file, show_grids=True)


if __name__ == "__main__":
    main()
