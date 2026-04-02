
## Objective  
Perform end-to-end data processing using PySpark by following the ETL approach and generating meaningful insights from the data.

---

## Problem Summary  
Worked with customer and sales datasets in multiple formats (CSV, JSON, Parquet).  

Tasks performed:
- Reading data from different sources  
- Cleaning and filtering data  
- Performing transformations and aggregations  
- Generating insights like daily sales and city-wise revenue  
- Identifying repeat and top customers  

---

## Approach  
- Loaded datasets using PySpark  
- Checked data using `show()` and `printSchema()`  
- Removed null and invalid records  
- Worked with multiple formats (CSV, JSON, Parquet)  
- Applied transformations like aggregation and joins  
- Used window functions for ranking  

---

## Key Transformations  
- `groupBy()` and `agg()` → aggregation  
- `join()` → combining datasets  
- `filter()` and `dropna()` → cleaning data  
- `withColumn()` and `when()` → transformations  
- Window functions → ranking customers  

---

## Results  
- Daily sales summary  
- City-wise revenue  
- Repeat customers  
- Top customer in each city  
- Final aggregated report  

(All outputs are in the **OUTPUTS** folder)

---

## Challenges  
- Handling missing and inconsistent data  
- Writing window functions  
- Managing multiple file formats  
- Understanding transformations  

---

## Learnings  
- End-to-end ETL using PySpark  
- Data cleaning and validation  
- Working with multiple data formats  
- Using window functions for analysis  

---

## Project Structure  
- `solution/` → PySpark ETL code  
- `phase3_problem_statement/` → Problem description  
- `OUTPUTS/` → Output screenshots  
- `README.md` → Documentation  
