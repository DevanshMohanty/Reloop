from db_scripts.delete_item import delete
from db_scripts.update_db import attribute_update
from db_scripts.product_fetch import all_products

def user_signal(signal):
    
    products = all_products()
    print('Select the Product:')
    for product in products:
        print(f"\n{product}")
    id = int(input().strip())

    if(signal == 'DELETE'):
        delete(int(id))
    
    elif(signal == 'EDIT'):
        print("Choose the change:\n1.Days Left\n2.Description\n3.Product Type")
        button = int(input().split())
        print("Enter new value")
        change = input()
        attribute_update(id,change,button)

    elif(signal == 'MANUAL_CHECK'): 







    