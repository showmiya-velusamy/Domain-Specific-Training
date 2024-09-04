import pandas as pd

#Exercise 1: Creating DataFrame from Scratch
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    'Price': [80000, 1500, 20000, 3000, 40000],
    'Quantity': [10, 100, 50, 75, 30]
}
df = pd.DataFrame(data)
print(df)

#Exercise 2: Basic DataFrame Operations
# Display the first 3 rows
print(df.head(3))
# Display the column names
print("Column names:", df.columns)
# Display the index
print("Index:", df.index)
# Display summary statistics for numeric columns
print(df.describe())

#Exercise 3: Selecting Data
# 1. Select and display the "Product" and "Price" columns
print("\nProduct and Price columns:\n", df[['Product', 'Price']])
# 2. Select rows where the "Category" is "Electronics" and print them
electronics_df = df[df['Category'] == 'Electronics']
print("\nElectronics Category:\n", electronics_df)

#Exercise 4: Filtering Data
# 1. Filter the DataFrame to display only the products with a price greater than 10,000
high_price_df = df[df['Price'] > 10000]
print("\nProducts with Price > 10,000:\n", high_price_df)
# 2. Filter the DataFrame to show only products that belong to the "Accessories" category and have a quantity greater than 50
accessories_df = df[(df['Category'] == 'Accessories') & (df['Quantity'] > 50)]
print("\nAccessories with Quantity > 50:\n", accessories_df)

#Exercise 5: Adding and Removing Columns
# 1. Add a new column "Total Value" which is calculated by multiplying "Price" and "Quantity"
df['Total Value'] = df['Price'] * df['Quantity']
print("\nDataFrame with 'Total Value':\n", df)
# 2. Drop the "Category" column from the DataFrame and print the updated DataFrame
df = df.drop(columns=['Category'])
print("\nDataFrame after dropping 'Category' column:\n", df)

#Exercise 6: Sorting Data
# 1. Sort the DataFrame by "Price" in descending order
sorted_by_price = df.sort_values(by="Price", ascending=False)
print("DataFrame sorted by Price (descending):\n", sorted_by_price)
# 2. Sort the DataFrame by "Quantity" in ascending order, then by "Price" in descending order
sorted_by_quantity_price = df.sort_values(by=["Quantity", "Price"], ascending=[True, False])
print("\nDataFrame sorted by Quantity (ascending) and Price (descending):\n", sorted_by_quantity_price)

#Exercise 7: Grouping Data
# 1. Group the DataFrame by "Category" and calculate the total quantity for each category
total_quantity_by_category = df.groupby("Category")["Quantity"].sum().reset_index()
print("\nTotal Quantity by Category:\n", total_quantity_by_category)
# 2. Group by "Category" and calculate the average price for each category
average_price_by_category = df.groupby("Category")["Price"].mean().reset_index()
print("\nAverage Price by Category:\n", average_price_by_category)

#Exercise 8: Handling Missing Data
# Introduce some missing values in the "Price" column by assigning None to two rows
df.loc[1, "Price"] = None
df.loc[3, "Price"] = None
print("\nDataFrame with missing Price values:\n", df)
# 1. Fill the missing values with the mean price of the available products
mean_price = df["Price"].mean()
df["Price"].fillna(mean_price, inplace=True)
print("\nDataFrame after filling missing Price values with mean:\n", df)
# 2. Drop any rows where the "Quantity" is less than 50
df_filtered = df[df["Quantity"] >= 50]
print("\nDataFrame after dropping rows with Quantity < 50:\n", df_filtered)

#Exercise 9: Apply Custom Functions
# 1. Apply a custom function to the "Price" column that increases all prices by 5%
df["Price"] = df["Price"].apply(lambda x: x * 1.05)
print("\nDataFrame after increasing prices by 5%:\n", df)
# 2. Create a new column "Discounted Price" that reduces the original price by 10%
df["Discounted Price"] = df["Price"] * 0.90
print("\nDataFrame with Discounted Price column:\n", df)

