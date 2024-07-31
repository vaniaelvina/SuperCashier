import pandas as pd
from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.dict_trnsct = dict()

    def show_menu(self):
        print('Please choose 1 option below.')
        print('[1] Add item')
        print('[2] Update item name')
        print('[3] Update item quantity')
        print('[4] Update item price')
        print('[5] Delete item')
        print('[6] Reset transaction')
        print('[7] Check order')
        print('[8] Finish order')
    
    def add_item(self):
        while True:
            try:
                item_name = str(input("\nInsert item name: "))
                item_qty = int(input("Insert item quantity: "))
                item_price = int(input("Insert item price: Rp  "))
                
                if item_name in self.dict_trnsct.keys():
                    self.new_item_qty = self.dict_trnsct[item_name][0] + item_qty
                    self.item_total_price = self.new_item_qty * self.dict_trnsct[item_name][1]

                    self.dict_trnsct[item_name][0] = self.new_item_qty
                    self.dict_trnsct[item_name][2] = self.item_total_price
                else:
                    self.item_total_price = item_qty*item_price
                    self.dict_trnsct[item_name] = [item_qty, item_price, self.item_total_price]
                
                while True:
                    self.add_more_item = input("Add more item (y/n)? ")
                    if self.add_more_item.lower() == "y":
                        self.add_item()
                    elif self.add_more_item.lower() == "n":
                        self.check_order()
                    else:
                        print("Try again.")
                        continue  
                    
            except ValueError:
                print("Item quantity and price must be a number! Please insert the item again.")
                continue
            
    def update_item_name(self):
        while True:
            self.item_name = input("Item name you want to change:  ")
            self.updated_item_name = input("")
            if self.item_name in self.dict_trnsct.keys():
                self.dict_trnsct[]
            else
                


        

    def check_order(self):
        self.order_table=pd.DataFrame(self.dict_trnsct).T
        headers=["Item name","Item quantity","Item price", "Total item price"]
        
        if len(self.dict_trnsct) == 0:
            print(f"Your cart is empty. Add new item below.\n")
            self.add_item()
        else:
            print(f"\n{tabulate(self.order_table, headers, tablefmt='github')}\n")
            self.show_menu()
    

