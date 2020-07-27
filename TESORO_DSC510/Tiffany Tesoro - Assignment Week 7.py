#DSC 510

#Week 7

#Programming Assignment Week 7

#Author Tiffany Tesoro

#07/19/2020

#NOTE: ADDED EXTRA COMMENTS FOR REMINDER IN FUTURE USE

#TO HELP REMOVE PUNCTUATION
import string
print()

#DEFINE ADD_WORD FUNCTION
#ADD WORD TO DICTIONARY
#REFERENCE TEXTBOOK ADVANCED TEXT PARSING PG 114
def add_word(counts, file_dictionary):
    for word in counts:
        if word in file_dictionary:
            file_dictionary[word] += 1
        else:
            file_dictionary[word] = 1

#DEFINE PROCESS_LINE FUNCTION
#REMOVE PUNCTUATIONS AND SPACES
#LOWERCASE LETTERS SO PYTHON CAN COUNT PROPERLY
#REFERENCE TEXTBOOK ADVANCED TEXT PARSING PG 114
def process_line(line, file_dictionary):
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    counts = line.split()
    #CALL TO ADD_WORD FUNCTION
    add_word(counts, file_dictionary)

#DEFINE PRETTY_PRINT FUNCTION
def pretty_print(file_dictionary):
    #COUNT HEADER
    print('Length of the dictionary: ', len(file_dictionary))
    print('Word               Count')
    print('------------------------------')
    #FORMATTING COUNT
    #SORT REFERENCE https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    #PRINT REFERENCE https://www.dummies.com/programming/python/how-to-format-strings-in-python/
    for key in sorted(file_dictionary, key=file_dictionary.get, reverse=True):
        print('{:15} {:5}'.format(key, file_dictionary[key]))

#DEFINE MAIN FUNCTION
def main():
    #USER INPUT FILE NAME
    fname = input('Enter the file name and press enter: ')
    print()
    #OPEN CORRECTLY NAMED FILE
    if fname == 'gettysburg.txt':
        file_dictionary = dict()
        gba_file = open('gettysburg.txt', 'r')
    #IF INCORRECT FILE NAME
    else:
        print('File cannot be opened:', fname)
        exit()
    #CALL PROCESS_LINE ON EACH LINE
    for line in gba_file:
        process_line(line, file_dictionary)
    #CALL PRETTY_PRINT TO PRINT THE DICTIONARY
    pretty_print(file_dictionary)

#CALL TO MAIN FUNCTION
if __name__ == "__main__":
    main()