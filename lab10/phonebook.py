import psycopg2
import csv

conn=psycopg2.connect(
    host="localhost",
    database="lab10",
    user="postgres",
    password="dilyara2639_"
)

cur=conn.cursor()

def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Phonebook(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20)
        );
    ''')
    conn.commit()


def insert_manual():
    name=input(("Your name: "))
    phone=input(("Your pnone number: "))
    cur.execute("INSERT INTO Phonebook (first_name,phone) VALUES(%s,%s)",(name,phone))
    conn.commit()

def insert_from_csv(filename):
    with open(filename,newline='',encoding='utf-8') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO Phonebook (first_name,phone) VALUES(%s,%s)",(row["first_name"],row["phone"]))
            conn.commit()
        
def update_user(name, new_phone):
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()

def find_user(name=None, phone=None):
    if name:
        cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s", (name,))
    elif phone:
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user(name=None, phone=None,letter=None):
    if name:
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    conn.commit()
    print(" Deleted successfully.") 

create_table()
insert_manual()
#insert_from_csv('contacts.csv')
# update_user("Dilyara", "87001231234")
# find_user(name="Dilyara")
#delete_user(name="Dilyara")

cur.close()
conn.close()