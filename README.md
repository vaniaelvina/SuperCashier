# SuperCashier

## Description
SuperCashier is a self-service cashier system built using python. 

## Tools
Languages: 
- Python

Libraries:
- Tabulate
- Pandas

## Project Background
An owner of a supermarket located in one of the small towns in Indonesia has a plan to implement a cashier system that can be self-service, so customers can directly scan and pay for the items they buy, reducing the time spent buying, thus, customers do not have to queue at said town’s supermarket anymore. After conducting research, it turns out that there are problems with the system. He needs a Programmer to create some features for this self-service cashier system so that it can run smoothly.

## Features
1. Create an ID
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
1. User starts the system and creates an ID.
2. Because the cart is empty, user will be asked to add item name, its quantity and its price.
3. User then can also add more items to the cart if needed.
4. User then can also check the added items and change their name, quantity, or price, delete an item, or reset all transaction if needed.
5. If user want to change the ID, user can exit the system and start over.
6. When user finish adding items to the cart, the system will calculate subtotal of all items ordered.
7. For subtotal amount more than Rp 500.000, user will get 10% discount.
8. For subtotal amount more than Rp 300.000, user will get 8% discount.
9. For subtotal amount more than Rp 200.000, user will get 5% discount.
10. After the transaction, user can do another transaction with another transaction ID if needed.

## How to use
1. Download this repository
2. Run **main.py**

## Program explanation
1. transaction.py

    `Transaction()`

   Class that contains all the functions to execute the transaction process in the cashier system. In this class there are multiple methods below:
   - `init()`

     This method will initialize Transaction() and create an empty dictionary dict_trnsct.
     https://github.com/vaniaelvina/SuperCashier/blob/74accee37d5c8d0e78d2c8c319ec654a5964eaa6/transaction.py#L14-L17
   - `clear_screen()`

     This method will clear the user screen and can be called when needed.
     https://github.com/vaniaelvina/SuperCashier/blob/5d35deb127802165d5b91c022d34dea5cd51063b/transaction.py#L19-L22
   - `user_id()`

     This method will create an ID by asking user name and create a user ID from the input. This function will also create a transaction date.
     https://github.com/vaniaelvina/SuperCashier/blob/5d35deb127802165d5b91c022d34dea5cd51063b/transaction.py#L24-L32
   - `add_item()`

     This method adds and stores item in the dictionary. In this method, the user will be asked to input the item's name they want to add, its quantity and its price. It will first check whether the input is correct before proceeding. If the input is not valid, the system will ask the user to input the item again. If the input is valid, the system will calculate the total price of the item. It will also offer the user whether they want to add more than 1 item. In this method, the item name will be the key of the dictionary whereas item quantity, price per item and total price per item will be the values.      
     https://github.com/vaniaelvina/SuperCashier/blob/1074d6ebf652bf20aeb1e686dbe14326ab810aa4/transaction.py#L34-L86
   - `update_item_name()`

     This method updates the name of an item. First, the system will ask the user which item's quantity they want to change. If the user inputs an item name that doesn't exist in the ordered items, the system will prompt the user to re-enter the item name. If the item exists in the ordered items, the system will ask for the correct name, update it, and delete the old name from the ordered items.
     https://github.com/vaniaelvina/SuperCashier/blob/00120a25ca1b8028fbe36131baa307856dd4fc2e/transaction.py#L88-L103

   - `update_item_qty()`
     This method updates the quantity of an item. First, the system will ask the user which item's quantity they want to change. If the user inputs an item name that doesn't exist in the ordered items, the system will prompt the user to re-enter the item name. If the item exists in the ordered items, the system will ask for the correct quantity, update it, and delete the old quantity from the ordered items. It will also calculate the total price of an item"
     https://github.com/vaniaelvina/SuperCashier/blob/bfd3d90e6c023a2abb5cda96e9f596dbcd93298b/transaction.py#L105-L130
     
   - `update_item_price()`
   
     This method updates the price of an item. First, the system will ask the user which item's price they want to change. If the user inputs an item name that doesn't exist in the ordered items, the system will prompt the user to re-enter the item name. If the item exists in the ordered items, the system will ask for the correct price, update it, and delete the old price from the ordered items. It will also calculate the total price of an item."
     https://github.com/vaniaelvina/SuperCashier/blob/bfd3d90e6c023a2abb5cda96e9f596dbcd93298b/transaction.py#L132-L157
     
   - `delete_item()`
   
     This method deletes an item.
     https://github.com/vaniaelvina/SuperCashier/blob/bfd3d90e6c023a2abb5cda96e9f596dbcd93298b/transaction.py#L159-L174
   - `check_order()`

     This method checks if there are any stored items and if the user-inputted items are correct. This method will show customer ID, transaction date, all the ordered items with its quantity, its price per item and total price per item. If there are any empty input, it will notice the customer. Otherwise, it will state that there's no error detected.
     https://github.com/vaniaelvina/SuperCashier/blob/bfd3d90e6c023a2abb5cda96e9f596dbcd93298b/transaction.py#L176-L206
   - `reset_transaction()`
   
     This method deletes all the items.
     https://github.com/vaniaelvina/SuperCashier/blob/bfd3d90e6c023a2abb5cda96e9f596dbcd93298b/transaction.py#L207-L213
   - `total_price()`
   
     This method calculates the subtotal of the items ordered, discount, and total price. For subtotal amount more than Rp 500.000, user will get 10% discount. For subtotal amount more than Rp 300.000, user will get 8% discount. For subtotal amount more than Rp 200.000, user will get 5% discount.
     https://github.com/vaniaelvina/SuperCashier/blob/bfd3d90e6c023a2abb5cda96e9f596dbcd93298b/transaction.py#L215-L253
     
2. main.py
   
   This module imports functions from module Transaction.py and methods to show simple UI.
   - `main_menu(trnsct_123)`

     This function displays the ordered items and a menu for the user to interact with the Transaction object which is trnsct_123. It also contains menu loop and ask user to input their selected menu.  If the input is not a number between 1 and 9, it will ask the user to re-input the menu.
     https://github.com/vaniaelvina/SuperCashier/blob/05d3bc828f45ef14121549c07f7b679e9a39e1f3/main.py#L3-L50

   - `main()`
     
     This function drives the program's overall flow. It creates an instance of the Transaction class which is trnsct_123. It will greet user and call methods that will create customer ID and show function main menu.
     https://github.com/vaniaelvina/SuperCashier/blob/05d3bc828f45ef14121549c07f7b679e9a39e1f3/main.py#L52-L79
   
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
   ![image](https://github.com/user-attachments/assets/8d287583-58e6-4fa0-8630-8cc986348352)

3. If Andi want to delete all transaction without making a new ID, he can choose menu `6` to reset transaction. The system will delete all ordered items and show an empty cart then ask him to add items.
   
   ![image](https://github.com/user-attachments/assets/3f440bac-0c3d-454d-b9c5-6b7fda94836d)

4. When Andi is done with the transaction, the system will show all ordered items and the total.
   
   ![image](https://github.com/user-attachments/assets/a628c0c4-fbfa-4db7-97dc-605680b01f3f)


