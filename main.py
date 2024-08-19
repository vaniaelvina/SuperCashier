from transaction import Transaction

def main_menu(trnsct_123):
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

        try:
            selected_menu = int(input("\nSelect menu: "))
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
            case 9: return
            case _: print("Selected menu is invalid, try again.")

def main():
    trnsct_123 = Transaction()
    
    while True:
        trnsct_123.clear_screen()
        print("\n------------- Welcome to Self-Service Cashier -------------")
        print("\nBefore making transactions, please fill in the information below")
        
        trnsct_123.user_id()

        main_menu(trnsct_123)

        another_trnsct = input("\nCreate another transaction (y/n)?  ").strip().lower()
        if another_trnsct == "n":
            break

if __name__ == "__main__":
    main()
