#  HR Workforce Analytics & Employee Retention Dashboard

An end-to-end HR analytics project combining **Excel, SQL, Python, and Power BI** 
to analyze employee attrition, compensation patterns, and workforce retention — 
helping organizations make data-driven decisions about talent management.

##  Business Problem

Employee attrition is one of the most costly challenges organizations face — 
replacing an employee can cost significantly more than retaining one. This 
project analyzes workforce data across 1,470 employees to answer critical 
business questions:

- Which departments and roles have the highest turnover?
- What factors most strongly influence employee retention?
- How does compensation relate to performance and attrition?
- Which employee segments require immediate management attention?

##  Tools & Tech Stack

- **Excel** : Data cleaning, calculated columns, PivotTable-based initial analysis
- **SQL (SQLite)** : Advanced querying with Window Functions, CTEs, and multi-factor 
  risk analysis
- **Python (Pandas, Matplotlib, Seaborn)** : Deep EDA, correlation analysis, and 
  statistical validation
- **Power BI** : Multi-page interactive dashboard with KPIs, heatmaps, and 
  actionable business recommendations

##  Project Workflow

This project follows a connected 4-tool pipeline, where each stage builds on 
the previous one:

1. **Excel** : Cleaned raw HR data, engineered calculated columns (Estimated 
   Joining Date, Age Group, Salary Band, Tenure Group), and built PivotTables 
   for initial KPIs.
2. **SQL** : Converted the enriched dataset into a SQLite database and wrote 
   15 analytical queries, including window functions (RANK, running totals) 
   and CTEs to identify department averages, top earners, and multi-factor 
   high-risk employee segments.
3. **Python** : Performed deep exploratory analysis: correlation analysis 
   between attrition and key variables, distribution analysis, and outlier 
   detection using boxplots.
4. **Power BI** : Built a 3-page interactive dashboard combining KPI cards, 
   bar charts, scatter plots, a heatmap matrix, and a data-driven 
   recommendations panel.

##  Dashboard Preview

### Page 1: Workforce Overview
![Workforce Overview](Page1_Workforce_Overview.png)

### Page 2: Attrition & Retention
![Attrition Retention](Page2_Attrition_Retention.png)

### Page 3: Compensation & Performance
![Compensation Performance](Page3_Compensation_Performance.png)

##  Key Insights & Recommendations

1. **Reduce overtime dependency** : Employees working overtime show approximately 
   3× higher attrition than those who don't.

2. **Review retention strategies for Sales Representatives** : This role records 
   the highest overall attrition rate, with high-risk segments reaching 70%.

3. **Strengthen early-tenure engagement** : Employees with 0–2 years of tenure 
   show the highest attrition, highlighting the need for stronger onboarding 
   and early career support.

4. **Monitor low-salary employees closely** : The low salary band shows 
   substantially higher attrition than the high salary band.

5. **Learn from stronger retention areas** : Research & Development has the 
   largest workforce share (~65%) while maintaining relatively lower attrition, 
   offering useful practices that could be examined for other departments.

##  Files in This Repository

| File | Description |
|------|-------------|
| `HR_Analytics_Master.xlsx` | Cleaned dataset with calculated columns and initial PivotTable analysis |
| `hr_analysis.py` | Full Python script: SQL database creation, 15 analytical queries, EDA, correlation analysis |
| `cleaned_hr_data.csv` | Final processed dataset used for the Power BI dashboard |
| `Page1_Workforce_Overview.png` | Screenshot of the Workforce Overview dashboard page |
| `page2_Attrition_Retention.png` | Screenshot of the Attrition & Retention dashboard page |
| `page3_Compensation_Performance.png` | Screenshot of the Compensation & Performance dashboard page |

##  Business Impact

This dashboard moves HR decision-making from reactive to proactive — instead 
of discovering attrition problems after employees leave, management can 
identify at-risk segments (by department, role, salary band, and overtime 
status) in advance and take targeted retention action, ultimately reducing 
recruitment costs and preserving institutional knowledge.

---
*Dataset: IBM HR Analytics Employee Attrition & Performance Dataset, sourced 
from Kaggle.*
