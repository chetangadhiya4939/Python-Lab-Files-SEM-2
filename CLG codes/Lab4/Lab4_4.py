import csv
print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")

# Function to write to CSV file
def write_to_csv(filename, data):
  with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


# Function to read from CSV file
def read_from_csv(filename):
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    return list(reader)


# Function to search for password
def search_password(data, user_id):
  for row in data:
    if row[0] == user_id:
      return row[1]
  return None


# Test data
data = [['Sahaj', 'Sahaj@1234'], ['Hill', 'Hill@1234'],
        ['Chetan', 'Chetan@1234']]

# Write data to CSV
write_to_csv('users.csv', data)

# Read data from CSV
read_data = read_from_csv('users.csv')

# Search for password
print(search_password(read_data, 'user2'))  # Output: password2