#Exercise 10: Merging DataFrames
# Create another DataFrame with columns "Product" and "Supplier"
supplier_data = {
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    "Supplier": ['Supplier A', 'Supplier B', 'Supplier A', 'Supplier C', 'Supplier B']
}
supplier_df = pd.DataFrame(supplier_data)
# 1. Merge it with the original DataFrame based on the "Product" column
merged_df = pd.merge(df, supplier_df, on="Product")
print("\nMerged DataFrame:\n", merged_df)

#Exercise 11: Pivot Tables
# 1. Create a pivot table that shows the total quantity of products for each category and product combination
pivot_table = pd.pivot_table(df, values='Quantity', index='Category', columns='Product', aggfunc='sum', fill_value=0)
print("Pivot Table showing total quantity for each category and product:\n", pivot_table)

#Exercise 12: Concatenating DataFrames
store_a_data = {
    "Product": ['Laptop', 'Mouse', 'Monitor'],
    "Price": [80000, 1575, 21000],
    "Quantity": [10, 100, 50]
}

store_b_data = {
    "Product": ['Keyboard', 'Phone', 'Laptop'],
    "Price": [3150, 42000, 81000],
    "Quantity": [75, 30, 12]
}
store_a_df = pd.DataFrame(store_a_data)
store_b_df = pd.DataFrame(store_b_data)
# 1. Concatenate these DataFrames to create a combined inventory list
combined_inventory = pd.concat([store_a_df, store_b_df], ignore_index=True)
print("\nCombined Inventory DataFrame:\n", combined_inventory)

#Exercise 13: Working with Dates

# 1. Create a DataFrame with a "Date" column that contains the last 5 days starting from today
date_range = pd.date_range(end=pd.Timestamp.today(), periods=5)
sales_data = {
    "Date": date_range,
    "Sales": np.random.randint(1000, 5000, size=5)
}
sales_df = pd.DataFrame(sales_data)
print("\nSales DataFrame:\n", sales_df)
# 2. Find the total sales for all days combined
total_sales = sales_df["Sales"].sum()
print("\nTotal Sales for all days combined:", total_sales)

#Exercise 14: Reshaping Data with Melt
# Creating a DataFrame with columns "Product", "Region", "Q1_Sales", "Q2_Sales"
sales_data = {
    "Product": ['Laptop', 'Mouse', 'Monitor'],
    "Region": ['North', 'South', 'East'],
    "Q1_Sales": [15000, 20000, 13000],
    "Q2_Sales": [17000, 21000, 14000]
}
sales_df = pd.DataFrame(sales_data)
# 1. Use pd.melt() to reshape the DataFrame so that it has columns "Product", "Region", "Quarter", and "Sales"
melted_df = pd.melt(sales_df, id_vars=['Product', 'Region'], var_name='Quarter', value_name='Sales')
print("\nMelted DataFrame:\n", melted_df)

#Exercise 15: Reading and Writing Data
df = pd.read_csv('products.csv')
print("DataFrame loaded from 'products.csv':\n", df)
df['Total Value'] = df['Price'] * df['Quantity']
print("\nDataFrame after adding 'Total Value' column:\n", df)
df.to_csv('updated_products.csv', index=False)
print("\nDataFrame written to 'updated_products.csv'.")

#Exercise 16: Renaming Columns
df.rename(columns={
    'Prod': 'Product',
    'Cat': 'Category',
    'Qty': 'Quantity'
}, inplace=True)
print(df)

#Exercise 17: Creating a MultiIndex DataFrame
arrays = [
    ['Store1', 'Store1', 'Store2', 'Store2', 'Store3', 'Store3'],
    ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone', 'Headphones']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Store', 'Product'))
data = {
    'Price': [80000, 1500, 20000, 3000, 40000, 2500],
    'Quantity': [10, 100, 50, 75, 30, 60]
}
df = pd.DataFrame(data, index=index)
print(df)

