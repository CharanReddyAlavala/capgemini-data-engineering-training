# 🚀 Phase 5 – Databricks Olist End-to-End Data Engineering Pipeline

## 📌 Objective

In this phase, we worked with a real-world dataset to build a complete data engineering pipeline using PySpark in Databricks. The objective was to perform data ingestion, transformation, analysis, and generate meaningful insights by integrating multiple datasets.

---

## 📊 Problem Summary

The project uses the Olist e-commerce dataset, which includes multiple tables such as customers, orders, products, order items, and payments.

### Tasks Performed:

* Reading multiple datasets from CSV files
* Joining tables to establish meaningful relationships
* Performing aggregations and calculations
* Applying window functions for advanced analytics
* Creating customer segmentation
* Building a final reporting dataset

---

## ⚙️ Approach

### 🔹 Data Ingestion

* Loaded all datasets using PySpark from Databricks storage
* Verified data using `show()` and schema inspection

### 🔹 Data Integration

* Joined customers, orders, and payments for customer-level analysis
* Joined order items and products for product-level insights

### 🔹 Data Transformation

* Calculated total spend per customer
* Computed daily sales
* Aggregated product sales by category

### 🔹 Window Functions

* Ranked customers within each city
* Calculated running totals of sales
* Identified top-performing products in each category

### 🔹 Customer Segmentation

* Classified customers into Gold, Silver, and Bronze segments based on total spending

### 🔹 Final Dataset

* Created a consolidated report combining customer details, city, total spend, segment, and order count

---

## 🔧 Key Transformations Used

* `groupBy()` for aggregations
* `agg()` for sum and count calculations
* `join()` to merge datasets
* `withColumn()` to create new columns
* `when()` for conditional logic
* Window functions for ranking and cumulative analysis
* `dense_rank()` and `rank()` for ordering
* `to_date()` for date conversion

---

## 📈 Output and Results

* Top 3 customers in each city based on total spending
* Daily sales with running totals
* Top-selling products by category
* Customer lifetime value (total spend)
* Customer segmentation (Gold, Silver, Bronze)
* Final reporting dataset with customer insights

---

## ⚠️ Data Engineering Considerations

* Ensured accurate joins to maintain relationships
* Prevented data duplication during aggregations
* Applied window functions for advanced insights
* Maintained consistency in column naming and data types
* Validated intermediate outputs for correctness

---

## 🚧 Challenges Faced

* Handling large and multiple datasets
* Understanding relationships across tables
* Implementing window functions effectively
* Managing joins without introducing duplicate data
* Ensuring accurate aggregation results

---

## 📚 Learnings

* Gained hands-on experience in building end-to-end data pipelines using PySpark
* Worked with real-world datasets and complex transformations
* Improved skills in joins, aggregations, and window functions
* Learned to build scalable and production-ready reporting datasets

---

## 📂 Project Structure

* `solution/` → PySpark implementation
* `phase5_problem_statement/` → Task details
* `OUTPUTS/` → Results and screenshots
* `README.md` → Project documentation

---

## ✅ Conclusion

This project demonstrates the complete lifecycle of a data engineering pipeline—from data ingestion to insight generation—using PySpark in Databricks. It highlights practical skills in data processing, analytics, and building scalable data solutions.
