import datetime
import random
import string
from transaction import *

trnsct_123 = Transaction()

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

    while True:       
        trnsct_123.show_menu()
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
            trnsct_123.total_price()
            continue
        elif selected_menu == "9":
            break
        else:
            print("Selected menu is invalid, try again.")
            continue
    


