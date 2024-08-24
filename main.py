from transaction import Transaction

def main_menu(trnsct_123):
    '''
    This function shows ordered items and menu
    '''
    
    # a loop to show ordered items and menu
    while True:

        # showing ordered items
        trnsct_123.check_order()

        # showing menu 
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

        # ask user to select a menu
        try:
            selected_menu = int(input("\nSelect menu: "))
            if selected_menu not in range(1, 10):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        match selected_menu:
            case 1: trnsct_123.add_item()
            case 2: trnsct_123.update_item_name()
            case 3: trnsct_123.update_item_qty()
            case 4: trnsct_123.update_item_price()
            case 5: trnsct_123.delete_item()
            case 6: trnsct_123.reset_transaction()
            case 7: trnsct_123.check_order()
            case 8:
                trnsct_123.check_order()
                trnsct_123.total_price()
                return
            case 9: 
                trnsct_123.reset_transaction()
                return
            case _: print("Selected menu is invalid, try again.")

def main():

    '''This function creates a transaction object and display a simple UI for user'''

    # creates an object
    trnsct_123 = Transaction()
    
    # display a simple UI for user 
    while True:
        trnsct_123.clear_screen()
        print("\n------------- Welcome to Self-Service Cashier -------------")
        print("\nBefore making transactions, please fill in the information below")
        
        trnsct_123.user_id()

        main_menu(trnsct_123)

        # a loop for additional transaction by user
        while True:
            another_trnsct = input("\nCreate another transaction (y/n)?  ").strip().lower()
            if another_trnsct == "n":
                break
            elif another_trnsct == "y":
                continue
            else:
                print("Invalid input, please try again.")
        if another_trnsct == "n":
            break

if __name__ == "__main__":
    main()