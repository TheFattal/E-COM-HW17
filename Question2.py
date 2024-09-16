import sqlite_lib

# Connect to the SQLite database
db_file = r'C:\Users\David\PycharmProjects\HW17-Fattal-David\E-commerce_db.db'
sqlite_lib.connect(db_file)

# Define and run the queries

# 1. How many customers are there in the table?
query1 = 'SELECT COUNT(*) FROM customers;'
result1 = sqlite_lib.run_query_select(query1)
print("Total number of customers:", result1[0][0])

# 2. What is the average customer age?
query2 = 'SELECT AVG(Age) FROM customers;'
result2 = sqlite_lib.run_query_select(query2)
print("Average customer age:", result2[0][0])

# 3. How many male customers are there? And how many female customers?
query3_male = 'SELECT COUNT(*) FROM customers WHERE Gender = "Male";'
query3_female = 'SELECT COUNT(*) FROM customers WHERE Gender = "Female";'
result3_male = sqlite_lib.run_query_select(query3_male)
result3_female = sqlite_lib.run_query_select(query3_female)
print("Number of male customers:", result3_male[0][0])
print("Number of female customers:", result3_female[0][0])

# 4. How many products do the men buy on average? How many products do women buy on average?
query4_male = 'SELECT AVG("Items Purchased") FROM customers WHERE Gender = "Male";'
query4_female = 'SELECT AVG("Items Purchased") FROM customers WHERE Gender = "Female";'
result4_male = sqlite_lib.run_query_select(query4_male)
result4_female = sqlite_lib.run_query_select(query4_female)
print("Average number of products bought by men:", result4_male[0][0])
print("Average number of products bought by women:", result4_female[0][0])

# 5. How many types of membership are there in the table?
query5 = 'SELECT COUNT(DISTINCT "Membership Type") FROM customers;'
result5 = sqlite_lib.run_query_select(query5)
print("Number of membership types:", result5[0][0])

# 6. How many members are there in each type of membership?
query6 = '''
SELECT "Membership Type", COUNT(*) AS member_count
FROM customers
GROUP BY "Membership Type"
ORDER BY member_count DESC;
'''
result6 = sqlite_lib.run_query_select(query6)
print("Members by membership type:")
for row in result6:
    membership_type = row[0]  # Access first element (Membership Type)
    member_count = row[1]     # Access second element (member_count)
    print(membership_type, member_count)

# 7. How many customers live in New York?
query7 = 'SELECT COUNT(*) FROM customers WHERE City = "New York";'
result7 = sqlite_lib.run_query_select(query7)
print("Number of customers living in New York:", result7[0][0])

# 8. How many customers are there in each city (in descending order from largest to smallest)?
query8 = '''
SELECT City, COUNT(*) AS customer_count
FROM customers
GROUP BY City
ORDER BY customer_count DESC;
'''
result8 = sqlite_lib.run_query_select(query8)
print("Customers by city:")
for row in result8:
    city = row[0]              # Access first element (City)
    customer_count = row[1]   # Access second element (customer_count)
    print(city, customer_count)

# 9. How much did the men spend? How much did the women spend?
query9_male = 'SELECT SUM("Total Spend") FROM customers WHERE Gender = "Male";'
query9_female = 'SELECT SUM("Total Spend") FROM customers WHERE Gender = "Female";'
result9_male = sqlite_lib.run_query_select(query9_male)
result9_female = sqlite_lib.run_query_select(query9_female)
print("Total amount spent by men:", result9_male[0][0])
print("Total amount spent by women:", result9_female[0][0])

# 10. Who is the customer who bought the most products? Who is the customer who bought the fewest products?
query10_max = '''
SELECT "Customer ID", "Items Purchased"
FROM customers
ORDER BY "Items Purchased" DESC
LIMIT 1;
'''
query10_min = '''
SELECT "Customer ID", "Items Purchased"
FROM customers
ORDER BY "Items Purchased" ASC
LIMIT 1;
'''
result10_max = sqlite_lib.run_query_select(query10_max)
result10_min = sqlite_lib.run_query_select(query10_min)
print("Customer who bought the most products:", result10_max[0][0])
print("Customer who bought the fewest products:", result10_min[0][0])

# Close the connection
sqlite_lib.close()
