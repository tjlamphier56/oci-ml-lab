import pandas as pd

print("OCI ML Lab Initialized")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

print("\nDataFrame Summary:")
print(df.describe())    

print("\nAverage Age:", df["Age"].mean())
