import pandas as pd
import re

# Load your datasets using full path
resume_df = pd.read_csv("/Users/vijju/Desktop/AI-Driven Resume Screening & Hiring Pipeline Analytics Dashboard/AI_Resume_Screening.csv")
job_df = pd.read_csv("/Users/vijju/Desktop/AI-Driven Resume Screening & Hiring Pipeline Analytics Dashboard/DataAnalyst.csv")

# Helper function to extract keywords
def extract_keywords(text):
    if pd.isnull(text):
        return []
    return re.findall(r'\b\w+\b', text.lower())

# Process job title + description keywords
job_df['Keywords'] = job_df['Job Title'].fillna('').apply(extract_keywords) + \
                     job_df['Job Description'].fillna('').apply(extract_keywords)
job_df['Keywords'] = job_df['Keywords'].apply(set)

# Process resume skills
resume_df['Skills_Keywords'] = resume_df['Skills'].fillna('').apply(
    lambda x: set(skill.strip().lower() for skill in x.split(','))
)

# Match logic: find overlap
matches = []
for i, resume in resume_df.iterrows():
    for j, job in job_df.iterrows():
        score = len(resume['Skills_Keywords'] & job['Keywords'])
        if score > 0:
            matches.append({
                'Resume_ID': resume['Resume_ID'],
                'Candidate_Name': resume['Name'],
                'Skills': resume['Skills'],
                'Experience': resume['Experience (Years)'],
                'Job_Title': job['Job Title'],
                'Company': job['Company Name'],
                'Location': job['Location'],
                'Match_Score': score
            })

# Convert matches to DataFrame and save
match_df = pd.DataFrame(matches).sort_values(by='Match_Score', ascending=False)

# Save output CSV in the same folder
match_df.to_csv("/Users/vijju/Desktop/AI-Driven Resume Screening & Hiring Pipeline Analytics Dashboard/Resume_Job_Match_Report.csv", index=False)
print("✅ Match report saved as 'Resume_Job_Match_Report.csv'")
