# Katie Simek
# 26/07/2020
# Create a program that imports a txt file, then calculate the total words, and output
# the number of occurrences of each word in the file.
# Create separate print function to make modification changes easier
# Have program write to a user named file with just the length of the dictionary


import string    # use to eliminate punctuation in file


# Function to add words to dictionary called "counts"
# and count occurrences of each word
def add_word(word, counts):
    counts[word] = counts.get(word, 0) + 1


# Function to process the file lines, parsing the string to separate words
def process_line(line, counts):
    line = line.rstrip()    # removes extra spaces
    line = line.lower()    # makes all words lowercase
    # makes a list of all words, removes punctuation
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()    # splits words in the line
    for word in words:    # adds words to dictionary
        add_word(word, counts)


# Function to set print format for dictionary
def pretty_print(counts):
    print('-' * 20)
    print('{:^20}'.format('Word  :  Count'))
    # sorts by value, then for same value sorts key alpha
    for [key, value] in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print('{:13} {:>3}'.format(key, value))


# Function to open and read file.
# Get user input for name of new file to write to
# Write the length of the dictionary in the new file
def process_file(counts):
    # open file to create dict
    gba = 'gettysburg.txt'
    with open(gba, 'r') as gba_file:
        for line in gba_file:
            process_line(line, counts)
    # asks user for file name, creates new file and prints length of dict
    filename = input('What would you like to call the file?')
    with open(filename, 'w') as fileHandle:
        fileHandle.write('Length of the dictionary: ' + str(len(counts)))


# Creates empty dictionary, opens file to read and process line to add
# words to dictionary.
def main():
    counts = dict()
    gba = 'gettysburg.txt'
    with open(gba, 'r') as gba_file:
        for line in gba_file:
            process_line(line, counts)
    process_file(counts)  # gets file name, creates file and writes dict length
    pretty_print(counts)  # prints dictionary and counts in program


main()
