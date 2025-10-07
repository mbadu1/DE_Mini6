
# Week 6 Mini-Assignment: Introduction to Databases

## Project Overview
This project demonstrates basic database operations using SQLite and the University Rankings dataset (2012-2015). The assignment covers database connectivity, CRUD operations, and basic SQL analysis.

## Setup Instructions

### 1. Download the Database
- Download the SQLite database from the provided Google Drive link
- Save it as `university_rankings.db` in your project directory

### 2. Connect to Database
Using Command Line:
```bash
sqlite3 university_rankings.db
```

Using Python:
```python
import sqlite3
conn = sqlite3.connect('university_rankings.db')
cursor = conn.cursor()
```

Using DBeaver or other GUI tools:
- Open DBeaver
- Create new connection → SQLite
- Browse to your database file

## CRUD Operations Documentation

### 1. CREATE (Insert) - Adding Duke Tech University

**Operation:** Insert a new university record for Duke Tech in 2014

**SQL Query:**
```sql
INSERT INTO rankings (institution, country, year, world_rank, score)
VALUES ('Duke Tech', 'USA', 2014, 350, 60.5);
```

**Changes Made:**
- Added 1 new row to the rankings table
- Institution: Duke Tech
- Country: USA
- Year: 2014
- World Rank: 350
- Score: 60.5

### 2. READ (Query) - Japanese Universities Analysis

**Operation:** Count Japanese universities in the global top 200 for 2013

**SQL Query:**
```sql
SELECT COUNT(*) as japanese_universities_top200
FROM rankings
WHERE country = 'Japan' 
  AND year = 2013 
  AND world_rank <= 200;
```

**Findings:**
- [Number] Japanese universities appeared in the global top 200 rankings for 2013
- This represents approximately [percentage]% of the top 200 universities

### 3. UPDATE - Correcting Oxford's Score

**Operation:** Increase University of Oxford's 2014 score by 1.2 points

**SQL Query:**
```sql
UPDATE rankings
SET score = score + 1.2
WHERE institution = 'University of Oxford' 
  AND year = 2014;
```

**Changes Made:**
- Updated 1 row in the rankings table
- University of Oxford's 2014 score changed from [original_score] to [new_score]
- This correction adjusts for the previously miscalculated score

### 4. DELETE - Removing Low-Scoring Universities

**Operation:** Remove universities with scores below 45 in 2015

**SQL Query:**
```sql
DELETE FROM rankings
WHERE year = 2015 
  AND score < 45;
```

**Changes Made:**
- Removed [number] rows from the rankings table
- All deleted records were from 2015 with scores below 45
- This cleanup ensures only universities meeting the minimum score threshold remain

## Basic Analysis Performed

### Database Structure
```sql
PRAGMA table_info(rankings);
```
The rankings table contains the following columns:
- institution (TEXT): University name
- country (TEXT): Country location
- year (INTEGER): Ranking year
- world_rank (INTEGER): Global ranking position
- score (FLOAT): Overall score

### Summary Statistics

**Universities per Year:**
```sql
SELECT year, COUNT(*) as university_count
FROM rankings
GROUP BY year
ORDER BY year;
```

Results:
- 2012: [count] universities
- 2013: [count] universities
- 2014: [count] universities
- 2015: [count] universities

**Top Countries by Average Score:**
```sql
SELECT country, AVG(score) as avg_score
FROM rankings
GROUP BY country
ORDER BY avg_score DESC
LIMIT 10;
```

## File Structure
```
project/
├── README.md                  # This documentation file
├── university_rankings.db     # SQLite database file
├── queries/
│   ├── 01_insert.sql         # Insert operation
│   ├── 02_read.sql           # Read/query operation
│   ├── 03_update.sql         # Update operation
│   ├── 04_delete.sql         # Delete operation
│   └── 05_analysis.sql       # Additional analysis queries
└── screenshots/              # Optional: GUI screenshots
```

## Technologies Used
- SQLite 3
- SQL (Structured Query Language)
- Optional: DBeaver (Database GUI)
- Optional: Python with sqlite3 library

## Key Learning Outcomes
1. **Database Connectivity:** Successfully connected to SQLite database using multiple methods
2. **CRUD Operations:** Implemented all four fundamental database operations
3. **SQL Proficiency:** Wrote complex queries including filters, aggregations, and joins
4. **Data Analysis:** Performed basic statistical analysis on the dataset
5. **Documentation:** Created comprehensive documentation of database changes

## Future Improvements
- Add data validation before insert operations
- Implement transaction management for multiple operations
- Create backup before delete operations
- Add indexing for performance optimization
- Implement error handling for database operations



## Author
Michael Kofi Badu