#Exercise 18: Resample Time-Series Data
dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
sales = np.random.randint(100, 1000, size=len(dates))
df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})
df.set_index('Date', inplace=True)
print("Original DataFrame:")
print(df)
weekly_sales = df.resample('W').sum()
print("\nWeekly Sales DataFrame:")
print(weekly_sales)

#Exercise 19: Handling Duplicates
df_cleaned = df.drop_duplicates()
print("\nCleaned DataFrame without duplicates:")
print(df_cleaned)

#Exercise 20: Correlation Matrix
data = {
    'Height': [160, 165, 170, 175, 180],
    'Weight': [55, 60, 65, 70, 75],
    'Age': [25, 30, 35, 40, 45],
    'Income': [50000, 55000, 60000, 65000, 70000]
}
df = pd.DataFrame(data)
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

#Exercise 21: Cumulative Sum and Rolling Window
dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
sales = np.random.randint(100, 1000, size=len(dates))
df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})
df.set_index('Date', inplace=True)
df['Cumulative Sales'] = df['Sales'].cumsum()
df['Rolling Avg'] = df['Sales'].rolling(window=7).mean()
print(df)

#Exercise 22: String Operations
data = {
    'Names': ['John Doe', 'Jane Smith', 'Sam Brown']
}
df = pd.DataFrame(data)
df[['First Name', 'Last Name']] = df['Names'].str.split(' ', 1, expand=True)
df['First Name'] = df['First Name'].str.upper()
df.drop(columns=['Names'], inplace=True)
print(df)

#Exercise 23: Conditional Selections with `np.where`
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [45, 32, 28, 50, 36],
    'Department': ['HR', 'Finance', 'IT', 'Management', 'Marketing']
}
df = pd.DataFrame(data)
df['Status'] = np.where(df['Age'] >= 40, 'Senior', 'Junior')
print(df)

#Exercise 24: Slicing DataFrames
data = {
    'Products': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone', 'Tablet', 'Printer', 'Camera', 'Headphones', 'Smartwatch',
                 'TV', 'Speakers', 'Projector', 'Router', 'Smartphone', 'Charger', 'Power Bank', 'External HDD', 'SSD', 'Webcam'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics',
                 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics', 'Accessories'],
    'Sales': [80000, 1500, 20000, 3000, 40000, 12000, 2500, 35000, 5000, 7000,
              90000, 12000, 30000, 4000, 60000, 5000, 3000, 70000, 15000, 4000],
    'Profit': [5000, 500, 2500, 400, 2000, 800, 300, 1500, 200, 300,
               6000, 800, 4000, 300, 5000, 600, 400, 7000, 2000, 350]
}
df = pd.DataFrame(data)
print("First 10 rows:")
print(df.head(10))
print()
print("Rows where Category is 'Electronics':")
print(df[df['Category'] == 'Electronics'])
print()
print("Sales and Profit for products with sales greater than 50,000:")
print(df[df['Sales'] > 50000][['Sales', 'Profit']])

#Exercise 25: Concatenating DataFrames Vertically and Horizontally
#1
data_a = {
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'Salary': [70000, 60000, 80000]
}
df_a = pd.DataFrame(data_a)
data_b = {
    'Employee': ['David', 'Eve', 'Frank'],
    'Age': [40, 28, 32],
    'Salary': [85000, 65000, 72000]
}
df_b = pd.DataFrame(data_b)
print("DataFrame for Store A:")
print(df_a)
print("\nDataFrame for Store B:")
print(df_b)

#2
df_combined = pd.concat([df_a, df_b], ignore_index=True)
print("\nCombined DataFrame:")
print(df_combined)

