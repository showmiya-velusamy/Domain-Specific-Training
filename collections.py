#Exercise 1
# 1. Create a list called numbers
numbers = [1, 2, 3, 4, 5]
# 2. Append the number 6 to the list
numbers.append(6)
# 3. Remove the number 3 from the list
numbers.remove(3)
# 4. Insert the number 0 at the beginning of the list
numbers.insert(0, 0)
# 5. Print the final list
print(numbers)

#Exercise 2
# 1. Create a tuple called coordinates
coordinates = (10.0, 20.0, 30.0)
# 2. Access and print the second element of the tuple
print(coordinates[1])
# 3. Try to change the third element of the tuple to 40.0
# Tuples are immutable, so this will raise a TypeError if attempted:
# coordinates[2] = 40.0  # Uncommenting this line will cause an error

#Exercise 3
# 1. Create a set called fruits
fruits = {"apple", "banana", "cherry"}
# 2. Add "orange" to the set
fruits.add("orange")
# 3. Remove "banana" from the set
fruits.remove("banana")
# 4. Check if "cherry" is in the set and print a message
if "cherry" in fruits:
    print("Cherry is in the set.")
else:
    print("Cherry is not in the set.")
# 5. Create another set called citrus
citrus = {"orange", "lemon", "lime"}
# 6. Perform a union of fruits and citrus and print the result
union_set = fruits.union(citrus)
print(union_set)
# 7. Perform an intersection of fruits and citrus and print the result
intersection_set = fruits.intersection(citrus)
print(intersection_set)

#Exercise 4
# 1. Create a dictionary called person
person = {"name": "John", "age": 30, "city": "New York"}
# 2. Access and print the "name" key from the dictionary
print(person["name"])
# 3. Update the "age" key to 31
person["age"] = 31
# 4. Add a new key-value pair "email": "john@example.com"
person["email"] = "john@example.com"
# 5. Remove the "city" key from the dictionary
del person["city"]
# 6. Print the final dictionary
print(person)

#Exercise 5
# 1. Create a dictionary called school
school = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 78, "Science": 92},
    "Charlie": {"Math": 95, "Science": 88}
}
# 2. Print the grade of "Alice" in "Math"
print(school["Alice"]["Math"])
# 3. Add a new student "David"
school["David"] = {"Math": 80, "Science": 89}
# 4. Update "Bob"'s "Science" grade to 95
school["Bob"]["Science"] = 95
# 5. Print the final school dictionary
print(school)

#Exercise 6
# 1. Given a list of numbers
numbers = [1, 2, 3, 4, 5]
# 2. Use list comprehension to create a new list where each number is squared
squared_numbers = [x**2 for x in numbers]
# 3. Print the new list
print(squared_numbers)

#Exercise 7
# 1.Create a set comprehension that generates a set of squared numbers
squared_set = {x**2 for x in [1, 2, 3, 4, 5]}
# 2. Print the resulting set
print(squared_set)

#Exercise 8
#1. Create a dictionary comprehension that generates a dictionary
cubes = {x: x**3 for x in range(1, 6)}
# 2. Print the resulting dictionary
print(cubes)

#Exercise 9
# 1. Create two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "Paris"]
# 2. Use the zip() function to combine keys and values into a dictionary
combined_dict = dict(zip(keys, values))
# 3. Print the resulting dictionary
print(combined_dict)

#Exercise 10
# 1. Write a Python program to count occurrences of each word
sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
# 2. Print the resulting dictionary with word counts
print(word_count)

#Exercise 11
# 1. Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# 2. Find and print the unique elements in both sets combined
unique_elements = set1.union(set2)
print(unique_elements)
# 3. Find and print the common elements between the two sets
common_elements = set1.intersection(set2)
print(common_elements)
# 4. Find and print the elements that are only in set1 but not in set2
only_in_set1 = set1.difference(set2)
print(only_in_set1)

#Exercise 12
# 1. Create a tuple with three elements
person_tuple = ("Alice", 25, "Paris")
# 2. Unpack the tuple into three variables
name, age, city = person_tuple
# 3. Print the variables to verify the unpacking
print(name)
print(age)
print(city)

#Exercise 13
# 1. Write a Python program to count the frequency of each letter
text = "hello world"
letter_count = {}
for letter in text:
    if letter != " ":  # Exclude spaces from counting
        letter_count[letter] = letter_count.get(letter, 0) + 1
# 2. Print the resulting dictionary with letter frequencies
print(letter_count)

#Exercise 14
# 1. Given a list of tuples representing students and their grades
students = [("Alice", 90), ("Bob", 80), ("Charlie", 85)]
# 2. Sort the list by grades in descending order
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
# 3. Print the sorted list
print(students_sorted)