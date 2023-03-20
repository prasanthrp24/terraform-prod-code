#Comment  - Adding IP changes
import psycopg2

conn = psycopg2.connect(database="postgres",
						user='postgres', password='mysecretpassword',
						host='3.237.234.45', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

# Table creation

orders_sql = '''create table orders( order_id int not null, \
order_date date, order_status char(10), \
total_amount int, store_cd int, \
agent_id int );'''

order_item_sql = '''create table order_item ( order_item_id int not null, order_id int not null, \
order_item_details char(10), order_item_amount int, quantity int );'''

agent_sql = '''create table agent( agent_id int not null, agent_name char(50));'''

store_sql = '''create table store( store_cd int not null, store_name char(50), store_area char(20) );'''

drop_sql='''drop table orders;drop table order_item; drop table agent; drop table store;'''

cursor.execute(drop_sql);
cursor.execute(orders_sql);
cursor.execute(order_item_sql);
cursor.execute(agent_sql);
cursor.execute(store_sql);

#Insert the sql

with open('/home/order_header.csv','r') as f:
    next(f)
    cursor.copy_from(f,'orders',sep=',')

conn.commit()
#cursor.execute(sql2)

with open('/home/order_item.csv','r') as f:
    next(f)
    cursor.copy_from(f,'order_item',sep=',')

conn.commit()

with open('/home/agent.csv','r') as f:
    next(f)
    cursor.copy_from(f,'agent',sep=',')

conn.commit()

with open('/home/store.csv','r') as f:
    next(f)
    cursor.copy_from(f,'store',sep=',')

conn.commit()


# SQL SELECT QUERY
sql3 = '''select * from orders;'''
cursor.execute(sql3)
for i in cursor.fetchall():
	print(i)

#conn.commit()
conn.close()

