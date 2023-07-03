import pandas as pd
import yaml

# Read the YAML file
with open('destination to path of yml file saved', 'r') as file:
    data = yaml.safe_load(file)

# Convert YAML to pandas DataFrame
df = pd.json_normalize(data)

# Save DataFrame to Excel
output_path = 'destination of path of saving excel file'
df.to_excel(output_path, index=False)

print(f"Excel file saved at: {output_path}")

