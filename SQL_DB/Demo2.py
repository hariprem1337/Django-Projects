from SQL_DB.utils import getCursor

curs = getCursor()
curs.execute("create table if not exists Employee(id_number integer unique, name text, contact integer unique, email text unique, salary real, experience real)")
id = int(input("IDNo : "))
name = input("Name : ")
contact = int(input("Contact Number : "))
email = input("Email Id : ")
salary = float(input("Salary : "))
exp = float(input("Experience : "))

curs.execute("insert into Employee values (?, ?, ?, ?, ?, ?)", (id, name, contact, email, salary, exp))
conn.commit()
print("Record is Inserted")