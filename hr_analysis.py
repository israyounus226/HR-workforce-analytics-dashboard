import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("HR_Analytics.db")

# Loading data from excel
df = pd.read_excel("HR_Analytics_Master.xlsx", sheet_name="HR Dataset")

# Cleaning Column Names
df.columns = [c.replace(" ", "_") for c in df.columns]

# Converting SQLite to Database
df.to_sql("Employees", conn, if_exists="replace", index=False)
print("Database Created Successfully")
print(df.shape)
print(df.columns.tolist())

# SQL ANALYSIS QUERIES

# Query 1: Department-wise Attrition Rate
query1 = """
SELECT 
    Department,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY Department
ORDER BY Attrition_Rate_Percent DESC
"""
print("--- Department-wise Attrition Rate ---")
print(pd.read_sql(query1, conn), "\n")

# Query 2: Salary Rank within Department 
query2 = """
SELECT 
    JobRole,
    Department,
    MonthlyIncome,
    RANK() OVER (PARTITION BY Department ORDER BY MonthlyIncome DESC) as Salary_Rank_In_Dept
FROM Employees
ORDER BY Department, Salary_Rank_In_Dept
LIMIT 15
"""
print("--- Salary Rank within Department ---")
print(pd.read_sql(query2, conn), "\n")

# Query 3: Employees earning above department average
query3 = """
WITH DeptAvg AS (
    SELECT Department, AVG(MonthlyIncome) as Dept_Avg_Salary
    FROM Employees
    GROUP BY Department
)
SELECT 
    E.JobRole,
    E.Department,
    E.MonthlyIncome,
    ROUND(D.Dept_Avg_Salary, 2) as Department_Average
FROM Employees E
JOIN DeptAvg D ON E.Department = D.Department
WHERE E.MonthlyIncome > D.Dept_Avg_Salary
ORDER BY E.MonthlyIncome DESC
LIMIT 10
"""
print("--- Employees Earning Above Department Average ---")
print(pd.read_sql(query3, conn), "\n")

# Query 4: Attrition by Job Role
query4 = """
SELECT 
    JobRole,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY JobRole
ORDER BY Attrition_Rate_Percent DESC
"""
print("--- Attrition Rate by Job Role ---")
print(pd.read_sql(query4, conn), "\n")


# Query 5: Attrition by Tenure Group
query5 = """
SELECT 
    TenureGroup,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY TenureGroup
ORDER BY Attrition_Rate_Percent DESC
"""
print("--- Attrition Rate by Tenure Group ---")
print(pd.read_sql(query5, conn), "\n")


# Query 6: Attrition by Salary Band
query6 = """
SELECT 
    SalaryBand,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY SalaryBand
ORDER BY Attrition_Rate_Percent DESC
"""
print("--- Attrition Rate by Salary Band ---")
print(pd.read_sql(query6, conn), "\n")


# Query 7: Attrition by Age Group
query7 = """
SELECT 
    AgeGroup,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY AgeGroup
ORDER BY AgeGroup
"""
print("--- Attrition Rate by Age Group ---")
print(pd.read_sql(query7, conn), "\n")


# Query 8: Salary vs Experience Correlation
query8 = """
SELECT 
    CASE 
        WHEN TotalWorkingYears <= 5 THEN '0-5 yrs'
        WHEN TotalWorkingYears <= 10 THEN '6-10 yrs'
        WHEN TotalWorkingYears <= 20 THEN '11-20 yrs'
        ELSE '20+ yrs'
    END as Experience_Bucket,
    COUNT(*) as Employee_Count,
    ROUND(AVG(MonthlyIncome), 2) as Avg_Salary
FROM Employees
GROUP BY Experience_Bucket
ORDER BY Avg_Salary
"""
print("--- Salary vs Experience ---")
print(pd.read_sql(query8, conn), "\n")


# Query 9: Performance Rating vs Average Salary
query9 = """
SELECT 
    PerformanceRating,
    COUNT(*) as Employee_Count,
    ROUND(AVG(MonthlyIncome), 2) as Avg_Salary,
    ROUND(AVG(PercentSalaryHike), 2) as Avg_Salary_Hike
FROM Employees
GROUP BY PerformanceRating
"""
print("--- Performance vs Compensation ---")
print(pd.read_sql(query9, conn), "\n")


