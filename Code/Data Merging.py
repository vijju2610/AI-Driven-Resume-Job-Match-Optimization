import pandas as pd
import os

# Folder where your CSVs are saved
folder_path = "/Users/vijju/Desktop/AI-Driven Resume & Job Match Optimization Dashboard"

# Exact file names from your screenshot (watch that space in "pt 1 .csv")
file_names = [
    "pt 1 .csv",
    "pt 2.csv",
    "pt 3.csv",
    "pt 4.csv",
    "pt 5.csv"
]

# Build full paths
file_paths = [os.path.join(folder_path, file) for file in file_names]

# Merge CSVs
combined_df = pd.concat([pd.read_csv(fp) for fp in file_paths], ignore_index=True)

# Save merged file
output_path = os.path.join(folder_path, "combined_resume_data.csv")
combined_df.to_csv(output_path, index=False)

print("✅ CSV files merged and saved successfully!")
print("📁 Location:", output_path)
