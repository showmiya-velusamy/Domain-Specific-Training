#Exercise 1
import json
data={'name':'John Doe','age':30,'city':'New York','skills':['Python','Machine Learning','Data Analysis']}
with open(r"C:\Training\data1.json", "w") as file:
    json.dump(data,file)

with open("C:/Training/data1.json", "r") as file:
        loaded_data = json.load(file)
        print(loaded_data)

#Exercise 2
import json
profile = {
    "name": "Jane Smith",
    "age": 28,
    "city": "Los Angeles",
    "hobbies": ["Photography", "Traveling", "Reading"]
}
with open('profile.json', 'w') as file:
    json.dump(profile, file)
print("Profile saved to profile.json")

#Exercise 3
import csv
import json
students_list = []
with open('students.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students_list.append(row)
print(students_list)
with open('students.json', 'w') as file:
    json.dump(students_list, file)
print("Data saved to students.json")

#Exercise 4
import json
import csv
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    headers = data[0].keys()
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print("Data successfully converted to data.csv")
else:
    print("Error: JSON data is not in the expected format.")

#Exercise 5
books:{ [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
        {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
    ]}
import json
with open('books.json', 'r') as file:
    data = json.load(file)
books = data.get('books', [])
for book in books:
    print(book.get('title', 'No title available'))




