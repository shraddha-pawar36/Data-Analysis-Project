create table test_customers(custno int PRIMARY KEY,
 firstname varchar(20), lastname varchar(20),gender varchar(20), 
age int,profession varchar(20),contactNo long,
emailId varchar(20),
city varchar(20), state varchar(20),
isActive char(1),createdDate datetime, UpdatedDate datetime);


create table test_products(productno int PRIMARY KEY, productName varchar(20), Description varchar(20), isActive char(1),createdDate datetime, UpdatedDate datetime);

create table test_transactions(txnno int PRIMARY KEY, txndate datetime,
custno int, amount double,productno int, spendby varchar(10),
FOREIGN KEY (custno) REFERENCES test_customers(custno),
FOREIGN KEY (productno) REFERENCES test_products(productno) );

select * from tab; 









