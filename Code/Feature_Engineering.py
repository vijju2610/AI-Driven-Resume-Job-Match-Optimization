#Feature Engineering
# STEP 2.1: Create custom ranking score
df['Custom_Score'] = (
    df['Match_Score'] * 0.5 +
    df['Experience'] * 0.3 +
    df['Skill_Count'] * 0.2
).round(2)

# STEP 2.2: Create experience level flags
df['Is_Junior'] = df['Experience'].apply(lambda x: 1 if x < 3 else 0)
df['Is_Senior'] = df['Experience'].apply(lambda x: 1 if x >= 7 else 0)

# STEP 2.3: Create skill presence flags
def has_skill(skill_list, keyword):
    return 1 if keyword in skill_list else 0

df['Has_SQL'] = df['Cleaned_Skills'].apply(lambda skills: has_skill(skills, 'sql'))
df['Has_Python'] = df['Cleaned_Skills'].apply(lambda skills: has_skill(skills, 'python'))
df['Has_React'] = df['Cleaned_Skills'].apply(lambda skills: has_skill(skills, 'react'))

# STEP 2.4: Preview engineered features
print("\n🔹 Feature engineering preview:\n")
print(df[['Candidate_Name', 'Experience', 'Skill_Count', 'Custom_Score',
          'Is_Junior', 'Is_Senior', 'Has_SQL', 'Has_Python', 'Has_React']].head())

# Optional: Save engineered file
df.to_csv("/Users/vijju/Desktop/AI-Driven Resume & Job Match Optimization Dashboard/Data_Engineered.csv", index=False)
print("\n✅ Feature-engineered dataset saved as 'Data_Engineered.csv'")