#3
# DataFrame with Employee and Department
data_department = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['HR', 'Finance', 'IT', 'Management', 'Marketing', 'IT']
}
df_department = pd.DataFrame(data_department)
data_salary = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [70000, 60000, 80000, 85000, 65000, 72000]
}
df_salary = pd.DataFrame(data_salary)
df_merged = pd.merge(df_department, df_salary, on='Employee')
print("\nMerged DataFrame:")
print(df_merged)

#Exercise 26: Exploding Lists in DataFrame Columns
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor'],
    'Features': [['Intel i7', '16GB RAM', '512GB SSD'], ['Wireless', 'Ergonomic'], ['4K Resolution', '27 inches']]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df_exploded = df.explode('Features')
print("\nDataFrame after exploding 'Features':")
print(df_exploded)

#Exercise 27: Using `.map()` and `.applymap()`
def increase_price(price):
    return price * 1.10
df['Price'] = df['Price'].map(increase_price)
print("\nDataFrame with Increased Prices:")
print(df)
def format_to_two_decimal(x):
    if isInstance(x, (int, float)):
        return f"{x:.2f}"
    return x
print("\nDataFrame with Formatted Numeric Values:")
print(df_formatted)

#Exercise 28: Combining `groupby()` with `apply()`
def calculate_profit_margin(group):
    total_sales = group['Sales'].sum()
    total_profit = group['Profit'].sum()
    return total_profit / total_sales if total_sales != 0 else 0
profit_margin_by_city = df.groupby('City').apply(calculate_profit_margin).reset_index(name='Profit Margin')
print("\nProfit Margin by City:")
print(profit_margin_by_city)

#Exercise 29: Creating a DataFrame from Multiple Sources
csv_data = """ID,Name,Age
1,Alice,30
2,Bob,25
3,Charlie,35"""

# Simulate JSON data
json_data = """[
    {"ID": 1, "Salary": 70000},
    {"ID": 2, "Salary": 60000},
    {"ID": 3, "Salary": 80000}
]"""

# Simulate dictionary data
dict_data = {
    'ID': [1, 2, 3],
    'Department': ['HR', 'Finance', 'IT']
}

# Create DataFrames
df_csv = pd.read_csv(StringIO(csv_data))
df_json = pd.read_json(StringIO(json_data))
df_dict = pd.DataFrame(dict_data)

# Print the individual DataFrames
print("DataFrame from CSV:")
print(df_csv)
print("\nDataFrame from JSON:")
print(df_json)
print("\nDataFrame from Dictionary:")
print(df_dict)

# Merge the DataFrames based on the 'ID' column
df_merged = pd.merge(df_csv, df_json, on='ID')
df_merged = pd.merge(df_merged, df_dict, on='ID')

# Print the consolidated report
print("\nConsolidated Report:")
print(df_merged)

#Exercise 30: Dealing with Large Datasets
import pandas as pd
import numpy as np
import datetime

# 1. Create the large DataFrame
num_rows = 1_000_000

# Generate sample data
np.random.seed(0)
transaction_ids = np.arange(1, num_rows + 1)
customers = np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], size=num_rows)
products = np.random.choice(['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'], size=num_rows)
amounts = np.random.uniform(50, 1000, size=num_rows)
dates = pd.date_range(start='2023-01-01', periods=num_rows, freq='T')

# Create the DataFrame
df_large = pd.DataFrame({
    'Transaction ID': transaction_ids,
    'Customer': customers,
    'Product': products,
    'Amount': amounts,
    'Date': dates
})

# Print the first few rows of the DataFrame
print("Sample of the Large DataFrame:")
print(df_large.head())

# 2. Split the DataFrame into smaller chunks and analyze each chunk
chunk_size = 100_000
chunks = np.array_split(df_large, num_rows // chunk_size)

# Perform analysis on each chunk
results = []
for chunk in chunks:
    total_sales = chunk['Amount'].sum()
    results.append(total_sales)

# Combine results
total_sales_combined = sum(results)

# Print the total sales
print("\nTotal Sales Combined from All Chunks:")
print(total_sales_combined)

