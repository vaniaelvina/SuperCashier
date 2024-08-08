"""
This module contains a simple user interface, user ID and a menu loop 
"""

import datetime
import random
import string
from transaction import *

#create object
trnsct_123 = Transaction()

#greeting and user ID
while True:
    print("\n--------- Welcome to Self-Service Cashier ---------\n")
    print("Before making transactions, please fill in the information below")
    cust_name = input("\nName: ")
    cust_ID = cust_name +'_'+ ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    transaction_date = datetime.datetime.now()
    print(f"\nDate: {transaction_date}")
    print(f"Your ID: {cust_ID}")
    print(f"\nHello {cust_name}!")

    trnsct_123.check_order()

    #menu loop
    while True:       
        print('\nPlease choose 1 option below.')
        print('[1] Add item')
        print('[2] Update item name')
        print('[3] Update item quantity')
        print('[4] Update item price')
        print('[5] Delete item')
        print('[6] Reset transaction')
        print('[7] Check order')
        print('[8] Finish order')
        print('[9] Cancel')

        selected_menu = input(f"\nSelect menu: ")
        
        if selected_menu == "1":
            trnsct_123.add_item()
            continue
        elif selected_menu == "2":
            trnsct_123.update_item_name()
            continue
        elif selected_menu == "3":
            trnsct_123.update_item_qty()
            continue
        elif selected_menu == "4":
            trnsct_123.update_item_price()
            continue
        elif selected_menu == "5":
            trnsct_123.delete_item()
            continue
        elif selected_menu == "6":
            trnsct_123.reset_transaction()
            continue
        elif selected_menu == "7":
            trnsct_123.check_order()
            continue
        elif selected_menu == "8":
            print("\n----------- SUPERCASHIER -----------")
            print("\n----------- TRANSACTION INVOICE -----------")
            print(f"Date: {transaction_date}")
            print(f"ID: {cust_ID}")
            trnsct_123.total_price()
            break
        elif selected_menu == "9":
            trnsct_123.reset_transaction()
            break
        else:
            print("Selected menu is invalid, try again.")
            continue