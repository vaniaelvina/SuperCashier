# SuperCashier
## Background
SuperCashier is a self-service cashier built using python. 

## Tools
Languages: 
- Python

Libraries:
- Tabulate
- Pandas

## Features
1. Create transaction ID
2. Add item name, item quantity, and item price
4. Update item name
5. Update item quantity
6. Update item price
7. Delete item
8. Reset transaction
9. Cancel all transaction

## Flowchart
![SuperCashier Flowchart (1)](https://github.com/user-attachments/assets/6f594cb4-6595-4242-8d7f-f02aa5ead289)
User flow explanation:
1. User creates a transaction ID
2. Because the cart is empty, user will be asked to add item name, quantity and price
3. User can also add more items to the cart if needed
4. User can check the added items and change item name, quantity, or price, delete an item, or reset all transaction if needed
5. If user want to change the ID, user can cancel the transaction and start over
6. When user finish adding items to the cart, the system going to calculate all the orders and discounts

## How to use
1. Download this repository
2. Run **main.py**

## Functions
```
def add_item(self):
        """
        Method to add items to the dictionary. 
        Item name will be saved as keys. 
        Item quantity, price, and total price per item will be the values.
        """

        while True:
            print("\nAdd item")
            try:
                #adding item name, quantity, and price 
                item_name = str(input("Insert item name: "))
                item_qty = int(input("Insert item quantity: "))
                item_price = int(input("Insert item price: Rp  "))
                
                #if the added item already in the order, the quantity will be added
                if item_name in self.dict_trnsct.keys():
                    new_item_qty = self.dict_trnsct[item_name][0] + item_qty
                    item_total_price = new_item_qty * self.dict_trnsct[item_name][1]
                    
                    self.dict_trnsct[item_name][0] = new_item_qty
                    self.dict_trnsct[item_name][2] = item_total_price
        
                else:
                    item_total_price = item_qty*item_price
                    self.dict_trnsct[item_name] = [item_qty, item_price, item_total_price]

                #a loop to add more item              
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
            
            #validating user input
            except ValueError:
                print("Item quantity and price must be a number! Please insert the item again.")
                continue
```

