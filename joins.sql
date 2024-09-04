create table Employee(
Id int Not null primary key,
Name varchar(50),
Gender varchar(50),
Salary int,
DepartmentID int
FOREIGN KEY (Departmentid) REFERENCES Department(Departmentid));

insert into Employee(Id,Name,Gender,Salary,DepartmentID)
VALUES(1,'Tom','male',4000,1),
(2,'Pam','Female',3000,3),
(3,'John','male',3500,1),
(4,'Sam','male',4500,2),
(5,'Todd','male',2800,2),
(6,'Ben','male',7000,1),
(7,'Sara','female',5500,1),
(8,'Valarie','female',5500,1),
(9,'James','male',6500,null),
(10,'Russell','male',8800,null);

create table Department(
DepartmentId int not null primary key,
DepartmentName varchar(50),
Location varchar(50),
DepartmentHead varchar(50));

insert into Department(DepartmentId,DepartmentName,Location,DepartmentHead)
VALUES(1,'IT','London','Rick'),
(2,'Payroll','Delhi','Ron'),
(3,'HR','New York','Christie'),
(4,'Other Department','Sydney','Cindrella');

SELECT Name,Gender,Salary,DepartmentName
FROM Employee
JOIN Department
ON Employee.DepartmentID=Department.DepartmentId;

SELECT Name,Gender,Salary,DepartmentName
FROM Employee
LEFT JOIN Department
ON Employee.DepartmentID=Department.DepartmentId;

SELECT Name,Gender,Salary,DepartmentName
FROM Employee
RIGHT JOIN Department
ON Employee.DepartmentID=Department.DepartmentId;

SELECT Name,Gender,Salary,DepartmentName
FROM Employee
FULL JOIN Department
ON Employee.DepartmentID=Department.DepartmentId;

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL
);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    ProductID INT NOT NULL,
    OrderDate DATE NOT NULL,
    Quantity INT NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


INSERT INTO Products (ProductID, ProductName, Category, Price, StockQuantity)
VALUES
(1, 'Laptop', 'Electronics', 75000.00, 10),
(2, 'Smartphone', 'Electronics', 25000.00, 25),
(3, 'Headphones', 'Accessories', 2000.00, 50),
(4, 'Desk Chair', 'Furniture', 5000.00, 15),
(5, 'Monitor', 'Electronics', 12000.00, 8);


INSERT INTO Orders (OrderID, ProductID, OrderDate, Quantity, TotalAmount)
VALUES
(1, 1, '2024-08-01', 2, 150000.00),
(2, 2, '2024-08-02', 3, 75000.00),
(3, 3, '2024-08-03', 5, 10000.00),
(4, 4, '2024-08-04', 1, 5000.00),
(5, 2, '2024-08-05', 1, 25000.00);

SELECT ProductName,Price,TotalAmount,StockQuantity
FROM Products
JOIN Orders
ON Products.ProductID=Orders.ProductID;

SELECT ProductName,Price,TotalAmount,StockQuantity
FROM Products
LEFT JOIN Orders
ON Products.ProductID=Orders.ProductID;

SELECT ProductName,Price,TotalAmount,StockQuantity
FROM Products
RIGHT JOIN Orders
ON Products.ProductID=Orders.ProductID;

SELECT ProductName,Price,TotalAmount,StockQuantity
FROM Products
FULL OUTER JOIN Orders
ON Products.ProductID=Orders.ProductID;

---retrieve total no of items sold and total sales amount for each product.
---display productname,total quantitysold, and totalsalesamount
SELECT p.ProductName, SUM(o.Quantity) AS TotalQuantitySold,
SUM(o.TotalAmount) AS TotalSalesAmount
FROM  Orders o
JOIN  Products p ON o.ProductID = p.ProductID
GROUP BY p.ProductName;

---2
SELECT p.ProductID,p.ProductName, p.Category
FROM Products p
left join Orders o
ON p.ProductID=o.ProductID
WHERE o.ProductID is null;

--3
SELECT o.orderID,p.ProductName, o.OrderDate,o.Quantity,o.TotalAmount
FROM Products p
INNER JOIN Orders o
ON p.ProductID=o.ProductID
WHERE OrderDate>'2024-08-02';

--4
SELECT top 3 p.productname,sum(o.Quantity) as totalquantitysold
FROM Products p 
INNER JOIN Orders o
ON p.ProductID=o.OrderID
GROUP BY p.ProductName
order by totalquantitysold DESC;

SELECT productName, Price,Category
from Products
where Category in ('Electronics','Furniture');

SELECT DISTINCT Category
from Products;


SELECT productName, Price,Category
from Products
where Category='Electronics' and Price>20000;


SELECT productName,Category,StockQuantity
from Products
where Category ='Furniture' or StockQuantity<10;

SELECT productName, Price,Category
from Products
where Price between 5000 and 20000;

select distinct p.productName,p.category,p.price,o.orderDate
From Products as p
Inner join Orders as o
ON p.ProductID=o.ProductID
where p.Category in ('furniture','electronics')
and o.OrderDate>'2024-01-01'
and p.Price between 5000 and 50000
and p.ProductName like 's%';

select p1.productName as product1,p2.productName as product2,p1.category
from products p1
inner join Products p2 on p1.Category=p2.Category and p1.ProductID <> p2.ProductID;

