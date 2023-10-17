# Measuring-Online-Retail-Sales-Performance
Measuring Online Retail Sales Performance

# Online Retail Sales Performance Analysis

![Retail Image](retail_image.jpg) <!-- You can add an image related to your retail business here -->

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Dataset Columns](#dataset-columns)
- [Sections](#sections)
  - [Section 1: Analyzing Average Revenue Per Year](#section-1-analyzing-average-revenue-per-year)
  - [Section 2: Analyzing Customer Transactions Per Year](#section-2-analyzing-customer-transactions-per-year)
- [How to Run the Analysis](#how-to-run-the-analysis)
- [Interpretation](#interpretation)
- [GitHub Task Description](#github-task-description)

## Introduction

This project focuses on analyzing the performance of an online retail business over a three-year period (2009-2011). We will extract insights from a dataset containing transaction records, such as product sales, customer interactions, and cancellations.

## Dataset Columns

- **Invoice**: A unique 6-digit invoice number (if it starts with 'C', it represents a cancellation).
- **StockCode**: A unique 5-digit product code.
- **Description**: Product name.
- **Quantity**: The quantity of each product per transaction.
- **InvoiceDate**: Date and time of the invoice.
- **UnitPrice**: Unit price of the product in sterling (£).
- **CustomerID**: A unique 5-digit customer ID.
- **Country**: The customer's country of residence.

## Sections

### Section 1: Analyzing Average Revenue Per Year

1. Create a new feature called "Year" to extract the year from the "InvoiceDate" column.
2. Filter the data to include only transactions with a quantity greater than 0 and invoices that don't start with 'C' (cancellations).
3. Calculate the "Revenue" by multiplying the quantity with the price.
4. Calculate and visualize the average revenue per year.
5. Provide an interpretation of the average revenue per year.

### Section 2: Analyzing Customer Transactions Per Year

1. Filter the data for customers who finished their purchases (non-cancelled transactions).
2. Filter the data for customers who canceled their purchases.
3. Calculate the number of finished and canceled transactions for each year.
4. Calculate the cancellation rate for each year (percentage of canceled orders out of all orders).
5. Provide an interpretation of the cancellation rate and the number of transactions per year.


## Interpretation

In the notebook, you will find interpretations of the analysis results, providing insights into the online retail sales performance and customer behavior over the analyzed period.

## GitHub Task Description

For a detailed description of the GitHub task, please refer to the [task description](GitHub-Task-Description.md) file.
