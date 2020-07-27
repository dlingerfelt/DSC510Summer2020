# DSC 510
# Week 10
# Programming Assignment Week 10
# Author: Michael Hotaling
# 07/06/2020


import datetime

# This is definitely a stupid way to do this, but it'll work for now
# Let me see if I can add all this info to a dictionary instead. Maybe I can figure out how ot use 3 key values?


class CashRegister(object):
    def __init__(self):
        self.thing = []
        self.number = []
        self.price = []
        self.total_price = []
        self.amount = 0
        self.sales_tax = 0.08

    def add_item(self, item, quantity, value):
        self.thing.append(item)
        self.number.append(quantity)
        self.price.append(value)
        self.total_price.append(round(quantity * value, 2))
        '''
        Debugging
        print(self.thing)
        print(self.number)
        print(self.price)
        '''

    def sales_tax(self):
        return self.sales_tax

    def payment(self, payment_amount):
        self.amount = payment_amount - sum(self.total_price)
        return self.amount

    def printout(self):
        print("Receipt")
        date = datetime.datetime.now()
        print(str(date))
        print("--------")
        print("Item |  \n    Quantity | Price per Unit | Total Price")
        for i in range(0, len(self.thing)):
            print(str(self.thing[i]) + "  \n    " + str(self.number[i]) + " | " + str(self.price[i]) + " | " + str(
                self.total_price[i]))
        print()

        # Gotta clean this disaster up :'(
        print(" Number of items: " + str(int(sum(self.number))) + "\n Sub Total: " + str(sum(self.total_price)) + "\n "
            "Sales Tax: " + str(sum(self.total_price) * self.sales_tax) + "\n Total Price: " + str(sum(self.total_price)
            + (sum(self.total_price) * self.sales_tax)))


def main():
    register = CashRegister()
    while True:
        item = input("Item: ")
        quantity = float(input("Quantity: "))  # Changed this to float since some things are measured by weight
        value = float(input("Value: "))
        register.add_item(item, quantity, value)
        keep_going = input("Keep going?: ")
        if keep_going == "n":
            print()
            register.printout()
            print(" Change: " + str(register.payment(float(input(" Payment Amount: ")))))
            break


if __name__ == "__main__":
    main()