import datetime
import random
import string
from transaction import *

trnsct_123 = Transaction()

print("\n--------- Welcome to Self-Service Cashier ---------\n")
print("Before making transactions, please fill in the information below")
cust_name = input("\nName: ")
cust_ID = cust_name +'_'+ ''.join(random.choices(string.ascii_letters + string.digits, k=4))
transaction_date = datetime.datetime.now()
print(f"\nDate: {transaction_date}")
print(f"Your ID: {cust_ID}")
print(f"\nHello {cust_name}!")


