import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3, 4, 5, 6],
    'Column2': ['A', 'B', 'C', 'D', 'E', 'F']
}

df = pd.DataFrame(data)

# Define the starting row index (x)
x = 3  # For example, start from the 4th row (index 3)

# Define a method that accepts a DataFrame
def process_dataframe(sliced_df):
    print("Processing DataFrame:")
    print(sliced_df)

# Slice the DataFrame from the x-th row to the end
sliced_df = df.iloc[x:]
print(len(sliced_df))
 
# Pass the sliced DataFrame to the method
process_dataframe(sliced_df)
import os

# Given path
path = "/Weaviate/class_1$tenant_D/processed/unsynced/datalog.csv"

# Get the parent directory of the path
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(path)))
print(f"Parent directory: {parent_dir}")

