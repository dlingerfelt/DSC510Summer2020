# DSC 510
# Week 10
# Programming Assignment 10.1
# Author: Michael Hotaling
# 08/03/2020


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
        self.amount = payment_amount - (sum(self.total_price) + (sum(self.total_price) * self.sales_tax))
        return self.amount

    def printout(self):
        print("Receipt")
        date = datetime.datetime.now()
        print(str(date))
        print("=" * len("| {:<10} | {:<10}  | {:<12}  |".format("Quantity", "Price/Item", "Price")))
        print("| {:<40} |  \n| {:<10} | {:<10}  | {:<12}  |".format("Item", "Quantity", "Price/Item", "Price"))
        print("=" * len("| {:<10} | {:<10}  | {:<12}  |".format("Quantity", "Price/Item", "Price")))
        for i in range(0, len(self.thing)):
            print("| {:<40} |  \n| {:<10} | ${:<10,.2f} | ${:<12,.2f} |"
                  .format(self.thing[i], self.number[i], self.price[i], self.total_price[i]))
        print("=" * len("| {:<10} | {:<10}  | {:<12}  |".format("Quantity", "Price/Item", "Price")))

        # Gotta clean this disaster up :'(
        print(" Number of Items: {}\n "
              "Subtotal: ${:,.2f}\n "
              "Sales Tax: ${:,.2f}\n "
              "Total Price: ${:,.2f}"
              .format(sum(self.number),
                      sum(self.total_price),
                      sum(self.total_price) * self.sales_tax,
                      sum(self.total_price) + sum(self.total_price) * self.sales_tax))


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
            print(" Change: ${:,.2f}".format(register.payment(float(input(" Payment Amount: ")))))
            break


if __name__ == "__main__":
    main()
