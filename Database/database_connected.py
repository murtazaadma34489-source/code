import mysql.connector as connector
print("Welcome to the Restaurant Management System")

mydb = connector.connect(host="localhost",user='root',passwd='murtaza123')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists restaurant_db")
print("Database created!")

mycursor.execute("use restaurant_db")
mycursor.execute("create table if not exists login(username varchar(25) not null, password varchar(25))")
print("Login Table created")
mycursor.execute("create table if not exists customer(customer_id int not null, name varchar(50), contactNo varchar(20), email varchar(100))")
print("customer table created")
mycursor.execute("create table if not exists order_details(order_id int not null AUTO_INCREMENT, order_date date, customer_name varchar(50), item_id int not null, amount double(16,2), primary key(order_id))")
print("order table created")
mycursor.execute("create table if not exists item(item_id int(8) not null, item_name varchar(50), item_price double(16,2), item_quantity int(8))")
print("item table created")

mydb.commit()

z = 0
mycursor.execute("select * from login")
for i in mycursor:
    z+=1
if(z==0):
    mycursor.execute("insert into login values('murtaza','murtaza123')")
    mydb.commit()

while True:
    print("""
    1. Admin
    2. Customer
    3. Exit
    """)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        pasword = input("Enter your password: ")
        mycursor.execute("select * from login")
        for i in mycursor:
            username, password = i
        if pasword == password:
            print("Welcome Admin")
            print()
            edit = 'y'
            while edit == 'y' or edit == 'Y':
                print("""
                1. Add New Item
                2. Update Item Price
                3. Delete an Item
                4. Display All Items
                5. Change your Password
                6. Log Out
                """)

                ch = int(input("Enter your choice: "))
                if ch == 1:
                    add_item = 'y'
                    while add_item == 'y' or add_item == 'Y':
                        item_id = int(input("Enter item id: "))
                        item_name = input("Enter item name: ")
                        item_price = float(input("Enter item price: "))
                        item_quantity = int(input("Enter item quantity: "))

                        mycursor.execute("insert into item values('"+str(item_id)+"','"+item_name+"','"+str(item_price)+"','"+str(item_quantity)+"')")
                        mydb.commit()
                        print("Item successfully inserted!")
                        add_item = input("Add another item? (y/n): ")
                    edit = input("Continue Editing? (y/n) ")

                elif ch == 2:
                    update = 'y'
                    while(update == 'y' or update=='Y'):
                        item_id = int(input("Enter item id you want to update: "))
                        new_price = float(input("Enter the new price: "))
                        mycursor.execute("update item set item_price = '"+str(new_price)+"' where item_id = '"+str(item_id)+"'")
                        mydb.commit()
                        print("Price updated successfully!")
                        update = input("Update price for another item? (y/n): ")
                    edit = input("Continue Editing? (y/n) ")

                elif ch == 3:
                    delete = 'y'
                    while(delete=='y' or delete=='Y'):
                        item_id = int(input("Enter id of the item you want to delete!"))
                        mycursor.execute("delete from item where item_id = '"+str(item_id)+"'")
                        mydb.commit()
                        print("item deleted successfully!")
                        delete=input("Delete another item? (y/n): ")
                    edit = input("Continue Editing? (y/n) ")

                elif ch == 4:
                    mycursor.execute("select * from item")
                    print("item id || item name || item price || item quantity")
                    for i in mycursor:
                        id,name,price,quantity=i
                        print(f"{id} || {name} || {price} || {quantity}")

                elif ch == 5:
                    old_pass = input("Enter old password: ")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        username,password = i
                    if old_pass == password:
                        new_password = input("Enter new password: ")
                        mycursor.execute("update login set password = '"+new_password+"'")
                        mydb.commit()
                        print("Password updated successfully!")
                        
                elif ch == 6:
                    break
        else:
            print("You Entered wrong password")
    
    #Customer login
    elif ch == 2:
        print("""
              1. Place an Order
              2. View my Bill
              3. View Menu
              4. Go Back""")
        ch=int(input("Enter your choice: "))
        if ch == 1:
            name = input("Enter your name: ")
            item_id = int(input("Enter the item id: "))
            quantity = int(input("Enter item quantity: "))
            mycursor.execute("select * from item where item_id = '"+str(item_id)+"'")
            for i in mycursor:
                i_id,i_name,i_price,i_quantity = i
            amount = i_price * quantity    
            new_quantity = i_quantity - quantity
            mycursor.execute("update item set item_quantity = '"+str(new_quantity)+"' where item_id = '"+str(item_id)+"'")

            #mycursor.execute("insert into order_details values(now(),'"+name+"','"+str(item_id)+"','"+str(amount)+"')")
            mycursor.execute("insert into order_details (order_date, customer_name, item_id, amount) values (CURDATE(), '"+name+"', '"+str(item_id)+"', '"+str(amount)+"')")
            mydb.commit()
            print("item added to the order")
        elif ch == 2:
            print(f"Your Bill is PKR{amount}")
        
        elif ch == 3:
            print("item id || item name || item price ")
            mycursor.execute("select item_id, item_name, item_price from item")
            for i in mycursor:
                i_id,i_name,i_price = i
                print(f"{i_id} || {i_name} || {i_price}")
        
        elif ch == 4:
            break
    elif ch == 3:
        break


    