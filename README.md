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
## User flow explanation:
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
Sure, here's the translation:

- `Transaction()`: Class that contains all the functions to execute the transaction process in the cashier system.
- `check_order()`: Function that checks if there are any stored items and if the user-inputted items are correct.
- `add_item()`: Function that adds and stores an item.
- `update_item_name()`: Function that updates the name of an item.
- `update_item_qty()`: Function that updates the quantity of an item.
- `update_item_price()`: Function that updates the price of an item.
- `delete_item()`: Function that deletes one or more items.
- `reset_transaction()`: Function that deletes all or resets the items.
- `total_price()`: Function that calculates and displays the total shopping amount, discount, and total payment.
