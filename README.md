# COP-3710 - Walmart Retail Sales Analytics Database

## Project Scope
This project designs a retail analytics database using Walmart weekly sales data along with related economic and weather indicators. The database is structured to support business intelligence reporting, sales trend analysis, and store-level performance evaluation across time.

## Target Users
- Students and Researchers
- Data Analysts
- Business Intelligence Teams
- Database / Data Engineering Students

## Data Source
Dataset: [Walmart Dataset](https://www.kaggle.com/datasets/yasserh/walmart-dataset)

This project is based on a Walmart dataset containing:
- Store
- Date
- Weekly Sales
- Holiday Flag
- Temperature
- Fuel Price
- CPI
- Unemployment

## Project Overview
The Walmart Retail Sales Analytics Database is a relational database project built from Walmart weekly sales data. The goal of the project is to organize the source dataset into a structured database schema that supports querying, reporting, and analysis of retail performance across stores and dates.

The project uses a CSV-driven workflow:
1. `Walmart.csv` serves as the raw input dataset
2. `preprocess.py` cleans and transforms the source data
3. Cleaned CSV files are generated for each table
4. `generate_dataload.py` creates `dataload.sql` from the processed CSV files
5. Oracle SQL scripts create and populate the database

This approach ensures that the database is loaded from the actual source data rather than hard-coded sample records.

## Database Design
The schema is designed around five main tables:

- **Store**
- **Date_Dim**
- **Sales_Fact**
- **Weather_Observation**
- **Economic_Observation**

This design separates store information, date-based attributes, sales records, weather observations, and economic indicators into related tables for better organization and analysis.

## Features
- Relational schema based directly on the Walmart dataset
- CSV preprocessing using Python
- Automatically generated SQL dataload script
- Separate tables for sales, weather, and economic observations
- Support for SQL queries on sales trends and store performance
- Clean ER diagram reflecting the implemented schema

## User Groups
- Retail Analysts
- Business Intelligence Teams
- Students learning relational database design
- Data Analysts
- Database Administrators / Instructors reviewing ETL workflow

## Files Included
- `Walmart.csv` - raw source dataset
- `preprocess.py` - cleans and transforms the source data
- `generate_dataload.py` - generates SQL insert statements from processed CSV files
- `create_db.sql` - creates the database schema in Oracle
- `dataload.sql` - loads the generated data into Oracle
- `ERDiagram.png` - entity relationship diagram for the final schema

## How to Run
1. Place `Walmart.csv` in the project folder
2. Run:
   ```bash
   python3 preprocess.py
   python3 generate_dataload.py
