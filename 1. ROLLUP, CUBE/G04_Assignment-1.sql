Activity 1:
(1):
create table DIM_item
(
    id_item int primary key,
    itemName char(20),
    color char(10),
    price real
);

create table DIM_time
(
    id_time int primary key,
    realDate char(8),
    yearMonth char(8)
);

create table DIM_place
(
    id_place int primary key,
    shopName char(20),
    city char(10),
    country char(3)
);

create table FACT_sale
(
    id_sale char(5) primary key,
    id_item int, 
    id_place int,
    id_time int,
    FOREIGN KEY (id_item) REFERENCES DIM_item(id_item),
    FOREIGN KEY (id_place) REFERENCES DIM_place(id_place),
    FOREIGN KEY (id_time) REFERENCES DIM_time(id_time),
    total real
);

(2):
insert into DIM_item values(1,'laptop','red',300);
insert into DIM_item values(2,'ball','blue',500);
insert into DIM_item values(3,'mobile','orange',200);
insert into DIM_item values(4,'wallet','grey',150);
insert into DIM_item values(5,'bat','green',400);

insert into DIM_place values(11,'arya','pune','Ind');
insert into DIM_place values(12,'shree','mumbai','Ind');
insert into DIM_place values(13,'diablo','chicago','USA');
insert into DIM_place values(14,'safa','sangli','Ind');
insert into DIM_place values(15,'hamley','nagpur','Ind');

insert into DIM_time values(111,'1/1/2014','2014-FEB');
insert into DIM_time values(112,'5/2/2014','2014-FEB');
insert into DIM_time values(113,'7/3/2014','2014-MAR');
insert into DIM_time values(114,'3/4/2014','2014-APR');
insert into DIM_time values(115,'8/5/2014','2014-MAY');

insert into FACT_sale values('1121',1,15,111,5200);
insert into FACT_sale values('1122',2,11,112,1500);
insert into FACT_sale values('1123',3,14,113,5000);
insert into FACT_sale values('1124',4,13,114,1300);
insert into FACT_sale values('1125',5,12,115,2500);
insert into FACT_sale values('1126',4,11,111,3000);
insert into FACT_sale values('1127',3,12,112,3500);
insert into FACT_sale values('1128',5,13,113,2700);
insert into FACT_sale values('1129',2,14,114,1800);
insert into FACT_sale values('1130',1,15,115,10000);

Activity 2:
(1):
select id_item,id_place,sum(total) as TOTAL
from FACT_sale
GROUP BY ROLLUP (id_item,id_place)
order by id_item,id_place;

(2):
select B.itemName,C.shopName,sum(A.total) as TOTAL
from FACT_sale A,DIM_item B,DIM_place C
where A.id_item=B.id_item and A.id_place=C.id_place
GROUP BY ROLLUP (B.itemName,C.shopName)
order by B.itemName,C.shopName;

(3):
select B.itemName,C.city,D.yearMonth,sum(A.total) as TOTAL
from FACT_sale A,DIM_item B,DIM_place C,DIM_TIME D
where A.id_item=B.id_item and A.id_place=C.id_place and A.ID_TIME = D.ID_TIME
GROUP BY ROLLUP (B.itemName,C.city,D.yearMonth)
order by B.itemName,C.city,D.yearMonth;

(4):
select B.color,C.country,D.yearMonth,sum(A.total) as TOTAL
from FACT_sale A,DIM_item B,DIM_place C,DIM_TIME D
where A.id_item=B.id_item and A.id_place=C.id_place and A.ID_TIME = D.ID_TIME
GROUP BY ROLLUP (B.color,C.country,D.yearMonth)
order by B.color,C.country,D.yearMonth;

Activity 3:
(1):
select id_item,id_place,sum(total) as TOTAL
from FACT_sale
GROUP BY CUBE (id_item,id_place)
order by id_item,id_place;

(2):
select B.itemName,C.shopName,sum(A.total) as TOTAL
from FACT_sale A,DIM_item B,DIM_place C
where A.id_item=B.id_item and A.id_place=C.id_place
GROUP BY CUBE (B.itemName,C.shopName)
order by B.itemName,C.shopName;

(3):
select B.itemName,C.city,D.yearMonth,sum(A.total) as TOTAL
from FACT_sale A,DIM_item B,DIM_place C,DIM_TIME D
where A.id_item=B.id_item and A.id_place=C.id_place and A.ID_TIME = D.ID_TIME
GROUP BY CUBE (B.itemName,C.city,D.yearMonth)
order by B.itemName,C.city,D.yearMonth;

(4):
select B.color,C.country,D.yearMonth,sum(A.total) as TOTAL
from FACT_sale A,DIM_item B,DIM_place C,DIM_TIME D
where A.id_item=B.id_item and A.id_place=C.id_place and A.ID_TIME = D.ID_TIME
GROUP BY CUBE (B.color,C.country,D.yearMonth)
order by B.color,C.country,D.yearMonth;

