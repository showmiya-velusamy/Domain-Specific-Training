import pandas as pd
# Creating a new dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rajesh", "Meena", "Suresh", "Anita", "Vijay", "Neeta"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Age": [29, 35, 45, 32, 50, 28],
    "Salary": [70000, 85000, 95000, 64000, 120000, 72000],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Delhi", "Mumbai"]
}
df = pd.DataFrame(data)
print(df)

#Exercise 1
df_renamed=df.rename(columns={'Salary':'Annual Salary','City':'Location'})
print(df_renamed)

#Exercise 2
df_dropped=df_renamed.drop(columns=['Location'])
print(df_dropped)

#Exercise 3
index_to_drop=df[df['Name']=='Suresh'].index
df=df.drop(index_to_drop)
print(df)

#Exercise 4
df.loc[df["Name"] == "Meena", "Annual Salary"] = None
df["Annual Salary"].fillna(df["Annual Salary"].mean(), inplace=True)
print(df)

#Exercise 5
df['Seniority'] = df['Age'].apply(lambda x: 'Senior' if x >= 40 else 'Junior')
print(df)

#Exercise 6
grouped_df = df.groupby("Department")["Annual Salary"].mean().reset_index()
grouped_df.rename(columns={"Annual Salary": "Average Salary"}, inplace=True)
print("\nGrouped DataFrame with average salary by department:")
print(grouped_df)