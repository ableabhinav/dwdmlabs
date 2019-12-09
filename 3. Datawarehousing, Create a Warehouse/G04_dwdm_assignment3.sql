Create table DimCustomer
(
CustomerID int primary key,
CustomerAltID varchar(10) not null,
CustomerName varchar(50),
Gender varchar(20)
);

Insert into DimCustomer values(1,'IMI-001','Henry Ford','M');
Insert into DimCustomer values(2,'IMI-002','Bill Gates','M');
Insert into DimCustomer values(3,'IMI-003','Muskan Shaikh','F');
Insert into DimCustomer values(4,'IMI-004','Richard Thrubin','M');
Insert into DimCustomer values(5,'IMI-005','Emma Wattson','F');

Create table DimProduct
(
ProductKey int primary key,
ProductAltKey varchar(10)not null,
ProductName varchar(100),
ProductActualCost int,
ProductSalesCost int
)

Insert into DimProduct values (11,'ITM-001','Wheat Floor 1kg',5.50,6.50);
Insert into DimProduct values (12,'ITM-002','Rice Grains 1kg',22.50,24);
Insert into DimProduct values (13,'ITM-003','SunFlower Oil 1 ltr',42,43.5);
Insert into DimProduct values (14,'ITM-004','Nirma Soap',18,20);
Insert into DimProduct values (15,'ITM-005','Arial Washing Powder 1kg',135,139);

Create table DimStores
(
StoreID int primary key,
StoreAltID varchar(10)not null,
StoreName varchar(100),
StoreLocation varchar(100),
City varchar(100),
State varchar(100),
Country varchar(100)
)

Insert into DimStores values(111,'LOC-A1','X-Mart','S.P. RingRoad','Ahmedabad','Guj','India');
Insert into DimStores values(112,'LOC-A2','X-Mart','Maninagar','Ahmedabad','Guj','India');
Insert into DimStores values(113,'LOC-A3','X-Mart','Sivranjani','Ahmedabad','Guj','India');

Create table DimSalesPerson
(
SalesPersonID int primary key,
SalesPersonAltID varchar(10)not null,
SalesPersonName varchar(100),
StoreID int,
City varchar(100),
State varchar(100),
Country varchar(100)
)

Insert into DimSalesPerson values (1111,'SP-DMSPR1','Ashish',1,'Ahmedabad','Guj','India');
Insert into DimSalesPerson values (1112,'SP-DMSPR2','Ketan',1,'Ahmedabad','Guj','India');
Insert into DimSalesPerson values (1113,'SP-DMNGR1','Srinivas',2,'Ahmedabad','Guj','India');
Insert into DimSalesPerson values (1114,'SP-DMNGR2','Saad',2,'Ahmedabad','Guj','India');
Insert into DimSalesPerson values (1115,'SP-DMSVR1','Jasmin',3,'Ahmedabad','Guj','India');
Insert into DimSalesPerson values (1116,'SP-DMSVR2','Jacob',3,'Ahmedabad','Guj','India');

CREATE TABLE DimTime(
	TimeKey int NOT NULL,
	TimeAltKey int NOT NULL,
	Time30 varchar(8) NOT NULL,
	Hour30 int NOT NULL,
	MinuteNumber int NOT NULL,
	SecondNumber int NOT NULL,
	TimeInSecond int NOT NULL,
	HourlyBucket varchar(15)not null,
	DayTimeBucketGroupKey int not null,
	DayTimeBucket varchar(100) not null
);


INSERT INTO DimTime (TimeKey,TimeAltKey, Time30,Hour30,MinuteNumber, SecondNumber, TimeInSecond,HourlyBucket, DayTimeBucketGroupKey,DayTimeBucket)
values(1,30000,'3:00:00',3,00,00,10800,'3:00-3:59',1,'Early Morning(03:00 AM To 6:59 AM)');

INSERT INTO DimTime (TimeKey,TimeAltKey, Time30,Hour30,MinuteNumber, SecondNumber, TimeInSecond,HourlyBucket, DayTimeBucketGroupKey,DayTimeBucket)
values(2,121000,'12:10:00',12,10,00,43800,'12:00-12:59',4,'Lunch (12:00 PM To 13:59 PM)');


Create Table FactProductSales
(
TransactionId int primary key,
SalesInvoiceNumber int not null,
SalesDateKey int,
SalesTimeKey int,
SalesTimeAltKey int,
StoreID int not null,
CustomerID int not null,
ProductID int not null,
SalesPersonID int not null,
Quantity float,
SalesTotalCost int,
ProductActualCost int,
Deviation float
)

AlTER TABLE FactProductSales ADD
FOREIGN KEY(StoreID)REFERENCES DimStores(StoreID);
AlTER TABLE FactProductSales ADD 
FOREIGN KEY (CustomerID)REFERENCES Dimcustomer(CustomerID);
AlTER TABLE FactProductSales ADD 
FOREIGN KEY (ProductID)REFERENCES Dimproduct(ProductKey);
AlTER TABLE FactProductSales ADD 
FOREIGN KEY (SalesPersonID)REFERENCES Dimsalesperson(SalesPersonID);
--AlTER TABLE FactProductSales ADD 
--FOREIGN KEY (SalesTimeKey)REFERENCES DimDate(TimeKey);

INSERT INTO FactProductSales values(11111,20130101,44347,121907,1219070,111,1,11,1111,20,11000,10000,1000);
INSERT INTO FactProductSales values(11112,20130102,44348,121908,1219080,112,2,12,1112,30,12000,10000,2000);