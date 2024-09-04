#Exercise1
#1
person={
    'name':'Alice',
    'age':25,
    'city':'New York'
}
#2
print(person)

#Exercise2
#1
print(person['city'])

#Exercise3
#1
person['email']='alice@example.com'
#2
person['age']=26
#3
print(person)

#Exercise4
#1
del person['city']
#2
print(person)

#Exercise5
#1
if 'email' in person:
    print('The email key is present')
else:
    print('Key not found')
#2
if 'phone' in person:
    print('The phone key is present')
else:
    print('Key not found')

#Exercise6
#1
for key, value in person.items():
    print(f"{key}: {value}")
#2
for key in person.keys():
    print(key)
#3
for value in person.values():
    print(value)

#Exercise7
#1
employees = {
       101: {"name": "Bob", "job": "Engineer"},
       102: {"name": "Sue", "job": "Designer"},
       103: {"name": "Tom", "job": "Manager"}
   }
#2
print(employees[102])
#3
employees[104]={'name':'Linda','job':'HR'}
#4
print(employees)

#Exercise8
#1
squared_numbers={z**2 for z in range(1,6)}
#2
print(squared_numbers)

#Exercise9
#1
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
#2
merged_dict= dict1 | dict2
print(merged_dict)

#Exercise10
#1
letters={"a": 1, "b": 2, "c": 3}
value=letters.get('b')
print(value)
#2
letters={"a": 1, "b": 2, "c": 3}
value=letters.get('d',0)
print(value)

#Exercise11
#1
keys = ["name", "age", "city"]
values = ["Eve", 29, "San Francisco"]
#2
dictionary = dict(zip(keys, values))
#3
print(dictionary)

#Exercise12
#1
sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
#2
print(word_count)
