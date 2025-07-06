import pandas as pd
import csv

# Load your original CSV (update path as needed)
input_file = "dummy_employees.csv"
output_file = "employees_cleaned.csv"

# Read the CSV
df = pd.read_csv(input_file)

# Save with proper quoting
df.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL)

print("✅ Cleaned file saved as:", output_file)
