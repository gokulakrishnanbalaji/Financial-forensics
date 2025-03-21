import os
import pandas as pd

folder_path = "."  # Current folder
output_file = "merged_output.csv"

# Get list of all CSV files in the current folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Print found files (debugging)
print("CSV Files found:", csv_files)

# Check if any CSV files exist
if not csv_files:
    print("Error: No CSV files found in the current folder.")
    exit()

# Read the first CSV file as the base dataframe
df_merged = pd.read_csv(csv_files[0])

# Merge all other CSVs on the 'Name' column
for file in csv_files[1:]:
    df = pd.read_csv(file)
    df_merged = pd.merge(df_merged, df, on='Name', how='outer', suffixes=('', '_dup'))  # Prevent merge error

# Drop duplicate columns (columns ending in '_dup')
df_merged = df_merged.loc[:, ~df_merged.columns.str.endswith('_dup')]

# Save the merged dataframe to a new CSV
df_merged.to_csv(output_file, index=False)

print(f"Merged CSV saved as {output_file} in the current folder.")
