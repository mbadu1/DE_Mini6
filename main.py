import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('university_rankings.db')
cursor = conn.cursor()

# Define the INSERT query using parameters for safety
query = '''
INSERT INTO university_rankings (institution, country, year, world_rank, score)
VALUES (?, ?, ?, ?, ?);
'''

# Data to insert
data = ('Duke Tech', 'USA', 2014, 350, 60.5)

# Execute the query
cursor.execute(query, data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")

# Connect to the database
conn = sqlite3.connect('university_rankings.db')
cursor = conn.cursor()

# Define the SELECT query using parameters
query = '''
SELECT COUNT(*) as japanese_universities_top200
FROM university_rankings
WHERE country = 'Japan'
  AND year = 2013
  AND world_rank <= 200;
'''

# Parameters for the query

# Execute the query
cursor.execute(query)

# Fetch the result
result = cursor.fetchone()

# Extract and print the count
count = result[0]
print(f"Number of Japanese universities in the top 200 (2013): {count}")

print(result)

# Close the connection
conn.close()

# Connect to the database
conn = sqlite3.connect('university_rankings.db')
cursor = conn.cursor()

# Define the UPDATE query using parameters
query = '''
UPDATE university_rankings
SET score = score + 1.2
WHERE institution ='University of Oxford' 
  AND year = 2014;
'''


# Execute the query
cursor.execute(query)

# Commit the changes
conn.commit()

# Print the number of rows updated
print(f"Rows updated: {cursor.rowcount}")

# Close the connection
conn.close()
