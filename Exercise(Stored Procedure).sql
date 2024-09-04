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

--- 6.stored procedure with insert operation
CREATE PROCEDURE InsertValues
  @productID int,
  @ProductName varchar(50),
  @Category varchar(50),
  @Price decimal(10,2),
  @StockQuantity int
as 
begin
  insert into Products(ProductID,ProductName,Category,Price,StockQuantity)
  Values(@productID,@ProductName,@Category,@Price,@StockQuantity);
end;
exec InsertValues @productID =6,@productName='JoyStick',@Category='Electronics',@Price=7000.00,@StockQuantity=9;

---7.stored procedure with update operation
CREATE PROCEDURE UpdateValues1
  @productID int,
  @StockQuantity int
as 
begin
  update Products
  set StockQuantity=@StockQuantity
  where ProductID=@productID
end;
exec UpdateValues1 @productID =6,@StockQuantity=5;

---8.stored procedure with delete operation
CREATE PROCEDURE DeleteValues
  @productID int
AS
BEGIN
  DELETE from Products
  where ProductID=@productID;
END;
exec DeleteValues @productID=6;

---9
---Retrieve all products from the Products table that belong to the category 'Electronics' and have a price greater than 500.
SELECT * FROM Products
WHERE Category ='Electronics' and Price >500;

---10
---Calculate the total quantity of products sold from the Orders table.
SELECT sum(Quantity) AS TotalQuantity
FROM Products

---11
---Calculate the total revenue generated for each product in the Orders table.
SELECT Sum(Amount) AS totalAmount, ProductID, Category
FROM Products
Group by ProductID;

---12
---Write a query that uses WHERE, GROUP BY, HAVING, and ORDER BY clauses and explain the order of execution.
SELECT ProductID, sum(Price)AS TotalRevenue
From Products
Where Price >10000              -- 1. Filter rows before grouping
GROUP BY ProductID              -- 2. Group rows by ProductID
Having TotalRevenue > 20000     -- 3. Filter groups based on aggregate function
ORDER BY TotalRevenue DESC;     -- 4. Sort the results

---13
---Write a query that corrects a violation of using non-aggregated columns without grouping them.
SELECT ProductID, SUM(TotalAmount) AS TotalRevenue
FROM Orders
GROUP BY ProductID;

---14
---Retrieve all customers who have placed more than 5 orders using GROUP BY and HAVING clauses.
SELECT CustomerID,count(OrderID)
FROM Orders
GROUP BY CustomerID
having count(orderID) > 5;

---15
---Create a stored procedure named GetAllCustomers that retrieves all customer details from the Customers table.
CREATE PROCEDURE GetAllCustomers
as 
begin
  select * from Customers
end;
exec GetAllCustomers;

---16
---Create a stored procedure named GetOrderDetailsByOrderID that accepts an OrderID as a parameter and
---retrieves the order details for that specific order.
CREATE PROCEDURE GetOrderDetailsByOrderID
     @OrderID INT
AS
BEGIN
   SELECT * FROM Orders
   WHERE OrderID =@OrderID;
END;
EXEC GetOrderDetailsByOrderID @OrderID =2;

---17
---Create a stored procedure named GetProductsByCategoryAndPrice that accepts a product Category and 
---a minimum Price as input parameters and retrieves all products that meet the criteria.
CREATE PROCEDURE GetProductsByCategoryAndPrice
       @Category Varchar(50),
	   @MinPrice Decimal(10,2)
AS
BEGIN
   SELECT * FROM Products
   Where Category = @Category AND Price > @MinPrice;
END;
EXEC GetProductsByCategoryAndPrice @Category='Electronics', @MinPrice = 12000.00

---18
---Create a stored procedure named InsertNewProduct that accepts parameters for ProductName, Category, Price, and 
---StockQuantity and inserts a new product into the Products table.
CREATE PROCEDURE InsertNewProduct
	@ProductName VARCHAR(50),
	@Category VARCHAR(50),
	@Price DECIMAL(10,2),
	@StockQuantity INT
AS
BEGIN
      insert into Products(ProductName,Category,Price,StockQuantity)
	  Values(@ProductName,@Category,@Price,@StockQuantity);
END;
EXEC InsertNewProduct @ProductName='JoyStick',@Category='Electronics',@Price=7000.00,@StockQuantity=9;

---19
---Create a stored procedure named UpdateCustomerEmail that accepts a CustomerID and 
---a NewEmail parameter and updates the email address for the specified customer.
CREATE PROCEDURE UpdateCustomerEmail
  @CustomerID int,
  @NewEmail VARCHAR(100)
AS
BEGIN
  update Customers
  set Email= @NewEmail
  where CustomerID= @CustomerID
END;
EXEC UpdateCustomerEmail @CustomerID =6,@NewEmail='asha.rao14@gmail.com';

---20
---Create a stored procedure named DeleteOrderByID that accepts an OrderID as a parameter and 
---deletes the corresponding order from the Orders table.
CREATE PROCEDURE DeleteOrderByID
  @OrderID int
AS
BEGIN
  DELETE from Orders
  where OrderID=@OrderID;
END;
exec DeleteOrderByID @OrderID=2;

---21
---Create a stored procedure named GetTotalProductsInCategory that accepts a Category parameter and 
---returns the total number of products in that category using an output parameter.
CREATE PROCEDURE GetTotalProductsInCategory
  @category int,
  @TotalProducts int output
as 
begin
  select TotalProducts= count(*) from Products
  where category=@category;
end;
DECLARE @Total INT;
EXEC GetTotalProductsInCategory @Category = 'Furniture', @TotalProducts = @Total OUTPUT;
SELECT @Total AS GetTotalProductsInCategory;