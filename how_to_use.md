# Walmart Sales Analytics Application – How to Use

## Overview
This document provides instructions on how to run and use the Walmart Sales Analytics application (`app.py`). The application allows users to interact with the database through a simple command-line interface and execute five analytical features.

---

## Prerequisites

Before running the application, ensure the following:

- Python is installed
- The `python-oracledb` package is installed
- Oracle Instant Client is installed locally
- Access to an Oracle database (FreeSQL or equivalent)
- The Walmart database tables have been created and populated with data

---

## Required Files

The following files should be present in the same directory:

- `app.py` — Main application script  
- `store.csv` — Store data  
- `date_dim.csv` — Date dimension data  
- `sales_fact.csv` — Sales data  
- `economic.csv` — Economic indicators data  

---

## Database Setup

Before running the application, ensure that:

1. The database schema has been created  
2. The required tables have been loaded with data  

Required tables:
- `Store`
- `Date_Dim`
- `Sales_Fact`
- `Economic_Observation`

---

## Configuration

Open `app.py` and update the following variables with your own Oracle credentials:

```python
DB_USER = "YOUR_USERNAME"
DB_PASS = "YOUR_PASSWORD"
DB_DSN = "YOUR_HOST:PORT/SERVICE_NAME"

LIB_DIR = r"PATH_TO_ORACLE_INSTANT_CLIENT"