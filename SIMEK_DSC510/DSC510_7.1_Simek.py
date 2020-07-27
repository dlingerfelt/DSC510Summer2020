# Katie Simek
# 19/07/2020
# Create a program that inports a txt file, then calculate the total words, and output
# the number of occurrences of each word in the file.
# Create seprate print function to make modification changes easier


import string    # use to eliminate punctuation in file


def add_word(word, counts):
    counts[word] = counts.get(word, 0) + 1


def process_line(line, counts):
    line = line.rstrip()    # removes extra spaces
    line = line.lower()    # makes all words lowercase
    # makes a list of all words, removes punctuation
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()    # splits words in file
    for word in words:    # adds words to dictionary
        add_word(word, counts)


def pretty_print(counts):
    print('-' * 20)
    print('{:^20}'.format('Word  :  Count'))
    # sorts by value, then for same value sorts key alpha
    for [key, value] in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print('{:13} {:>3}'.format(key, value))


def main():
    counts = dict()
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, counts)
    print('Length of the dictionary: ', len(counts))
    pretty_print(counts)


main()
