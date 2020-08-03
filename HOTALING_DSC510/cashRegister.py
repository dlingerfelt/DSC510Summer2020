# DSC 510
# Week 10
# Programming Assignment 10.1
# Author: Michael Hotaling
# 08/03/2020


import datetime
import sys
import webbrowser
from money import Money

# This is definitely a stupid way to do this, but it'll work for now
# Let me see if I can add all this info to a dictionary instead. Maybe I can figure out how ot use 3 key values?


class CashRegister(object):
    def __init__(self):
        self.thing = []
        self.number = []
        self.price = []
        self.total_price = []
        self.amount = 0
        self.sales_tax = 0.0825

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
        self.amount = payment_amount - (sum(self.total_price) * (1 + self.sales_tax))
        return self.amount

    def printout(self):
        print("=" * len("| {:<10} | {:>11} | {:>12}  |".format("Quantity", "Price/Item", "Price")))
        print("|{:^42}|".format("Receipt"))
        print("|{:^42}|".format(datetime.datetime.now().strftime("%m/%d/%Y")))
        print("|{:^42}|".format(datetime.datetime.now().strftime("%I:%M:%S%p")))
        print("=" * len("| {1:<10} | {0:<11} | {2:<12}  |".format("Quantity", "Price/Item", "Price")))
        print("| {0:<40} |  \n| {2:<10} | {1:>11} | {3:>12}  |".format("Item", "Quantity", "Price/Item", "Price"))
        print("=" * len("| {1:<10} | {0:<11} | {2:<12}  |".format("Quantity", "Price/Item", "Price")))
        for i in range(0, len(self.thing)):
            print("| {0:<40} |  \n| {2:<10} | {1:>11} | {3:>13} |"
                  .format(self.thing[i],
                          self.number[i],
                          Money(self.price[i], "USD").format("en_US"),
                          Money(self.total_price[i], "USD").format("en_US")))
        print("=" * len("| {1:<10} | {0:>11} | {2:>12}  |".format("Quantity", "Price/Item", "Price")))

        # Gotta clean this disaster up :'(
        print("| {1:<20}{5:>20} |\n"
              "| {2:<20}{6:>20} |\n"
              "| {3:<20}{7:>20} |\n"
              "| {4:<20}{8:>20} |"
              .format(sum(self.number),
                      "Number of Items: ",
                      "Subtotal: ",
                      "Sales Tax: ",
                      "Total Price: ",
                      sum(self.number),
                      Money(sum(self.total_price), "USD").format('en_US'),
                      Money((sum(self.total_price) * self.sales_tax), "USD").format('en_US'),
                      Money(sum(self.total_price) * (1 + self.sales_tax), "USD").format('en_US')))


def main():
    register = CashRegister()
    while True:
        item = input("Item Name: ")
        quantity = float(input("Quantity: "))  # Changed this to float since some things are measured by weight
        value = float(input("Value of Item: "))
        register.add_item(item, quantity, value)
        keep_going = input("Continue? [y/n]: ").lower()
        if keep_going == "n":
            print()
            register.printout()
            default = sys.stdout
            receipt_name = "{}.txt".format(datetime.datetime.now().strftime("%Y%M%dT%H%M%S"))
            receipt_printout = open(receipt_name, "w")
            sys.stdout = default
            payment_amount = float(input("| Payment Amount:                   $"))
            print("| {0:<20}{1:>20} |".format("Change:", Money(register.payment(payment_amount), "USD").format('en_US')))
            print("=" * len("| {:<10} | {:<10}  | {:<12}  |".format("Quantity", "Price/Item", "Price")))
            sys.stdout = receipt_printout
            register.printout()
            print("| {0:<20}{1:>20} |".format("Payment Amount:", Money(payment_amount, "USD").format('en_US')))
            print("| {0:<20}{1:>20} |".format("Change:", Money(register.payment(payment_amount), "USD").format('en_US')))
            print("=" * len("| {:<10} | {:<10}  | {:<12}  |".format("Quantity", "Price/Item", "Price")))
            sys.stdout = default
            receipt_printout.close()
            webbrowser.open(receipt_name)
            break


if __name__ == "__main__":
    main()
