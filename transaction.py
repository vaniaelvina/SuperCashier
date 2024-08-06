import pandas as pd
from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.dict_trnsct = dict()

    def show_menu(self):
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
                         
    def add_item(self):
        print("\nAdd item")
        while True:
            try:
                item_name = str(input("Insert item name: "))
                item_qty = int(input("Insert item quantity: "))
                item_price = int(input("Insert item price: Rp  "))
                
                if item_name in self.dict_trnsct.keys():
                    new_item_qty = self.dict_trnsct[item_name][0] + item_qty
                    item_total_price = new_item_qty * self.dict_trnsct[item_name][1]
                    
                    self.dict_trnsct[item_name][0] = new_item_qty
                    self.dict_trnsct[item_name][2] = item_total_price
                
                else:
                    item_total_price = item_qty*item_price
                    self.dict_trnsct[item_name] = [item_qty, item_price, item_total_price]
                                
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
            except ValueError:
                print("Item quantity and price must be a number! Please insert the item again.")
                continue

    def update_item_name(self):
        while True:
            print("\nUpdate item name")
            item_name = input("Item name you want to change:  ")
            if item_name in self.dict_trnsct.keys():
                updated_item_name = input("New item name:  ")
                self.dict_trnsct[updated_item_name] = self.dict_trnsct[item_name]
                del self.dict_trnsct[item_name]
                self.check_order()
                break
            else:
                print("Item name is not found, try again.")
                continue
                
   
    def update_item_qty(self):
        while True:
            print("\nUpdate item quantity")
            item_name = input("Item name the quantity you want to change:  ")
            if item_name in self.dict_trnsct.keys():
                try:
                    updated_item_qty = int(input("New quantity:  "))
                    self.dict_trnsct[item_name][0] = updated_item_qty
                    new_total_item_price = updated_item_qty * self.dict_trnsct[item_name][1]
                    self.dict_trnsct[item_name][2] = new_total_item_price
                    self.check_order()
                except ValueError:
                    print("Item quantity must be a number, try again.")
                    continue
            else:
                print("Item name is not found, try again.")
    
    def update_item_price(self):
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
                except ValueError:
                    print("Item price must be a number, try again.")
                    continue
            else:
                print("Item name is not found, try again.")
                continue
    
    def delete_item(self):
        while True:
            deleted_item = input("Item name you want to delete:  ") 
            if deleted_item in self.dict_trnsct.keys():
                del self.dict_trnsct[deleted_item]
                self.check_order()
            else:
                print("Item name is not found, try again.")
                continue
    
    def check_order(self):
        order_table=pd.DataFrame(self.dict_trnsct).T
        headers=["Item name","Item quantity","Item price", "Total item price"]
    
        if len(self.dict_trnsct) == 0:
            print(f"Your cart is empty. Add new item below.")
            self.add_item()
        else:
            print(f"\n{tabulate(order_table, headers, tablefmt='github')}\n")
            if any(any(0 > minus for minus in val) or 0 in val for val in self.dict_trnsct.values()):
                print("Ada kesalahan input harga atau jumlah, mohon cek order anda")
            elif "" in self.dict_trnsct.keys():
                print("Ada kesalahan input nama barang, mohon cek order anda")
            else:
                print("Pemesanan sudah benar")

    def reset_transaction(self):
        self.dict_trnsct.clear()
        print("All items have been deleted")

    def total_price(self):
        self.check_order()
        for item_name in self.dict_trnsct:
            subtotal += self.dict_trnsct[item_name][2]
        
        if subtotal>500_000:
            discount = int(subtotal*0.1)
            final_price = int(subtotal-discount)
            print(f"Discount 10%    = Rp {discount}")
            print(f"Total price     = Rp {final_price}")

        elif subtotal>300_000:
            discount = int(subtotal*0.08)
            final_price = int(subtotal-discount)
            print(f"Discount 10%    = Rp {discount}")
            print(f"Total price     = Rp {final_price}")

        elif subtotal>200_000:
            discount = int(subtotal*0.05)
            final_price = int(subtotal-discount)
            print(f"Discount 10%    = Rp {discount}")
            print(f"Total price     = Rp {final_price}")

        else:
            print(f"Total price = Rp {final_price}")

    

    