SELECT p.category, SUM(o.Quantity) AS TotalQuantity
from Products p
inner join Orders o 
ON p.ProductID=o.ProductID
group by p.Category
having SUM(o.Quantity) >3;

---1
select sum(o.quantity) as totalproducts , p.Category
from orders o
inner join orders 
ON o.ProductID =p.ProductID
group by GROUPING sets((p.category),());

---2
select productName
from Products 
where ProductID in (
     select productID
	 from Orders
	 group by ProductID
	 having count(OrderID)>5);

---3
select productName
from Products p
where exists (
     select 1
	 from Orders o
	 where p.ProductID=o.ProductID);

---4
select ProductName
from Products
where Price> all
(select Price
from Products
where Category= 'accessories');

---5
select ProductName
from Products
where Price> any
(select Price
from Products
where Category= 'accessories');

select (DATEDIFF(month,'2002-09-25',GETDATE()));

---23.08.2024
select productName , price, round(price,2) as roundprice
from Products;

select productName , price, ceiling(price) as ceilingprice
from Products;

select productName , price, floor(price) as floorprice
from Products;

select productName , price, sqrt(price) as sqrtprice
from Products;

select productName , price, power(price,2) as priceSquared
from Products;

select productName , price, price % 5 as moduloprice
from Products;

select abs(Max(Price)-Min(Price)) as priceDifference
from Products;

select productName , price, round(rand()*100,2) as randomPErcentage
from Products;

select productName , price, log(price) as logarithmicprice
from Products;

select productName , price as originalPrice,
(price*0.85) as discountedPrice,
round(price*0.85,2) as roundedDecimalPrice,
CEILING(price*0.85) as ceilingPrice,
FLOOR(price*0.85) as floorPrice
from Products;

---Exercises
---1
select sum(TotalAmount) as TotalAMountEarned
from Orders
group by CustomerID;

---2
select sum(TotalAmount) as TotalAMountEarned
from Orders
group by CustomerID
having sum(TotalAmount)>1000;

---3
select count(ProductID) as ProductCounted, Category
from Products
group by category
having COUNT(productID)>5;

---4
select categoryID,SupplierID,
COUNT(ProductID) as CountedProduct
from Products
group by CategoryID,SupplierID;

---5
SELECT ProductID,CustomerID,
SUM(SaleAmount) AS TotalSaleAmount,
NULL AS OverallTotalAmount
FROM Sales
GROUP BY ProductID, CustomerID
UNION ALL
SELECT NULL AS ProductID,NULL AS CustomerID,
SUM(SaleAmount) AS TotalSaleAmount,
SUM(SaleAmount) AS OverallTotalAmount
FROM Sales;

---stored procedures
CREATE PROCEDURE GetAllProducts
as 
begin
  select * from Products
  select * from Orders;
end;
exec getAllProducts;


---stored procedure with parameter
CREATE PROCEDURE GetProductID
  @productID int
as 
begin
  select * from Products
  where ProductID=@productID
end;
exec GetProductID @productID =1
exec GetProductID @productID =3

---2 params
CREATE PROCEDURE GetProductIByCategoryandPrice
  @category varchar(50),
  @MinPrice decimal(10,2)
as 
begin
  select * from Products
  where Category=@category
  and Price>=@MinPrice;
end;
exec GetProductIByCategoryandPrice @Category ='Electronics', @MinPrice=500.00;

---output
CREATE PROCEDURE GetTotal
  @category int,
  @TotalProducts int output
as 
begin
  select TotalProducts= count(*) from Products
  where category=@category;
end;
DECLARE @Total INT;
EXEC GetTotal @Category = 'Electronics', @TotalProducts = @Total OUTPUT;
SELECT @Total AS TotalProductsInCategory;

---TRANSACTIONS
CREATE PROCEDURE Processorder
   @ProductID INT,
   @Quantity INT,
   @OrderDate DATE
AS
BEGIN
   BEGIN TRANSACTION;
      BEGIN TRY
          INSERT INTO Orders (ProductID, Quantity, OrderDate) 
		  VALUES (@ProductID, @Quantity, @OrderDate);

          UPDATE Products
          SET StockQuantity = StockQuantity @Quantity 
		  WHERE ProductID = @ProductID;

          COMMIT TRANSACTION;
      END TRY
      BEGIN CATCH
        ROLLBACK TRANSACTION;
           ---You can handle errors here, such as logging or returning an error message
      THROW;
      END CATCH;
END;

---IF-ELSE
CREATE PROCEDURE AdjustStock
	@ProductID INT,
	@Adjustment INT
AS
BEGIN
  IF @Adjustment > 0
	BEGIN
     ---Add to stock
		UPDATE Products
		SET StockQuantity = StockQuantity + @Adjustment 
		WHERE ProductID = @ProductID;
	END
  ELSE IF @Adjustment < 0
	BEGIN

     ---Subtract from stock
		UPDATE Products
		SET StockQuantity = StockQuantity + @Adjustment
		WHERE ProductID = @ProductID;
	END
END;
EXEC AdjustStock @ProductID = 1, @Adjustment = 5;
---Increase stock by 5 Decrease stock by 3
EXEC AdjustStock @ProductID = 1, @Adjustment = -3