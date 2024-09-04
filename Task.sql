CREATE TABLE Orders2(
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderAmount DECIMAL(10, 2),
    OrderDate DATE
);
 
INSERT INTO Orders2(OrderID, CustomerID, OrderAmount, OrderDate)
VALUES 
(1, 1, 500.00, '2024-01-15'),
(2, 2, 700.00, '2024-01-16'),
(3, 1, 300.00, '2024-01-17'),
(4, 3, 1200.00, '2024-02-01'),
(5, 2, 900.00, '2024-02-03');

CREATE TABLE Customers1 (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15),
	city VARCHAR(50)
);

INSERT INTO Customers1(CustomerID, FirstName, LastName, Email, PhoneNumber,city) VALUES
(1, 'amit', 'sharma', 'amit.sharma@example.com', '9876543210','chennai'),
(2, 'priya', 'mehta', 'priya.mehta@example.com', '8765432109','banglore'),
(3, 'rohit', 'kumar', 'rohit.kumar@example.com', '7654321098','coimbatore'),
(4, 'neha', 'verma', 'neha.verma@example.com', '6543210987','chennai'),
(5, 'siddharth', 'singh', 'siddharth.singh@example.com', '5432109876','chennai'),
(6, 'asha', 'rao', 'asha.rao@example.com', '4321098765','banglore');

---- Task:1 Join the `Orders` and `Customers` tables 
----to find the total order amount per customer and filter out customers who have spent less than $1,000.
SELECT c.CustomerID, c.FirstName, SUM(o.OrderAmount) AS TotalAmount
FROM Customers1 c
JOIN Orders2 o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName
HAVING SUM(o.OrderAmount) >= 1000;

---- Task:2 Create a cumulative sum of the `OrderAmount` for each customer 
---to track the running total of how much each customer has spent.
SELECT CustomerID, OrderID, OrderAmount,
SUM(OrderAmount) OVER (PARTITION BY CustomerID ORDER BY OrderDate) 
AS RunningTotal FROM Orders2
order by CustomerID;

---- Task:3 Rank the customers based on the total amount they have spent, partitioned by city.
SELECT CustomerID, TotalAmount, 
RANK() OVER (ORDER BY TotalAmount DESC) AS CustomerRank FROM (
SELECT c.CustomerID, SUM (OrderAmount) AS TotalAmount,city
FROM Customers1 c
INNER JOIN Orders2 o
on c.CustomerID =o.CustomerID
GROUP BY c.CustomerID,c.city
) AS Data;

---- Task:4 Calculate the total amount of all orders (overall total) and 
----the percentage each customer's total spending contributes to the overall total.
WITH CustomerTotals AS (
SELECT c.CustomerID, SUM(o.OrderAmount) AS   TotalSpent
FROM Orders2 o
Inner Join Customers1 c ON o.CustomerID = c.CustomerID
GROUP BY c.CustomerID
)
SELECT CustomerID, TotalSpent,
TotalSpent * 100.0 / SUM(TotalSpent) OVER () AS PercentageOfTotal
FROM CustomerTotals;

--- Task:5 Rank all customers based on the total amount they have spent, without partitioning.
SELECT c.CustomerID, c.FirstName, SUM(o.OrderAmount) AS TotalSpent,
RANK() OVER (ORDER BY SUM(o.TotalAmount) DESC) AS CustomerRank
FROM Orders2 o
JOIN Customers1 c ON o.CustomerID = c.CustomerID
GROUP BY c.CustomerID, c.FirstName;

---Task:6 Write a query that joins the `Orders` and `Customers` tables, calculates the average order amount for each city, 
---and orders the results by the average amount in descending order.
SELECT c.City, AVG(o.OrderAmount) AS AvgAmount
FROM Orders2 o
INNER JOIN Customers1 c ON o.CustomerID = c.CustomerID
GROUP BY c.City
ORDER BY AvgAmount DESC;	

---Task:7 Write a query to find the top 3 customers who have spent the most, using `ORDER BY` and `LIMIT`.
SELECT TOP 3 c.CustomerID, SUM(o.OrderAmount) AS AmountSpentMost
FROM Customers1 c
INNER JOIN Orders2 o
ON c.CustomerID = o.CustomerID
Group by c.CustomerID
Order by SUM(o.OrderAmount) DESC;

---Task:8 Write a query that groups orders by year (using OrderDate),
--calculates the total amount of orders for each year, and orders the results by year.
select year(o.orderdate) as orderyear, 
sum(o.orderamount) as yearlytotal
from Orders2 o
group by year(o.orderdate)
order by orderyear;

---Task:9 Write a query that ranks customers by their total spending, but only for customers located in "Mumbai".
---The rank should reset for each customer in "Mumbai".
select c.customerid, c.firstname, c.lastname, 
sum(o.orderamount) as totalspent,
rank() over (order by sum(o.orderamount) desc) as chennairank
from Customers1 c
join Orders2 o on c.customerid = o.customerid
where c.city = 'chennai'
group by c.customerid, c.firstname, c.lastname;

---- Task: Write a query that calculates each customer's total order amount and 
---compares it to the average order amount for all customers.
with customertotals as (
select c.customerid, c.firstname, c.lastname, 
sum(o.orderamount) as totalspent
from Customers1 c
join Orders2 o on c.customerid = o.customerid
group by c.customerid, c.firstname, c.lastname)
select customerid, firstname, lastname, totalspent,
avg(totalspent) over () as avgtotalspent,
totalspent - avg(totalspent) over ()as differencefromaverage
from customertotals;

