import pandas as pd

# step 1: Read the data from csv
input_file = 'input_data_cvs'
data = pd.read_csv(input_file)

# Display the first few rows of the data
print("Original Data")
print(data.head())

# Step 2: Perform some bacis data manipulations
# For example: lets calculate the average of a numeric column

if 'numeric_column' in data.columns:
    data['average_value'] = data['numeric_column'].mean()
else:
    print("No numeric column found in the data")

# display the modified data

print("\nModified Data")
print(data.head())

# Step 3: Save the manipulated data to a new csv file
output_file = 'output_data_csv'
data.to_csv(output_file, index=False)

# Checkingn Data type
print(data.dtypes)

# Step 4: Lets calculate the meand and standard deviation of the numeric cokumn
print(data.describe())