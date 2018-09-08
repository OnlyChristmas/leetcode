'''

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.


Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:



FirstName, LastName, City, State
'''


# Write your MySQL query statement below


# 复习 left join /right join / inner join 的知识
# 左连会读取左边表格的所有数据(右边表格没有补null); 右连恰恰相反 ; inner可以省略,是默认值,取两个表格所共有的部分
# 方法二比方法一更快一点,可能是不用检索对比列名?

# method one
# SELECT FirstName, LastName, City, State
# FROM Person
# LEFT JOIN Address
# USING(PersonId);


# method two
SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;
