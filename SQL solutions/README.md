# CTS ANSI SQL Project

## Overview

This repository contains SQL exercises and solutions completed as part of the CTS Digital Nurture Program. The project demonstrates database creation, table design, data insertion, and SQL query implementation using ANSI SQL concepts.

---

## Technologies Used

- MySQL Workbench
- ANSI SQL

---

## Repository Structure

```
CTS-ANSI-SQL/
│
├── database_setup.sql
├── create_tables.sql
├── insert_data.sql
├── queries.sql
│
├── screenshots/
│   ├── schema.png
│   ├── tables.png
│   ├── insert_data.png
│   ├── query_results_1.png
│   ├── query_results_2.png
│   └── join_query.png
│
└── README.md
```

---

## Database Setup

### Step 1: Create Database

Run the script:

```sql
CREATE DATABASE event_management;
USE event_management;
```

### Step 2: Create Tables

Execute the table creation script to create all required tables.

### Step 3: Insert Sample Data

Run the insert script to populate the tables with sample records.

### Step 4: Execute Queries

Run the queries file to view results and perform analysis.

---

## Tables Included

- Users
- Events
- Sessions
- Registrations
- Feedback

---

## SQL Concepts Covered

- CREATE DATABASE
- CREATE TABLE
- PRIMARY KEY
- FOREIGN KEY
- INSERT INTO
- SELECT Statements
- WHERE Clause
- ORDER BY
- GROUP BY
- Aggregate Functions
  - COUNT()
  - AVG()
  - SUM()
- JOIN Operations
- Date Functions

---

## Sample Queries

### Total Registrations per Event

```sql
SELECT event_id, COUNT(*) AS registrations
FROM registrations
GROUP BY event_id;
```

### Average Rating per Event

```sql
SELECT event_id, AVG(rating) AS avg_rating
FROM feedback
GROUP BY event_id;
```

### Event-wise Registration Count

```sql
SELECT e.title, COUNT(r.reg_id) AS total_registrations
FROM events e
JOIN registrations r
ON e.event_id = r.event_id
GROUP BY e.title;
```

---

## Screenshots

The repository includes screenshots showing:

- Database schema
- Table creation
- Inserted records
- Query execution
- Join query results
- Aggregate query outputs

---

## Learning Outcomes

This project demonstrates:

- Database design
- Relational table creation
- Data manipulation
- SQL query writing
- Aggregate analysis
- Join operations
- Data retrieval techniques

---

## Author

Dharunyadevi S

CTS Digital Nurture Program