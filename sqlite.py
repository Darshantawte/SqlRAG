import sqlite3

#connect to sqlite
connection  =sqlite3.connect("employee.db")

#create a cursor object
cursor = connection.cursor()

#create table
table_info = """
 CREATE TABLE IF NOT EXISTS Employee (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Department TEXT,
            Salary REAL
        )
"""

cursor.execute(table_info)

cursor.execute('''INSERT INTO Employee values (1,'Krish','Manufacturing',50000.0)''')
cursor.execute('''INSERT INTO Employee values (2,'Ethan','Manufacturing',55000.0)''')
cursor.execute('''INSERT INTO Employee values (3,'Olivia','Sales',60000.0)''')
cursor.execute('''INSERT INTO Employee values (4,'Noah','Manufacturing',57000.0)''')
cursor.execute('''INSERT INTO Employee values (5,'Emma','IT',70000.0)''')
cursor.execute('''INSERT INTO Employee values (6,'Liam','Manufacturing',45000.0)''')
cursor.execute('''INSERT INTO Employee values (7,'Sophia','Manufacturing',52000.0)''')
cursor.execute('''INSERT INTO Employee values (8,'Jacob','Finance',50000.0)''')
cursor.execute('''INSERT INTO Employee values (9,'Ava','Sales',56000.0)''')
cursor.execute('''INSERT INTO Employee values (10,'Mason','Sales',58000.0)''')
cursor.execute('''INSERT INTO Employee values (11,'Amelia','IT',65000.0)''')
cursor.execute('''INSERT INTO Employee values (12,'Lucas','IT',80000.0)''')
cursor.execute('''INSERT INTO Employee values (13,'Mia','IT',67000.0)''')
cursor.execute('''INSERT INTO Employee values (14,'Isabella','Finance',50000.0)''')
cursor.execute('''INSERT INTO Employee values (15,'Lily','IT',50000.0)''')
cursor.execute('''INSERT INTO Employee values (16,'James','Sales',50000.0)''')
cursor.execute('''INSERT INTO Employee values (17,'Snape','Finance',50000.0)''')
cursor.execute('''INSERT INTO Employee values (18,'Voldemort','IT',78000.0)''')
cursor.execute('''INSERT INTO Employee values (19,'Bheem','Sales',45000.0)''')

#Display all the records
print("Inserted records are:")
data = cursor.execute(''' Select * From Employee''')

for row in data:
    print(row)

connection.commit()
connection.close()