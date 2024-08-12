"""
This module contains class and methods mainly used to calculate the transaction.
This module will be imported to module main.py.  
"""

import os
import random
import string
import datetime
import pandas as pd
from tabulate import tabulate

class Transaction:
    def __init__(self):
        """Initialize a dictionary containing transaction orders"""

        self.dict_trnsct = dict()
    
    def user_id(self):
        """Create customer ID and transaction date"""

        # create customer ID
        cust_name = input("\nName: ")
        self.cust_id = cust_name +'_'+ ''.join(random.choices(string.ascii_letters + string.digits, k=4))

        # create transaction date
        self.trnsct_date = datetime.datetime.now()
                         
    def add_item(self):
        """
        Method to add items to the dictionary. 
        Item name will be saved as keys. 
        Item quantity, price, and total price per item will be the values.
        """

        while True:
            print("\nAdd item")
            try:
                # adding item name, quantity, and price 
                item_name = str(input("Insert item name: "))
                item_qty = int(input("Insert item quantity: "))
                item_price = int(input("Insert item price: Rp  "))
                
                
                # function that validates item quantity and price to be a positive number
                if item_qty <= 0 or item_price <= 0:
                    print("Item quantity and price must be a positive number, please try again.")
                    break
                else:
                    pass

                # if the added item already in the order, the quantity will be added
                if item_name in self.dict_trnsct.keys():
                    new_item_qty = self.dict_trnsct[item_name][0] + item_qty
                    item_total_price = new_item_qty * self.dict_trnsct[item_name][1]
                    
                    self.dict_trnsct[item_name][0] = new_item_qty
                    self.dict_trnsct[item_name][2] = item_total_price
        
                else:
                    item_total_price = item_qty*item_price
                    self.dict_trnsct[item_name] = [item_qty, item_price, item_total_price]

                # a loop to add more item              
                while True:
                    add_more_item = input("\nAdd more item (y/n)? ")
                    if add_more_item.lower() == "y":
                        self.add_item()
                        break
                    elif add_more_item.lower() == "n":
                        self.check_order()
                        break
                    else:
                        print("Try again.")
                        continue  
                break
            
            # validating user input
            except ValueError:
                print("Item quantity and price must be a number! Please insert the item again.")
                continue

    def update_item_name(self):
        """
        Method to change name of an added item
        """
        
        while True:
            print("\nUpdate item name")
            item_name = input("Item name you want to change:  ")
            if item_name in self.dict_trnsct.keys():
                updated_item_name = input("New item name:  ")
                self.dict_trnsct[updated_item_name] = self.dict_trnsct[item_name]
                del self.dict_trnsct[item_name]
                break
            else:
                print("Item name is not found, try again.")
                continue
                
    def update_item_qty(self):
        """
        Method to change quantity of an added item
        """
        
        while True:
            print("\nUpdate item quantity")
            item_name = input("Item name the quantity you want to change:  ")
            
            if item_name in self.dict_trnsct.keys():
                try:
                    updated_item_qty = int(input("New quantity:  "))
                    self.dict_trnsct[item_name][0] = updated_item_qty
                    new_total_item_price = updated_item_qty * self.dict_trnsct[item_name][1]
                    self.dict_trnsct[item_name][2] = new_total_item_price
                    break
                
                # validating user input
                except ValueError:
                    print("Item quantity must be a number, try again.")
                    continue
            
            # validating user input
            else:
                print("Item name is not found, try again.")
                continue
    
    def update_item_price(self):
        """
        Method to change price of an added item
        """
       
        while True:
            print("\nUpdate item price")
            item_name = input("Item name which price you want to change:  ")
            if item_name in self.dict_trnsct.keys():
                try:
                    updated_item_price = int(input("New price:  "))
                    self.dict_trnsct[item_name][1] = updated_item_price
                    new_total_item_price = updated_item_price * self.dict_trnsct[item_name][0]
                    self.dict_trnsct[item_name][2] = new_total_item_price
                    self.check_order()
                    break
                
                # validating user input
                except ValueError:
                    print("Item price must be a number, try again.")
                    continue

            # validating user input
            else:
                print("Item name is not found, try again.")
                continue
    
    def delete_item(self):
        """
        Method to delete an added item
        """
    
        while True:
            deleted_item = input("Item name you want to delete:  ") 
            if deleted_item in self.dict_trnsct.keys():
                del self.dict_trnsct[deleted_item]
                self.check_order()
                break

            # validating user input
            else:
                print("Item name is not found, try again.")
                continue
    
    def check_order(self):
                
        """
        Method to check whether user order is correct
        """
        
        os.system('cls')
        
        # create a table containing orders
        order_table=pd.DataFrame(self.dict_trnsct).T
        headers=["Item name","Item quantity","Item price", "Total item price"]   

        print("\n--------------------------- SUPERCASHIER ---------------------------")
        print("----------------------- Self-Service Cashier -----------------------")
        print(f"\nDate: {self.trnsct_date}")
        print(f"Your ID: {self.cust_id} ")  
        
        # if order is empty, user will be asked to add item
        if len(self.dict_trnsct) == 0:
            print(f"\nYour cart is empty.")
            self.add_item()

        # checking whether there's error in user input
        else:
            print("\n------------------------------ ORDERS ------------------------------")
            print(f"\n{tabulate(order_table, headers, tablefmt='github')}\n")
            if "" in self.dict_trnsct.keys():
                print("There's an error in your order, check your item's name again.")
            else:
                print("No error detected.")

    def reset_transaction(self):
        """
        Method to delete all orders
        """

        self.dict_trnsct.clear()
        print("All items have been deleted")

    def total_price(self):
        """
        Method to calculate all orders with discounts
        """
        # total order counter
        subtotal=0

        # display and checking items added
        self.check_order()

        # calculating total orders
        for item_name in self.dict_trnsct:
            subtotal += self.dict_trnsct[item_name][2]
            total_price = subtotal
        
        # calculating discount
        try:
            if subtotal>500_000:
                discount = int(subtotal*0.1)
                total_price = int(subtotal-discount)
                print(f"\nDiscount 10%    = - Rp {discount}")
                print(f"Total            = Rp {total_price}")

            elif subtotal>300_000:
                discount = int(subtotal*0.08)
                total_price = int(subtotal-discount)
                print(f"\nDiscount 8%     = - Rp {discount}")
                print(f"Total            = Rp {total_price}")

            elif subtotal>200_000:
                discount = int(subtotal*0.05)
                total_price = int(subtotal-discount)
                print(f"\nDiscount 5%     = - Rp {discount}")
                print(f"Total            = Rp {total_price}")

            else:
                print(f"\nTotal           = Rp {total_price}")
        finally:
            print("\n----------------------------- THANK YOU ----------------------------")
            



    

    

