import pandas as pd
import numpy as np
import re

# STEP 1.1: Load the dataset
file_path = "/Users/vijju/Desktop/AI-Driven Resume & Job Match Optimization Dashboard/data.csv"
df = pd.read_csv(file_path)

# STEP 1.2: Basic exploration
print("🔹 Dataset Info:\n")
print(df.info())
print("\n🔹 First 5 rows:\n")
print(df.head())

# STEP 1.3: Check for missing values
print("\n🔹 Missing values per column:\n")
print(df.isnull().sum())

# STEP 1.4: Clean the 'Skills' column
def clean_skills(skills_text):
    if pd.isnull(skills_text):
        return []
    return [skill.strip().lower() for skill in skills_text.split(',')]

df['Cleaned_Skills'] = df['Skills'].apply(clean_skills)
df['Skill_Count'] = df['Cleaned_Skills'].apply(len)

# STEP 1.5: Parse location into city and state
def split_location(loc):
    if pd.isnull(loc):
        return pd.Series([np.nan, np.nan])
    parts = loc.split(',')
    if len(parts) == 2:
        return pd.Series([parts[0].strip(), parts[1].strip()])
    return pd.Series([loc.strip(), np.nan])

df[['City', 'State']] = df['Location'].apply(split_location)

# STEP 1.6: Clean the 'Company' column (strip whitespace, remove newlines)
df['Company'] = df['Company'].astype(str).str.replace('\n', ' ', regex=False).str.strip()

# 🆕 STEP 1.6.1: Fill missing company names
df['Company'].fillna('Unknown', inplace=True)

# STEP 1.7: Preview cleaned data
print("\n🔹 Cleaned dataset preview:\n")
print(df[['Candidate_Name', 'Cleaned_Skills', 'Skill_Count', 'City', 'State']].head())

# STEP 1.8: Save cleaned file for next steps
df.to_csv("/Users/vijju/Desktop/AI-Driven Resume & Job Match Optimization Dashboard/Data_Cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as 'Data_Cleaned.csv'")
