import pandas as pd
import csv

# Set the file path
file_path = 'rawdata2.csv'

# Step 1: Clean the data
# Read the file using Pandas
data = pd.read_csv(file_path, na_values=['no data'], encoding='utf-8')

# Remove special characters
data = data.replace({r'\#': '', r'\*': ''}, regex=True)

# Drop duplicate rows
data = data.drop_duplicates()

# Convert ALL columns to numeric where possible
for col in data.columns:
    data[col] = pd.to_numeric(data[col], errors='ignore')

# Identify numeric columns again (after conversion)
numeric_cols = data.select_dtypes(include=['number']).columns

# Round to 2 decimal places (keeping them as floats)
data[numeric_cols] = data[numeric_cols].apply(lambda x: x.round(0))


# Save cleaned data to a new file
cleaned_file_path = 'cleandata2.csv'
data.to_csv(cleaned_file_path, index=False)


print("Cleaned data file saved to:", cleaned_file_path)

# Step 2: Systematic sampling (e.g., every 8th row)
# Load the cleaned CSV file
cleaned_data = pd.read_csv(cleaned_file_path)

# Extract every 15th row
sample = cleaned_data.iloc[::15]

# Save the sampled data
sample_file_path = 'sampledata2.csv'
sample.to_csv(sample_file_path, index=False)

print("Sampled data file saved to:", sample_file_path)