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
SQL solutions/
│
├── database_setup.sql
├── create_tables.sql
├── insert_data.sql
├── queries.sql
│
├── screenshots/
│   ├── schemas and tables.png
│   ├── users_table.png
│   ├── events_table.png
│   ├── registrations_table.png
│   ├── insert_data.png
│   ├── query_3.png
│   ├── query_6.png
│   ├── query_20.png
│   └── query_21.png
│   
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

Below are a few sample screenshots from the SQL exercises and queries included in this repository.


### Database schema and Table creation
  <img width="1202" height="1072" alt="schemas and tables" src="https://github.com/user-attachments/assets/c8cc7904-6ee4-4b0b-85d0-d7e8d05a8955" />

  <img width="1204" height="1078" alt="users_table" src="https://github.com/user-attachments/assets/2d2ec335-2e10-456a-93e9-1aec4abcd4e3" />

<img width="1205" height="1076" alt="events_table" src="https://github.com/user-attachments/assets/85161958-e89b-401c-ba78-1eb807b0a3ba" />

<img width="1204" height="1076" alt="registrations_table" src="https://github.com/user-attachments/assets/da29f592-2b7b-41c9-b2c9-fe3c6a707753" />

###  Inserted records
<img width="1920" height="1080" alt="insert_data" src="https://github.com/user-attachments/assets/8dd18e95-52a5-4edf-beb6-ab14467f4982" />

### Query execution
<img width="597" height="479" alt="query_3" src="https://github.com/user-attachments/assets/f2792aef-4989-4634-ac63-6ab9f937c4a3" />

  
### Join query results
<img width="1207" height="1078" alt="query_6" src="https://github.com/user-attachments/assets/38b57c75-43d4-4989-9ab2-53932b3d5874" />

<img width="1203" height="1077" alt="query_20" src="https://github.com/user-attachments/assets/a5065bbe-82ea-42fc-860a-6cbc1192973c" />

<img width="1205" height="1072" alt="query_21" src="https://github.com/user-attachments/assets/af3f39dc-e518-40c5-9624-93eaed8e1fe4" />

> Note: Only a subset of screenshots is shown here. The repository contains solutions for all SQL exercises, including DDL, DML, Joins, Aggregate Functions, Subqueries, Views, Stored Procedures, and Database Design concepts.
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

Dharunyadevi S (B.Tech-IT)

CTS Digital Nurture Program
