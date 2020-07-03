'''
Hello, and welcome to my week 7 programming assignment

Dictionaries, Tuples, JSON Data

DSC 510

Programming Assignment Week 7

Author: Brett Foster

July 3, 2020
'''
print('Thanks for visiting my speech breakdown program!' + '\n')
word_dict = {}

def main():
    filepath = 'gettysburg.txt'
    with open(filepath, 'r') as fs:
        lines = fs.read()
        speech_list = lines.lower().split()
        for word in speech_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    
    word_dict_values = sorted(word_dict, key=word_dict.get, reverse=True)

    equals = '=' * 25
    dash = '-' * 25
    print("Length of the dictionary: " + str(len(word_dict)))
    print(equals)
    print('{:<16} {:<20}'.format('WORD', 'COUNT'))
    print(dash)
    for item in word_dict_values:
        if word_dict[item] > 3:
            print('{:<18} {:<20}'.format(item, word_dict[item]))
        else:
            continue
    


if __name__ == '__main__':
    main()
