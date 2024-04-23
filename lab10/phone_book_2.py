import psycopg2
import dotenv
import os
import csv

dotenv.load_dotenv()
PASSWORD = os.getenv('PASSWORD')
conn = psycopg2.connect(
    host='localhost',
    database='fatal',
    user='postgres',
    password=PASSWORD
)

cur = conn.cursor()

def create_table():
    cur.execute(
        '''
    create table if not exists phone_book(
        id serial primary key,
        first_name varchar(30),
        phone varchar(20)
    );
    '''
    )
    conn.commit()

# Insert data from CSV file
def insert_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            cur.execute(f"insert into phone_book (first_name, phone) values ('{row['first_name']}', '{row['phone']}')")
    conn.commit()

# Manually enter data
def insert_manually():
    first_name = input("Enter first name: ")
    phone = input("Enter phone number: ")
    cur.execute(f"insert into phone_book (first_name, phone) values ('{first_name}', '{phone}')")
    conn.commit()

# Update data
def update_data(old_value, new_first_name=None, new_phone=None):
    if new_first_name:
        cur.execute(f"update phone_book set first_name = '{new_first_name}' where first_name = '{old_value}'")
    if new_phone:
        cur.execute(f"update phone_book set phone = '{new_phone}' where phone = '{old_value}'")
    conn.commit()

# Query data
def query_data(first_name=None, phone=None):
    if first_name and phone:
        cur.execute(f"select * from phone_book where first_name = '{first_name}' and phone = '{phone}'")
    elif first_name:
        cur.execute(f"select * from phone_book where first_name = '{first_name}'")
    elif phone:
        cur.execute(f"select * from phone_book where phone = '{phone}'")
    else:
        cur.execute("select * from phone_book")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Delete data
def delete_data(first_name=None, phone=None):
    if first_name:
        cur.execute(f"delete from phone_book where first_name = '{first_name}'")
    if phone:
        cur.execute(f"delete from phone_book where phone = '{phone}'")
    conn.commit()


create_table()

insert_manually()  
update_data('John', new_first_name='Jonathan')  
query_data(first_name='Jonathan')  
delete_data(phone='1234567890')  
insert_from_csv('/Users/ualihanbisenev/Desktop/File_cabinet/KBTU/PP2/lab10/exampel.csv')

conn.close()