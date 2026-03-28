# Task 1
import csv

# Task 2
compromised_users = []

# Task 3
with open('passwords.csv') as password_file:

# Task 4
    password_csv = csv.DictReader(password_file)

# Task 5
    for password_row in password_csv:

# Task 6 
#       print(password_row['Username'])

# Task 7
        compromised_users.append(password_row['Username'])

# Task 8
with open('compromised_users.txt', 'w') as compromised_user_file:

# Task 9
    for compromised_user in compromised_users:

# Task 10
        compromised_user_file.write(compromised_user + '\n')