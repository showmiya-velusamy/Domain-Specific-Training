#Exercise 5
import pandas as pd
data = {
    "Name": ["Amit", "Neha", "Raj", "Priya"],
    "Age": [28, None, 35, 29],
    "City": ["Delhi", "Mumbai", None, "Chennai"]
}
df = pd.DataFrame(data)
average_age = df["Age"].mean()
df["Age"].fillna(average_age, inplace=True)
df_dropped_rows = df.dropna()
print("DataFrame after filling missing Age values:")
print(df)
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropped_rows)

#Exercise 6
df_dropped_rows["Salary"] = [50000, 60000, 70000, 65000]
df_final = df_dropped_rows.drop(columns=["City"])
print(df_final)

#Exercise 7
df_sorted_by_age = df_final.sort_values(by="Age")
df_sorted_by_city_and_age = df_with_city_dropped.sort_values(by=["City", "Age"], ascending=[True, False])

#Exercise 8
average_age_by_city = df_with_city_dropped.groupby("City")["Age"].mean()
count_by_city_age = df_with_city_dropped.groupby(["City", "Age"]).size()

#Exercise 9
df1 = pd.DataFrame({
    "Name": ["Amit", "Neha", "Raj"],
    "Department": ["HR", "IT", "Finance"]
})
df2 = pd.DataFrame({
    "Name": ["Neha", "Raj", "Priya"],
    "Salary": [60000, 70000, 65000]
})
df_inner = pd.merge(df1, df2, on="Name", how="inner")
print("Inner Join:")
print(df_inner)
df_left = pd.merge(df1, df2, on="Name", how="left")
print("\nLeft Join:")
print(df_left)

