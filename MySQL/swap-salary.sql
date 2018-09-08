'''

Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a single update query and no intermediate temp table.
For example:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
After running your query, the above salary table should have the following rows:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |

'''


# Write your MySQL query statement below

# method one      CASE when  ...  then ...  语句的复习
# UPDATE salary
# SET sex = (CASE when sex='m' then 'f' else 'm' end)



# method two      IF(expr1,expr2,expr3) 语句的复习. 如果 expr1 = true ,返回 expr2 , 否则返回 expr3
UPDATE salary
SET sex = IF(sex = 'm', 'f', 'm')
