create table Employee(
EmployeeID int Primary key,
FirstName varchar(100),
LastName varchar(100),
Position varchar(100),
Department varchar(100),
HireDate varchar(100));

insert into Employee(EmployeeID,FirstName,LastName,Position,Department,HireDate)
VALUES(1,'Amit','Sharma','Software Engineer','IT','2022-01-15'),
(2,'Priya','Mehta','Project Manager','Operations','2023-02-20'),
(3,'Raj','Patel','Business Analyst','Finance','2021-06-30'),
(4,'Sunita','Verma','HR Specialist','HR','2019-08-12'),
(5,'Vikram','Rao','Software Engineer','IT','2021-03-18'),
(6,'Anjali','Nair','HR Manager','HR','2019-08-12'),
(7,'Rohan','Desai','Finance Manager','Finance','2022-11-25'),
(8,'Sneha','Kumar','Operations Coordinator','Operations','2023-07-02'),
(9,'Deepak','Singh','Data Scientist','IT','2022-08-05'),
(10,'Neha','Gupta','Business Analyst','Finance','2020-10-10');

---Exercises
---1
SELECT EmployeeID, FirstName, LastName,Position,Department
FROM Employee
Where Department='IT';

---2
SELECT EmployeeID, FirstName, LastName,Position,Department
FROM Employee
Where HireDate>'2022-01-01';

---3
SELECT EmployeeID, FirstName, LastName,Position,Department
FROM Employee
Where Department='HR' or Department='Finance';

---4
SELECT EmployeeID, FirstName, LastName,Position,Department
FROM Employee
Where Position='Software Engineer' AND HireDate>'2021-01-01';

---5
SELECT EmployeeID, FirstName, LastName,Position,Department
FROM Employee
Where LastName like 'S%';

---6
SELECT EmployeeID, FirstName, LastName,Position,Department
FROM Employee
Where FirstName like '%n%';

---7
Select Count(EmployeeID) AS TotalNoOfEmployees
FROM Employee;

---8
Select Top 1 HireDate AS EarlistHireDate
From Employee
Order by HireDate ASC;

