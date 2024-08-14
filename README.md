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
9. Check order
10. Finish order
11. Exit

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
Say a customer named Andi want to make a transaction. The program will greet him and ask him to input his name then create an ID. Then, the program will show that his cart is empty and he will be asked to add an item to his cart.
![image](https://github.com/user-attachments/assets/7c224f2c-34bd-4214-905d-a6d80177fbaa)
![image](https://github.com/user-attachments/assets/a7fe3d19-ed54-4725-9756-d6b22a608e54)
1. Say Andi want to order
   - Fried Chicken
     Quantity: 2
     Price: Rp 20000
   - Toothpaste
     Quantity: 3
     Price: Rp 15000
   
   He will need to input each item's quantity and price as seen in the pictures below. After he's done adding items, the system will show all his orders, check any errors, and also show a menu.
![image](https://github.com/user-attachments/assets/b76730c0-6a2d-4929-997a-ee5668017e4a)
![image](https://github.com/user-attachments/assets/96546353-df18-4396-92d6-68d0a7336ac0)
![image](https://github.com/user-attachments/assets/84bf2d10-4abe-47c5-a384-5385ffd5ce33)

2. If Andi want to delete an item, he will need to choose menu `5` and type the item he want to delete. When an item is deleted, the system will automatically show all the orders without the deleted item.
   ![image](https://github.com/user-attachments/assets/e9b66720-d756-4b16-bfd5-172e78f29852)
   ![image](https://github.com/user-attachments/assets/e2316c78-c890-44ca-ae22-969417aa0f72)

3. If Andi want to delete all transaction without making a new ID, he can choose menu `6` to reset transaction. The system will delete all ordered items and show an empty cart then ask him to add items.
   ![image](https://github.com/user-attachments/assets/3f440bac-0c3d-454d-b9c5-6b7fda94836d)

4. When Andi is done with the transaction, the system will show all ordered items and the total.
   ![image](https://github.com/user-attachments/assets/a628c0c4-fbfa-4db7-97dc-605680b01f3f)


