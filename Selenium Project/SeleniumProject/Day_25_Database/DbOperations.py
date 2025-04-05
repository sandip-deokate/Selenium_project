import mysql.connector
insert_query = "insert into customer values (5,'sandip5',1000,7)"
update_query="update customer set name='sandip55' where id =5"
delete_query = "delete from customer"
select_query = "select * from customer limit 5"

con=mysql.connector.connect(host="127.0.0.1", port=3306, user="root",passwd="Sandip@007",database="emp")
curs = con.cursor()
curs.execute(select_query)
for row in curs:
    print(row)
#con.commit()
con.close()