# Query 10: Department Compensation Comparison 
query10 = """
SELECT 
    Department,
    COUNT(*) as Employee_Count,
    ROUND(AVG(MonthlyIncome), 2) as Avg_Salary,
    MIN(MonthlyIncome) as Min_Salary,
    MAX(MonthlyIncome) as Max_Salary
FROM Employees
GROUP BY Department
ORDER BY Avg_Salary DESC
"""
print("--- Department Compensation Comparison ---")
print(pd.read_sql(query10, conn), "\n")


# Query 11: Overtime Impact on Attrition (High-Impact Insight)
query11 = """
SELECT 
    OverTime,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY OverTime
ORDER BY Attrition_Rate_Percent DESC
"""
print("--- Overtime Impact on Attrition ---")
print(pd.read_sql(query11, conn), "\n")


# Query 12: Job Satisfaction Impact on Attrition
query12 = """
SELECT 
    JobSatisfaction,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction
"""
print("--- Job Satisfaction Impact on Attrition ---")
print(pd.read_sql(query12, conn), "\n")


# Query 13: Running Total of Employees Hired by Year (Window Function)
query13 = """
WITH HiringByYear AS (
    SELECT 
        strftime('%Y', EstimatedJoiningDate) as Hire_Year,
        COUNT(*) as Employees_Hired
    FROM Employees
    GROUP BY Hire_Year
)
SELECT 
    Hire_Year,
    Employees_Hired,
    SUM(Employees_Hired) OVER (ORDER BY Hire_Year) as Running_Total_Employees
FROM HiringByYear
ORDER BY Hire_Year
"""
print("--- Hiring Trend & Running Total (Workforce Growth) ---")
print(pd.read_sql(query13, conn), "\n")


# Query 14: Top 3 Highest Paid Employees per Department (Window Function)
query14 = """
WITH RankedSalaries AS (
    SELECT 
        JobRole,
        Department,
        MonthlyIncome,
        RANK() OVER (PARTITION BY Department ORDER BY MonthlyIncome DESC) as Salary_Rank
    FROM Employees
)
SELECT * FROM RankedSalaries
WHERE Salary_Rank <= 3
ORDER BY Department, Salary_Rank
"""
print("--- Top 3 Highest Paid Employees per Department ---")
print(pd.read_sql(query14, conn), "\n")


# Query 15: High-Risk Segment Identification (Multiple Risk Factors Combined)
query15 = """
SELECT 
    Department,
    JobRole,
    SalaryBand,
    OverTime,
    COUNT(*) as Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Employees_Left,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as Attrition_Rate_Percent
FROM Employees
GROUP BY Department, JobRole, SalaryBand, OverTime
HAVING COUNT(*) >= 5
ORDER BY Attrition_Rate_Percent DESC
LIMIT 10
"""
print("--- High-Risk Employee Segments (Combined Risk Factors) ---")
print(pd.read_sql(query15, conn), "\n")


# PYTHON DEEP EDA PHASE

df_full = pd.read_sql("SELECT * FROM Employees", conn)
print("Full Dataset Shape:", df_full.shape)
print(df_full.info())
print(df_full.describe())

# Correlation Analysis - Numeric columns ka relationship
# Converting Attrition into Numeric (Yes=1, No=0)
df_full["Attrition_Numeric"] = df_full["Attrition"].apply(lambda x: 1 if x == "Yes" else 0)

# Selecting important numeric columns for correlation
correlation_cols = ["Attrition_Numeric", "Age", "MonthlyIncome", "YearsAtCompany", 
                     "TotalWorkingYears", "JobSatisfaction", "EnvironmentSatisfaction",
                     "WorkLifeBalance", "DistanceFromHome", "NumCompaniesWorked",
                     "YearsSinceLastPromotion", "PerformanceRating"]

correlation_matrix = df_full[correlation_cols].corr()
print("--- Correlation with Attrition ---")
print(correlation_matrix["Attrition_Numeric"].sort_values(ascending=False))

# Correlation Heatmap (Visualization)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap - Attrition Factors")
plt.tight_layout()
plt.show()

# Distribution Analysis (Age, Salary)
# Distribution of key variables
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(df_full["Age"], bins=20, color="steelblue", edgecolor="black")
axes[0].set_title("Age Distribution")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Frequency")

axes[1].hist(df_full["MonthlyIncome"], bins=20, color="coral", edgecolor="black")
axes[1].set_title("Monthly Income Distribution")
axes[1].set_xlabel("Monthly Income")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()

# Outlier Detection (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x="Department", y="MonthlyIncome", data=df_full)
plt.title("Salary Outliers by Department")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# EXPORT FOR POWER BI
df_full.to_csv("cleaned_hr_data.csv", index=False)
print("File exported successfully: cleaned_hr_data.csv")

conn.close()