create table CustomerDW
( 
    customer_id integer primary key,
    customer_name varchar(20),
    city_id integer,
    First_order_date date
);

insert into CustomerDW values(1001,'Ritik',10,'3-FEB-2014');
insert into CustomerDW values(1002,'Abhinav',20,'21-AUG-2011');
insert into CustomerDW values(1003,'Himanshu',11,'27-JUN-2018');
insert into CustomerDW values(1004,'Shailesh',20,'26-DEC-2001');
insert into CustomerDW values(1005,'Ankur',14,'16-DEC-2017');
insert into CustomerDW values(1006,'Ajay',24,'11-NOV-2012');


create table Walkin_customers
( 
    customer_id integer,
    tourism_guide integer,
    walkin_time TIMESTAMP,
    foreign key(customer_id) REFERENCES CustomerDW(customer_id)
);

insert into Walkin_customers values(1001,01,'1-JUN-2017');
insert into Walkin_customers values(1001,11,'6-JUL-2018');
insert into Walkin_customers values(1002,02,'18-FEB-2011');
insert into Walkin_customers values(1004,01,'23-NOV-2019');
insert into Walkin_customers values(1003,03,'9-DEC-2006');


create table Mail_order_customers 
(
    customer_id integer,
    post_address varchar(20),
    Mail_order_time TIMESTAMP,
    foreign key(customer_id) REFERENCES CustomerDW(customer_id)
);

insert into Mail_order_customers values(1002,'Sangli','12-FEB-2015');
insert into Mail_order_customers values(1001,'Pune','10-DEC-2012');
insert into Mail_order_customers values(1004,'Kolhapur','12-JAN-2006');
insert into Mail_order_customers values(1003,'Nagpur','4-NOV-2018');

/*SALES DATABASE*/

create table Headqarters 
(
    City_id integer primary key,
    City_name varchar(20),
    Headquarter_addr varchar(20),
    State varchar(20),
    Headqarters_time TIMESTAMP
);

insert into Headqarters values(100,'Sangli','m.g.nagar','Maharashtra','29-JUL-2001');
insert into Headqarters values(101,'Pune','SP road','Maharashtra','12-MAR-2002');
insert into Headqarters values(102,'Kolhapur','vishrambagh','Maharashtra','20-DEC-2003');
insert into Headqarters values(20,'Nagpur','MS corner','Maharashtra','10-APR-2001');



create table Stores 
(
    Store_id integer primary key,
    City_id integer,
    phone integer,
    Stores_time TIMESTAMP,
    foreign key (City_id) references  Headqarters(City_id)
 );
 
 

insert into Stores values(9000,102,9172162833,'11-JUL-2008');
insert into Stores values(9001,101,8830448411,'22-MAY-2007');
insert into Stores values(9002,100,9423825515,'14-JAN-2006');

create table Items_2 
(
    Item_id integer primary key,
    Description varchar(20),
    item_size integer,
    Weight real,
    Unit_price real,
    Items_time TIMESTAMP
);

insert into Items_2 values(1,'Mouse',10*40,10,900,'23-JUL-2010');
insert into Items_2 values(2,'Books',10*10,12,499,'7-DEC-2008');
insert into Items_2 values(3,'Bottle',5*50,4,50,'28-MAY-2009');
insert into Items_2 values(4,'Mobile',5*5,18,40000,'4-APR-2011');


create table Stored_items 
(
    Store_id integer,
    Item_id integer,
    Quantity_held integer,
    Stored_items_time TIMESTAMP,
    primary key(Store_id,Item_id),
    foreign key (Store_id) references  Stores(Store_id),
    foreign key (Item_id) references  Items_2(Item_id)
);
insert into Stored_items values(9000,1,20,'23-JUL-2010');
insert into Stored_items values(9001,2,21,'7-DEC-2008');
insert into Stored_items values(9002,3,90,'28-MAY-2009');
insert into Stored_items values(9000,4,17,'4-APR-2011');


