## 1. Objective
In this phase, the goal is to perform end-to-end data processing using PySpark by following the ETL approach and generating meaningful insights from sales and customer data.

## 2. Problem Summary
We worked with customer and sales datasets to analyze data and generate insights. The tasks included:
- Calculating daily sales  
- Generating city-wise revenue  
- Identifying top 5 customers based on spending  
- Finding repeat customers  
- Performing customer segmentation (Gold, Silver, Bronze)  
- Creating a final aggregated reporting table  

## 3. Approach
- Loaded datasets using PySpark (CSV format)  
- Displayed data using show() for verification  

Transformations:
- Calculated daily sales using groupBy()  
- Joined datasets to generate city-wise revenue  
- Identified top customers using sorting and limit()  
- Found repeat customers using aggregation and filtering  
- Applied customer segmentation using when()  
- Combined all results into a final reporting table  
- Saved output as CSV file  

## 4. Key Transformations Used
- groupBy() → Aggregation  
- agg() → Sum and count  
- join() → Combine datasets  
- filter() → Apply conditions  
- orderBy() → Sorting  
- limit() → Top records  
- withColumn() → Create new columns  
- when() → Conditional logic  
- concat() → Combine names  

## 5. Output / Results
The following outputs were generated:
- Daily sales summary  
- City-wise total revenue  
- Top 5 customers  
- Repeat customers (order count > 1)  
- Customer segmentation (Gold, Silver, Bronze)  
- Final reporting table  


## 6. Data Engineering Considerations
- Used joins to combine customer and sales data  
- Applied aggregation functions for accurate insights  
- Used filtering to identify repeat customers  
- Applied conditional logic for segmentation  
- Ensured proper column selection  
- Saved output in structured CSV format  

## 7. Challenges Faced
- Understanding join operations  
- Writing aggregation queries  
- Applying segmentation logic  
- Managing multiple transformations  
- Handling column names  

## 8. Learnings
- Learned complete ETL workflow using PySpark  
- Gained experience with joins and aggregations  
- Generated business insights from raw data  
- Learned customer segmentation  
- Built end-to-end data pipeline  

## 9. Project Files
- solution.py → PySpark implementation  
- README.md → Documentation  
- OUTPUTS/ → Result screenshots  
