# 📊 Phase 4A: Bucketing and Segmentation in PySpark

## 1. Objective
In this phase, the goal is to understand how continuous data can be converted into categories using PySpark and apply different segmentation techniques to generate meaningful insights.

## 2. Problem Summary
We worked with customer and sales datasets to perform segmentation. The tasks included:
- Reading data from CSV files  
- Joining datasets  
- Calculating total spending and total orders  
- Applying segmentation techniques  
- Comparing different segmentation methods  

## 3. Approach
- Loaded datasets using PySpark  
- Inspected data using show() and printSchema()  
- Joined datasets using customer_id  
- Created full_name using first_name and last_name  

### Transformations:
- Calculated total_spend using sum()  
- Calculated total_orders using count()  
- Applied segmentation techniques:
  - Conditional segmentation using when()  
  - Quantile-based segmentation using approxQuantile()  
  - Bucketizer segmentation (MLlib)  
  - Window-based ranking using percent_rank()  
- Grouped data to count customers in each segment  
- Compared results of different methods  

## 4. Key Transformations Used
- groupBy() → Aggregation  
- agg() → Sum and count  
- join() → Combine datasets  
- withColumn() → Create new columns  
- when() → Conditional logic  
- approxQuantile() → Quantile segmentation  
- Bucketizer → Range-based segmentation  
- Window functions → Ranking (percent_rank())  

## 5. Output / Results
The following outputs were generated:
- Customer segmentation using conditional logic  
- Segment-wise customer count  
- Quantile-based segmentation  
- Bucketizer segmentation  
- Window-based ranking output  

## 6. Data Engineering Considerations
- Used inferSchema for correct data types  
- Avoided duplication during aggregation  
- Applied proper segmentation logic  
- Maintained clean dataset after transformations  

## 7. Challenges Faced
- Understanding segmentation techniques  
- Implementing quantile-based logic  
- Using window functions correctly  
- Comparing different segmentation outputs  

## 8. Learnings
- Learned bucketing and segmentation concepts  
- Implemented multiple PySpark techniques  
- Understood fixed vs data-driven segmentation  
- Used window functions for ranking  
- Compared different analytical approaches  

## 9. Project Files
- solution.py → PySpark implementation  
- phase4a_problem_statement → Problem description  
- OUTPUTS/ → Result screenshots  
- README.md → Documentation  