create table Orders
(
    Order_no integer primary key,
    Order_date date,
    Customer_id integer
);
insert into Orders values(2000,'2-FEB-2002',1001);
insert into Orders values(2001,'20-JUL-2002',1004);
insert into Orders values(2002,'15-JAN-2009',1002);
insert into Orders values(2003,'17-JUL-2002',1004);
insert into Orders values(2004,'9-NOV-2003',1003);



create table Ordered_item 
(
    Order_no integer,
    Item_id integer,
    Quantity_ordered integer,
    Ordered_price real,
    Orederd_item_time TIMESTAMP,
    primary key(Order_no,Item_id),
    foreign key (Order_no) references  Orders(Order_no),
    foreign key (Item_id) references  Items_2(Item_id)
);
/*900 499 50 40000*/
insert into Ordered_item values(2000,1,2,2000,'2-JAN-2009');
insert into Ordered_item values(2001,3,3,180,'18-JUL-2009');
insert into Ordered_item values(2000,2,1,600,'26-AUG-2009');
insert into Ordered_item values(2002,4,3,41000,'9-SEP-2009');
insert into Ordered_item values(2003,2,3,1600,'21-APR-2010');
insert into Ordered_item values(2004,3,2,110,'16-OCT-2010');

/*
1. Find all the stores along with city, state, phone, description, size, weight and
unit price that hold a particular item of stock.
*/

select h.city_name,state,phone,description,item_size,weight,Unit_price
from Stored_items,Items_2,Headqarters h ,Stores s
where Stored_items.item_id=Items_2.item_id and s.city_id= h.city_id and Stored_items.store_id= s.store_id;

/*
2. Find all the orders along with customer name and order date that can be
fulfilled by a given store.
*/
select unique customer_name,Order_date
from CustomerDW, orders,stores ,ordered_item o, stored_items s
where orders.order_no=o.order_no and s.store_id=stores.store_id and CustomerDW.customer_id=orders.customer_id and s.Quantity_held>o.Quantity_ordered;

/*
3. Find all stores along with city name and phone that hold items ordered by
given customer.
*/

select stores.store_id,city_name,phone
from stores,Headqarters h,orders,ordered_item o, stored_items s
where orders.order_no=o.order_no and s.store_id=stores.store_id and o.item_id=s.item_id and h.city_id= stores.city_id;

/*
4. Find the headquarter address along with city and state of all stores that hold
stocks of an item above a particular level.
*/
select Headquarter_addr,city_name, state
from Headqarters h,stores, stored_items s
where stores.city_id=h.city_id and stores.store_id= s.store_id and s.Quantity_held>3;

/*
5. For each customer order, show the items ordered along with description, store
id and city name and the stores that hold the items.
*/
select unique o.item_id,Description,s.store_id,city_name
from Items_2,stores,stored_items s,orders,ordered_item o,Headqarters h,CustomerDW
where h.CITY_ID=STOREs.CITY_ID
and ITEMS_2.ITEM_ID=o.ITEM_ID
and o.ITEM_ID=s.ITEM_ID and stores.store_id= s.store_id;

/*
6. Find the city and the state in which a given customer lives.
*/
select Customer_name,City_name,HEADQARTERS.State 
from CustomerDW, HEADQARTERS
where HEADQARTERS.city_id=CustomerDW.CITY_ID and CustomerDW.CUSTOMER_ID=1002;

/*
7. Find the stock level of a particular item in all stores in a particular city.
*/

select Customer_name,City_name,HEADQARTERS.State 
from CustomerDW, HEADQARTERS
where HEADQARTERS.city_id=CustomerDW.CITY_ID and CustomerDW.CUSTOMER_ID=1002;

/*
8. Find the items, quantity ordered, customer, store and city of an order.
*/
select unique Customer_name,city_id,Quantity_ordered,Description,s.store_id
from Orders,CustomerDW,Ordered_item,Items_2, Stored_items s
where Orders.Order_no = Ordered_item.Order_no and
 CustomerDW.customer_id=Orders.customer_id and Ordered_item.item_id= Items_2.item_id and s.item_id= Items_2.item_id;

/*
9. Find the walk in customers, mail order customers and dual customers (both
walk-in and mail order).
*/
(select customer_id from WALKIN_CUSTOMERS) union (select customer_id from Mail_order_customers);
