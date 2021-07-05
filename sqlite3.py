#access db with python

import sqlite3
connection=sqlite3.connect("\\home\\gopi\\Desktop\\test.db")
cursor=connection.cursor()

#ddl
#table creation

cursor.execute("Create table gopii(name varchar,id integer);")

#dml
#insert data

cursor.execute("insert into gopii(name,id) values('gopi','1');")
connection.commit()

#view data

cursor.execute("select * from gopii")
a=cursor.fetchall()
	print(i)

#update data

cursor.execute("update gopii set name='gopal' where name='gopi';")
cursor.execute("select * from gopii")
a=cursor.fetchall()
for i in a:
	print(i)
	
#delete data	
	
cursor.execute("delete from gopii where name='gopal';")
cursor.execute("select * from gopii")
a=cursor.fetchall()
for i in a:
	print(i)
	
#ddl

#add a coloum

cursor.execute("alter table gopii add column text;")
cursor.execute("select * from gopii")
a=cursor.fetchall()
for i in a:
	print(i)

	
#drop a column

cursor.execute("alter table gopii drop column column;")
cursor.execute("select * from gopii")
a=cursor.fetchall()
for i in a:
	print(i)

#change the data type of a column

cursor.execute("alter table gopii alter column name integer;")

#drop the table
cursor.execute("drop table gopii;")

#clear the table


cursor.execute("Create table gokul(name varchar,id integer);")
cursor.execute("insert into gokul(name,id) values('gopi','1');")
connection.commit()
cursor.execute("truncate table gokul;")
