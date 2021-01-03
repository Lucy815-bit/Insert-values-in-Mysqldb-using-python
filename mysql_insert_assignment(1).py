#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Enter your password here"
)

print(db)


# In[2]:


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Enter your password here"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'datacamp'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'datacamp' database
cursor.execute("CREATE DATABASE Mydatabase")


# In[20]:


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Enter yourpassword here",
    database = "Mydatabase"
)

cursor = db.cursor()

## creating a table called 'users' in the 'mydatabase' database
cursor.execute("CREATE TABLE customer (firstname VARCHAR(255), lastname VARCHAR(255), address VARCHAR(255), email VARCHAR(255), phone VARCHAR(255), city VARCHAR(255), state VARCHAR(255), country VARCHAR(255))")


# In[ ]:





# In[27]:


import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Enter your password here",
  database="Mydatabase"
)
my_database = db_connection.cursor()
sql = "INSERT INTO customer(firstname,lastname, address, email, phone,city,state,country) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
values = [ 
    ('Peter', 'Mwangi', 'Lowstreet 4','perterm@gmail.com','817-707-8732','Abuja','Equatorial','Nigeria'),
    ('Amy', 'Wanja', 'Apple st 652','Amy-Wanja@yahoo.com','817-187-8732','Dallas','Texas','USA'),
    ('Hannah', 'Hannadez', 'Mountain 21','HannahHannadez@ymail.com','817-787-4732','Miami','Florida','USA'),
    ('Michael', 'Onyango', 'Valley 345','perterm@gmail.com','847-787-8432','Manchester City','Manchester','United Kingdom'),
    ('Sandy', 'Beach', 'Ocean blvd 2','SandyBeach@gmail.com','847-757-8732','Ocala','Florida','USA'),
    ('Betty', 'Oprah','Green Grass 1','perterm@gmail.com','827-787-8732','Chicago','Illinois','USA'),
    ('Richard', 'Galloh', 'Sky st 331','perterm@gmail.com','812-787-0032','New York','New York','USA'),
    ('Susan', 'Griffin', 'Oneway 98','perterm@aol.com','817-787-8700','NAirobi','Nairobi','Kenya'),
    ('Vicky', 'Weja', 'Yellow Garden 2','Vicky.Weja@gmail.com','817-717-2332','Fort Bend','Indiana','USA'),
    ('Ben', 'Oguttu', 'Park Lane 38','BenOguttu@aol.com','807-727-8732','Plantation','Alabama','USA'),
    ('William', 'Ndola', 'Central st 954','WilliamNdola@gmail.com','810-787-8733','Houston','Texas','USA'),
    ('Chuck', 'Norris', 'Main Road 989','ChuckNorris@gmail.com','817-787-8734','Waco','Texas','USA'),
    ('Viola', 'Davis', 'Sideway 1633','Violad@gmail.com','817-787-8732','Los Angeles','California','USA')
    ]
my_database.executemany(sql,values)
db_connection.commit()
print(my_database.rowcount, "was inserted successfully.")


# In[1]:


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Enter your password here",
    database = "mydatabase"
)

cursor = db.cursor()

## adding 'id' column to the 'users' table
## 'FIRST' keyword in the statement will add a column in the starting of the table
cursor.execute("ALTER TABLE customer ADD COLUMN customerID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

cursor.execute("DESC customer")

print(cursor.fetchall())


# In[30]:


#Insert a new field, call it customer ID in the customer's table you created.
#Run this update Python programs
#After the running, then display and share a screenshot with us in the forum
#Insert a new field, call it customer ID in the customer's table you created.
#Run this update Python programs
#After the running, then display and share a screenshot with us in the forum



# In[ ]:





# In[ ]:




