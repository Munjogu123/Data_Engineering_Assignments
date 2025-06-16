create schema solution;

select * from solution.international_debt_with_missing_values limit 10;

-- 1. What is the total amount of debt owed by all countries in the dataset?
select sum(debt) as total_debt
from solution.international_debt_with_missing_values
where debt is not null;


-- 2. How many distinct countries are recorded in the dataset?
select count(distinct country_name)
from solution.international_debt_with_missing_values
where country_name <> '';


-- 3. What are the distinct types of debt indicators, and what do they represent?
select distinct indicator_name
from solution.international_debt_with_missing_values
where indicator_name <> '';


-- 4. Which country has the highest total debt, and how much does it owe?
select country_name, sum(debt) as highest_debt
from solution.international_debt_with_missing_values
where country_name <> ''
group by country_name 
order by highest_debt desc
limit 1;


-- 5. What is the average debt across different debt indicators?
select indicator_name, indicator_code, avg(debt) as avg_debt
from solution.international_debt_with_missing_values
where indicator_name <> '' and indicator_code <> ''
group by indicator_name, indicator_code
order by avg_debt desc;


-- 6. Which country has made the highest amount of principal repayments?
select country_name, sum(debt) as principal_repayment
from solution.international_debt_with_missing_values
where indicator_name like '%Principal repayments%' and country_name <> ''
group by country_name
having sum(debt) > 0
order by principal_repayment desc
limit 1;

-- 7. What is the most common debt indicator across all countries?
select indicator_name, count (*) as frequency
from solution.international_debt_with_missing_values
where indicator_name <> ''
group by indicator_name
order by frequency desc
limit 1;


-- 8. Identify any other key debt trends and summarize your findings.
-- Top 10 debtor counries
select country_name, sum(debt) as total_debt
from solution.international_debt_with_missing_values
where country_name <> '' and debt is not null
group by country_name
order by total_debt desc
limit 10;



















