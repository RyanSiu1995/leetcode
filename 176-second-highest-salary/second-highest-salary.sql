-- Write your PostgreSQL query statement below
WITH
    TopSalary AS (
        SELECT MAX(salary) as salary
        FROM Employee
    )
SELECT MAX(Employee.salary) AS SecondHighestSalary
FROM Employee
RIGHT JOIN TopSalary
ON Employee.salary != TopSalary.salary