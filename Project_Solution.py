# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:47:30 2022

@author: Shraddha 
"""


"""
Usecase-1 Load all three csv datasets in Pandas Data frames and display first 5 records.
"""
# first importing pandas
 
import pandas as pd

# Reading customers dataset and giving names to columns saving dataframe in variable named customers
# col_names list contains list of column names
col_names = ['custno', 'firstname', 'lastname', 'gender', 'age', 'profession', 'contactNo', 'emailId', 'city', 'state', 'isActive', 'createdDate', 'UpdatedDate']
customers = pd.read_csv("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/CSV_s1/customers.csv", names = col_names)


# Reading products dataset and giving names to columns saving dataframe in variable named products
# col_names list contains list of column names
col_names = ['productno', 'productName', 'Description', 'isActive', 'createdDate', 'UpdatedDate']
products = pd.read_csv("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/CSV_s1/products.csv", names = col_names)


# Reading transaction dataset and giving names to columns saving dataframe in variable named trans
# col_names list contains list of column names
col_names = ['txnno', 'txndate', 'custno', 'amount', 'productno', 'spendby']
trans = pd.read_csv("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/CSV_s1/transactions.csv", names = col_names)

# printing first  five records from each dataframe to understand what kind of data is in dataframe

print("First 5 Records :\n")
print("Customer".center(78, "*"))
print(customers.head())
print("Products".center(78, "*"))
print(products.head())
print("Transaction".center(78, "*"))
print(trans.head())


"""
Usecase-2 Display only those customers from CSV_s1, who purchased more than 3 products
"""

mydata = pd.merge(customers,trans, on = 'custno', how = 'inner')
prod1= mydata[['custno','productno']].groupby('custno').count()
prod2=prod1[prod1['productno']>3]

result = pd.merge(customers,prod2, how = 'inner', on = 'custno')
result.drop('productno',axis=1,inplace=True)

print("Customers information who purchased more than 3 products")
print(result)


"""
Usecase-3 Display top 5 most demanded products from CSV_s1
"""

sale = trans[['txnno','productno']].groupby('productno').count()
top5 = sale[sale['txnno']>=4].sort_values( by = 'txnno',ascending=False).head()
top5.drop('txnno', axis =1, inplace= True)

top_5_products = pd.merge(top5, products, how = 'inner', on = 'productno')
print("Top 5 most demanded products ")
print(top_5_products)


"""
Usecase-4 Display top 5 transactions amount from CSV_s1
"""
print("top 5 transactions amount")
print(trans["amount"].sort_values(ascending = False).head())


"""
Usecase-5 Display distinct professions from CSV_s1
"""

print("Distinct professions")
print(customers.profession.unique())


"""
Usecase-6 Display highest age in CSV_s1 customer’s dataset
"""

print("Highest age in customer's dataset: ")
print(customers['age'].max())


"""
Usecase-7 Display custno, gender, age, profession, contactno, productno, productName,
txndate, spendby, amount from CSV_s1 for custno = 923
"""

#merging 3 dataframes
merged = pd.merge(pd.merge(customers,trans, on = 'custno', how = 'inner'),products, on = 'productno', how = 'inner')

print("information of customer whose custno = 923 ")
print(merged[['custno','gender','age','profession','contactNo','productno','productName','txndate',
             'spendby','amount']][merged['custno']==923])


"""
Usecase-8 Load all three PSV (pipe separated values) dataset in Pandas Data frames and
display first 5 records.
"""


# Reading customers dataset and giving names to columns saving dataframe in variable named customers
# col_names list contains list of column names
col_names = ['custno', 'firstname', 'lastname', 'gender', 'age', 'profession', 'contactNo', 'emailId', 'city', 'state', 'isActive', 'createdDate', 'UpdatedDate']
customers = pd.read_csv("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/PSV_s2/customers.txt",names = col_names, sep='|')

# Displaying first 5 records
print(customers.head())


# Reading products dataset and giving names to columns saving dataframe in variable named products
# col_names list contains list of column names
col_names = ['productno', 'productName', 'Description', 'isActive', 'createdDate', 'UpdatedDate']
products = pd.read_csv("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/PSV_s2/products.txt", names = col_names, sep='|')

# Displaying first 5 records
print(products.head())

# Reading transaction dataset and giving names to columns saving dataframe in variable named trans
# col_names list contains list of column names
col_names = ['txnno', 'txndate', 'custno', 'amount', 'productno', 'spendby']
trans = pd.read_csv("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/PSV_s2/transactions.txt", names = col_names, sep='|')

# Displaying first 5 records
print(trans.head())


"""
Usecase-9 Load all three JSON datasets in Pandas Data frames and display first 5 records.
"""

# Reading customers dataset 
customers = pd.read_json("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/JSON_s3/customers.json", lines=True)

# Displying first 5 records
print(customers.head())


# Reading products dataset
products = pd.read_json("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/JSON_s3/products.json", lines=True)

# displaying first 5 records
print(products.head())


# Reading transactions dataset
trans = pd.read_json("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/JSON_s3/transactions.json", lines=True)

# Displaying first 5 records
print(trans.head())


"""
Usecase-10 Load all three XML datasets in Pandas Data frames and display first 5 records
"""

import pandas as pd

# Reading customers dataset

customers = pd.read_xml("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/XML_s4/customers.xml")

# Displaying first 5 records
print(customers.head())

# Reading products dataset
products = pd.read_xml("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/XML_s4/products.xml")

# Displaying first 5 records
print(products.head())

# Reading transactions dataset
trans = pd.read_xml("https://raw.githubusercontent.com/shraddha-pawar36/Data-Analysis-Project/main/XML_s4/transactions.xml")

# Displaying first 5 records
print(trans.head())

