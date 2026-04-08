# 🚀 Phase 6 – Spark Playground Exit Sprint (Advanced Practice Lab)

## 📌 Objective

The objective of this phase is to build strong fluency and confidence in PySpark by practicing joins, window functions, date operations, and executing a complete data pipeline before transitioning to Databricks.

---

## 📊 Problem Summary

This phase focuses on hands-on practice using a starter dataset.

### Tasks Performed:

* Practicing different types of joins
* Applying window functions for ranking and analysis
* Performing date-based transformations and aggregations
* Executing a complete data pipeline within a time limit
* Validating results at each step

---

## ⚙️ Approach

### 🔹 Data Ingestion

* Loaded dataset using PySpark
* Inspected data using `show()` and `printSchema()`

### 🔹 Join Operations

* Applied **inner join** to retrieve matching records
* Used **left join** to identify missing values
* Applied **left anti join** to detect invalid foreign keys
* Validated joins by comparing row counts

### 🔹 Window Functions

* Ranked top customers within each city
* Calculated running totals of sales
* Ranked customers based on total spend
* Used `lag()` function to track previous transactions

### 🔹 Date Analysis

* Extracted month from date column
* Calculated monthly sales aggregation
* Computed differences between dates
* Analyzed trends based on monthly data

### 🔹 Pipeline Execution

* Loaded and cleaned data
* Filtered invalid records
* Validated referential integrity
* Joined datasets
* Applied aggregations and window functions
* Saved final output within the given time limit

---

## 🔧 Key Transformations Used

* `join()` → Combining datasets
* `groupBy()` → Aggregations
* `agg()` → Sum and count calculations
* `withColumn()` → Creating new columns
* `filter()` → Removing invalid data
* Window functions → Ranking and running totals
* `lag()` → Accessing previous records
* Date functions → Extracting and transforming date values

---

## 📈 Output and Results

* Valid joined dataset
* Top customers per city
* Running total of sales
* Monthly sales aggregation
* Trend analysis results
* Final pipeline output stored as **phase6_final_detailed_v2**

---

## ⚠️ Data Engineering Considerations

* Validated joins using row counts and null checks
* Ensured referential integrity between datasets
* Handled missing and invalid data before processing
* Maintained correct data types for date operations
* Verified intermediate results at each stage

---

## 🚧 Challenges Faced

* Understanding different join types and their outputs
* Implementing window functions correctly
* Working with date transformations
* Managing time during pipeline execution
* Debugging errors efficiently

---

## 📚 Learnings

* Improved understanding of PySpark transformations
* Gained confidence in joins and window functions
* Learned debugging and data validation techniques
* Increased speed and accuracy in problem-solving
* Developed ability to build complete pipelines independently

---

## 🔍 Reflection Questions

* Which task took the most time?
* What mistakes were made during implementation?
* How were issues debugged?
* Can the pipeline be built independently?
* What areas need improvement?

---

## 📂 Project Structure

* `phase6_problem_statement/` → Task details
* `phase6_dirty_starter/` → Initial dataset and raw files
* `solution/` → PySpark implementation
* `OUTPUTS/` → Result screenshots
* `README.md` → Project documentation

---

## ✅ Conclusion

This phase strengthens practical knowledge of PySpark by focusing on real-time problem solving, efficient data processing, and building complete pipelines under constraints. It prepares for advanced data engineering workflows in Databricks and production environments.

