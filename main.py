"""
This module contains a simple user interface, user ID and a menu loop 
"""

import os
from transaction import Transaction

# create object
trnsct_123 = Transaction()


while True:

    os.system('cls')
    
    # greeting 
    print("\n------------- Welcome to Self-Service Cashier -------------")
    print("\nBefore making transactions, please fill in the information below")
    
    trnsct_123.user_id()


    # menu loop
    while True:      
        trnsct_123.check_order()

        print('\nPlease choose 1 option below.')
        print('[1] Add item')
        print('[2] Update item name')
        print('[3] Update item quantity')
        print('[4] Update item price')
        print('[5] Delete item')
        print('[6] Reset transaction')
        print('[7] Check order')
        print('[8] Finish order')
        print('[9] Exit')

        selected_menu = int(input(f"\nSelect menu: "))
        
        match selected_menu:
            case 1:
                trnsct_123.add_item()
                continue
            case 2:
                trnsct_123.update_item_name()
                continue
            case 3:
                trnsct_123.update_item_qty()
                continue
            case 4:
                trnsct_123.update_item_price()
                continue
            case 5:
                trnsct_123.delete_item()
                continue
            case 6:
                trnsct_123.reset_transaction()
                continue
            case 7:
                trnsct_123.check_order()
                continue
            case 8:
                trnsct_123.check_order()
                trnsct_123.total_price()
                break
            case 9:
                break
            case _:
                print("Selected menu is invalid, try again.")
                continue
    
    if selected_menu == 8:
        another_trnsct = input("\nCreate another transaction (y/n)?  ")
        if another_trnsct.lower() == "y":
            continue
        elif another_trnsct.lower() == "n":
            break  

            

