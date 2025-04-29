SELECT 
    Candidate_Name AS "Candidate",
    Experience AS "Years of Experience",
    Custom_Score AS "Total Score",
    City AS "City",
    State AS "State"
FROM resumes
WHERE Has_Python = 1
ORDER BY Custom_Score DESC
LIMIT 10;

SELECT Candidate_Name, Experience, City, State
FROM resumes
WHERE Is_Junior = 1
ORDER BY Experience;

SELECT Candidate_Name, Experience, Skill_Count, Custom_Score
FROM resumes
WHERE Is_Senior = 1 AND Has_SQL = 1
ORDER BY Custom_Score DESC
LIMIT 10;

SELECT City, COUNT(*) AS Candidate_Count
FROM resumes
GROUP BY City
ORDER BY Candidate_Count DESC
LIMIT 10;

SELECT State, ROUND(AVG(Experience), 2) AS Avg_Experience
FROM resumes
GROUP BY State
ORDER BY Avg_Experience DESC;



