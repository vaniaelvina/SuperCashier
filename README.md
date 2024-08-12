# SuperCashier
## Description
SuperCashier is a self-service cashier system built using python.

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
10. Exit 

## Flowchart
![SuperCashier Flowchart (3)](https://github.com/user-attachments/assets/72207beb-8d95-453c-9772-d4af67e70306)

## User flow explanation
1. User creates a transaction ID.
2. Because the cart is empty, user will be asked to add item name, its quantity and its price.
3. User then can also add more items to the cart if needed.
4. User then can also check the added items and change their name, quantity, or price, delete an item, or reset all transaction if needed.
5. If user want to change the ID, user can exit the system and start over.
6. When user finish adding items to the cart, the system will calculate all the orders.
7. For subtotal amount more than Rp 500.000, user will get 10% discount.
8. For subtotal amount more than Rp 300.000, user will get 8% discount.
9. For subtotal amount more than Rp 200.000, user will get 5% discount.
10. After the transaction, user can do another transaction with another transaction ID if needed.

## How to use
1. Download this repository
2. Run **main.py**

## Program Functions
1. transcation.py
   `Transaction()`: Class that contains all the functions to execute the transaction process in the cashier system. In this class there are multiple methods below:
   - `init()`
     This function will initialize Transaction() and create an empty dictionary dict_trnsct.
   - `user_id()`
     This function will create a transaction ID by asking user name and create a username ID from the input. This function will also create a transaction date.
   - `add_item()`: Method that adds and stores item in the dictionary. In this method, the item name will be the key whereas item quantity and price will be the values.
   - `update_item_name()`: Function that updates the name of an item.
   - `update_item_qty()`: Function that updates the quantity of an item.
   - `update_item_price()`: Function that updates the price of an item.
   - `delete_item()`: Function that deletes one or more items.
   - `reset_transaction()`: Function that deletes all or resets the items.
   - `check_order()`: Function that checks if there any stored items and if the user-inputted items are correct.
   - `total_price()`: Function that calculates the total shopping amount, discount, and total payment.
