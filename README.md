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
9. Cancel transaction

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

## Program explanation
1. transcation.py
   `Transaction()`

   Class that contains all the functions to execute the transaction process in the cashier system. In this class there are multiple methods below:
   - `init()`

     This method will initialize Transaction() and create an empty dictionary dict_trnsct.
     https://github.com/vaniaelvina/SuperCashier/blob/74accee37d5c8d0e78d2c8c319ec654a5964eaa6/transaction.py#L14-L17
   - `user_id()`

     This method will create a transaction ID by asking user name and create a username ID from the input. This function will also create a transaction date.
     https://github.com/vaniaelvina/SuperCashier/blob/74accee37d5c8d0e78d2c8c319ec654a5964eaa6/transaction.py#L19-L27
   - `add_item()`

     This method adds and stores item in the dictionary. In this method, the item name will be the key whereas item quantity and price will be the values.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L29-L82
   - `update_item_name()`

     This method updates the name of an item.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L83-L98

   - `update_item_qty()`
     This method updates the quantity of an item.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L100-L125
     
   - `update_item_price()`
   
     This method updates the price of an item.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L127-L152
     
   - `delete_item()`
   
     This method deletes an item.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L154-L169
   - `check_order()`

     This method checks if there any stored items and if the user-inputted items are correct.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L171-L201
   - `reset_transaction()`
   
     This method deletes all the items.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L202-L208
   - `total_price()`
   
     This method calculates the subtotal amount, discount, and total price.
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L210-L248

## Test case

