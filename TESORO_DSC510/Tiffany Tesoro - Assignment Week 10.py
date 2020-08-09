#DSC 510

#Week 10

#Programming Assignment Week 10

#Author Tiffany Tesoro

#08/09/2020

#TO FORMAT TOTAL PRICE
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
#locale.setlocale(locale.LC_ALL, '') did not work for me
#REFERENCE https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting

#DEFINE CASHREGISTER CLASS
class CashRegister(object):
    #CASHREGISTER INSTANCE
    def __init__(self):
        self.itemCount = 0
        self.totalPrice = 0
    #ADDITEM INSTANCE METHOD
    def addItem(self, price):
        self.totalPrice += float(price)
        self.itemCount += 1
    #@property GETTOTAL GETTER METHOD
    #tried to use it based on Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters
    #TypeError: 'float' object is not callable when I include this in code
    def getTotal(self):
        return self.totalPrice
    #@property GETCOUNT GETTER METHOD
    def getCount(self):
        return self.itemCount

#TRIED TO MAKE A LIST TO PRINT THE PRICE OF EACH ITEM AT THE END BUT DID NOT WORK OUT
#BASED FUNCTION FROM WEEK 6 ASSIGNMENT
#def user_input(prices):
    #while True:
        #try:
            #input_price = input('Input price of item in and press enter: USD$ ')
            #price = input_price
            #prices.append(float(price))
        #except ValueError:
            #print('Please try again.')
            #print()

#DEFINE MAIN FUNCTION
def main():
    #WELCOME MESSAGE
    print()
    print('Welcome to the Bellevue Cash Register!')
    print()
    #CALL TO CASHREGISTER CLASS
    checkout = CashRegister()
    while True:
        addAnother = input('Would you like to add an item? Type YES or NO then press enter: ').upper()
        if addAnother == 'YES' or addAnother == 'Y':
                try:
                    price = float(input('Input price of item in and press enter: USD$ '))
                    #CALL TO ADDITEM METHOD
                    checkout.addItem(price)
                except ValueError:
                    print('Please try again.')
                    print()
                #ATTEMPT AT WHAT WOULD'VE BEEN IF LIST ACCEPTED
                #while True:
                    #prices = []
                    #print()
                    #prices = user_input(prices)
                    #print()
                    #HAD TROUBLE INCORPORATING CALL TO ADDITEM METHOD
                    #CashRegister.addItem(price)
                    #break
        elif addAnother == 'NO' or addAnother == 'N':
            print()
            #CALL TO GETTOTAL METHOD
            print('Transaction total: ' + locale.currency(checkout.getTotal()))
            #REFERENCE https://pymotw.com/3/locale/
            #CALL TO ITEMCOUNT METHOD
            print('Total number of items: ' + str(checkout.getCount()))
            print()
            print('Thank you for using Bellevue Grocery. Have a wonderful day!')
            exit()
        else:
            print('Please try again.')
            print()

#CALL TO MAIN FUNCTION
if __name__ == "__main__":
    main()