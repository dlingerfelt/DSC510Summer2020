#DSC 510

#Week 8

#Programming Assignment Week 8

#Author Tiffany Tesoro

#07/26/2020

#TO HELP REMOVE PUNCTUATION
import string

#IMPORT OS LIBRARY
import os
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

#DEFINE PROCESS_FILE FUNCTION
def process_file(file_dictionary, fname, title=''):
    #ASK USER IF WOULD LIKE TO PRINT RESULTS IN FILE BY OVERWRITING
    overwrite_fname = input('Would you like to print results in an existing file? Type YES (will overwrite a file) or NO (will print results on screen) then press enter: ')
    print()
    #YES TO OVERWRITE WITH WORD COUNT RESULTS
    if overwrite_fname == 'YES':
        fname_overwrite = input('Type the file name to be overwritten and press enter: ')
        print()
    #NO TO NOT OVERWRITE WORD COUNT RESULTS - RESULTS WILL ONLY BE PRINTED ON SCREEN
    elif overwrite_fname == 'NO':
        # CALL PRETTY_PRINT TO PRINT THE DICTIONARY
        pretty_print(file_dictionary)
        exit()
    #IF YES OR NO NOT ENTERED
    else:
        print('Please try again.')
        exit()
    #VALIDATE FILE EXISTS
    if os.path.isfile('gba_count.txt'):
        print("File being overwritten with word count results...")
        print()
    else:
        print("File does not exist.")
        exit()
    #WRITE TO FILE
    with open('gba_count.txt', 'w') as fileHandle: # w for writing
        #COUNT HEADER
        fileHandle.write('Length of the dictionary: ' + str(len(file_dictionary)) + '\n ')
        fileHandle.write('Word               Count \n')
        fileHandle.write('------------------------------\n')
        #FORMATTING COUNT
        for key in sorted(file_dictionary, key=file_dictionary.get, reverse=True):
            fileHandle.write('{:15} {:5} \n'.format(key, file_dictionary[key]))

#DEFINE MAIN FUNCTION
def main():
    #USER INPUT FILE NAME
    print('This program counts the number of words found in a text file and the results will be printed in an existing file. The file can then be opened for reading.')
    fname = input('Type the file name to be processed and press enter: ')
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
    #CLOSE FILE
    gba_file.close()
    # CALL PROCESS_FILE TO WRITE TO FILE
    process_file(file_dictionary, fname, title='')
    #ASK TO PREVIEW OR EXIT TO CLOSE
    preview = input('Type YES to preview overwritten file or NO to exit: ')
    if preview == 'YES':
        # OPEN FILE
        print()
        fcount = open('gba_count.txt', 'r')
        print(fcount.read())
    else:
        print('Program ending.')
        exit()

#CALL TO MAIN FUNCTION
if __name__ == '__main__':
    main()