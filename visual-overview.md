# 📊 Visual Overview – Credit EDA

This section provides a visual walkthrough of the Exploratory Data Analysis (EDA) performed on both the **Credit Card Dataset** and the **Customer Dataset**.  
The visuals highlight data quality checks, distributions, relationships, and customer behavior patterns.

---

## 🧾 Dataset Summary & Initial Exploration

The analysis starts with understanding the structure and basic characteristics of both datasets.

- Dataset shape and column overview
- Sample records (first 5 rows)
- Unique values for categorical features
- Verification of data completeness

### Credit Card Dataset Summary

[credit_card_dataset.csv](./credit_card_dataset.csv)

### Customer Dataset Summary

[customer_dataset.csv](./customer_dataset.csv)

---



## 📦 Distribution Analysis (Box Plots)

Box plots are used to understand the spread, central tendency, and presence of outliers in key financial variables:

- Credit Limit  
- Total Revolving Balance  
- Total Transaction Amount  
- Annual Fees  

These plots help identify high-value customers and spending variability.

<img width="1284" height="625" alt="Screenshot 2026-01-13 124518" src="https://github.com/user-attachments/assets/77bcc696-d83e-4e8d-aa37-58490b8aa716" />


---

## 🔗 Relationship Analysis (Scatter Plots)

Scatter plots are used to analyze relationships between important numerical features:

- Annual Fees vs Credit Limit  
- Total Transaction Amount vs Credit Limit  
- Total Transaction Amount vs Transaction Volume  

These visuals reveal spending behavior patterns and credit utilization trends.

<img width="1209" height="345" alt="Screenshot 2026-01-13 124752" src="https://github.com/user-attachments/assets/4b573e28-8c1b-498e-8285-5f2be7528e62" />
<p align="center">
  <img width="627" height="331" alt="Screenshot 2026-01-13 12475" src="https://github.com/user-attachments/assets/043bb577-1bb1-4dae-a3e1-13b0b7a241a1" >
</p>


---

## 👥 Customer Demographics & Behavior

Demographic analysis explores the distribution of customer's Age



<img width="1594" height="806" alt="Screenshot 2026-01-13 123719" src="https://github.com/user-attachments/assets/bdaebf0b-ce69-4797-a04a-581acc2fe40d" />


---

## 🏦 Personal Loan Analysis

These plots analyze how personal loan acceptance varies across different customer groups:

- Job role vs Personal Loan
- Education level vs Personal Loan
- Marital status vs Personal Loan
- Gender vs Personal Loan

The analysis highlights which customer segments are more likely to opt for personal loans.

<img width="1242" height="684" alt="Screenshot 2026-01-13 125205" src="https://github.com/user-attachments/assets/7401151f-5418-4e17-ae2f-363798270b90" />



---

## 💰 Income vs Age Analysis

This scatter plot visualizes how customer income is distributed across different age groups, showing income diversity and trends over age.

<img width="1597" height="835" alt="Screenshot 2026-01-13 123729" src="https://github.com/user-attachments/assets/82c300c5-ad83-4c0a-8163-3f286870b747" />


---

## 🔥 Correlation Heatmap

The correlation heatmap summarizes relationships between numerical variables such as:

- Customer age
- Income
- Dependent count
- Satisfaction score

It confirms that most features have weak to moderate correlation, indicating low multicollinearity.

<img width="1614" height="710" alt="Screenshot 2026-01-13 123822" src="https://github.com/user-attachments/assets/f3cec8ea-c641-4751-a50f-772c2f215cd8" />




---

## ✅ Overall Insight

The visual analysis provides a comprehensive understanding of:
- Credit usage patterns
- Customer demographics
- Spending behavior
- Loan acceptance trends

This project demonstrates how structured EDA and visualization can convert raw financial data into meaningful insights.
