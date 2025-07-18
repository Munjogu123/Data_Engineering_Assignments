## International Debt Analysis Using SQL & Data Visualization

---

### Project Overview
Countries take on debt not just for necessities but to support economic development. Infrastructure spending, for instance, is a costly yet crucial investment for a country’s progress. The World Bank provides debt financing to developing countries to facilitate such initiatives.

In this project, you will analyze international debt data collected by the World Bank. The dataset includes information on the total debt (in USD) owed by developing countries across multiple debt categories from 1970 to 2015.

Your goal is to explore this dataset using SQL in PostgreSQL, extract meaningful insights, and answer key financial questions.

**Dataset:** `international_debt_with_missing_values.csv`

---

### Project Tasks & Deliverables
- Connect to the PostgreSQL database using the provided connection string and explore the dataset.
- Write SQL queries to find answers to the following key questions:

    1. What is the total amount of debt owed by all countries in the dataset?
    2. How many distinct countries are recorded in the dataset?
    3. What are the distinct types of debt indicators, and what do they represent?
    4. Which country has the highest total debt, and how much does it owe?
    5. What is the average debt across different debt indicators?
    6. Which country has made the highest amount of principal repayments?
    7. What is the most common debt indicator across all countries?
    8. Identify any other key debt trends and summarize your findings.

- Document your process: Clearly explain the steps you followed, your query logic, and insights from your findings.

- **Final Deliverable:**
  - A GitHub repository containing:  
    - A SQL script with all queries used.  
    - A report (Markdown or PDF) summarizing findings with supporting data. 

---

### 🔍 Key Trends and Insights
- China leads both in total borrowing and principal repayments, reflecting significant debt activity and economic capacity.
- The top 3 countries with the greatest debt are:
    1. China
    2. South Asia
    3. Brazil
- The most common debt indicator in most countries is *PPG, official creditors (INT, current US$)*.
