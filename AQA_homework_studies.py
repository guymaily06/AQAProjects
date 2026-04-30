#Task 1 (Write a program that stores a person's age. If the age is less than 13, print "Child".
# If the age is between 13 and 17, print "Teenager". If 18 or older, print "Adult".)

'''
if age < 13:
    print ("Child")
elif age >= 13 and age <= 17:
    print ('Teenager')
else:
    print ('Adult')
'''
from operator import index
from re import fullmatch

#Task 2 ( Write a program that checks a temperature variable. If temp is above 30, print "It's hot!".
# If temp is between 15 and 30, print "Nice weather.". If below 15, print "It's cold!".

'''
if temp > 30:
    print ("It's hot!")
elif temp <= 15 and temp <= 30:
    print ('Nice weather.')
else:
    print ("It's cold!")
    
'''

#Task 3 Create a list with 5 of your favorite cities.
# Write a for loop that prints each city name with its position number. For example: '1. Paris', '2. Tokyo', etc.
'''
favorite_cities = ["Rome", "Milwaukee", "Nashville", "Opelika", "Napa"]

for city in favorite_cities:
    print (f"{favorite_cities.index(city)+1}, {city}")

'''

#Task 4 Write a for loop that goes through numbers from 1 to 20. Print only the even numbers.
'''
for i in range (1, 21):
    if i % 2 == 0:
        print (i)
'''


#Task 5 Write a while loop that starts with a number = 100.
# Each iteration, divide the number by 2 (number = number / 2) and print it. Stop the loop when the number drops below 1.

"""
num = int(input("Enter a number: "))
while num > 1:
    print (num)
    num /= 2

"""


#Task 6 Write a program that uses a while loop to find the first number greater than 100 that is divisible by 7.
# Print that number.
"""
num = int(input("Enter a number: "))
while num % 7 != 0:
    num += 1
print (num)
"""

#Week 2 Day 1

#Task 1 Write a function called show_menu() that prints a simple menu with 3 items: '1. Start', '2. Settings',
# '3. Exit'. Call it twice.

"""
def show_menu():
    print ("1. Start")
    print ("2. Settings")
    print ("3. Exit")

show_menu()
show_menu()
"""


#Task 2Write a function called full_name(first, last) that
# takes a first name and a last name and prints them together as 'First Last'. Call it three times with different names.

'''
def full_name (first, last):
    print (f"{first} {last}")

full_name("Guy", "Maily")
full_name("John", "Jacob")
full_name("Jingleheimer", "Schmidt")
'''

# Task 3 Write a function called is_adult(name, age) that prints
# 'name is an adult' if age >= 18, otherwise prints 'name is not an adult yet'. Call it with at least 3 different inputs.

''' 
def is_adult (name, age):
    adult = "is an adult"
    not_adult = "is not an adult"
    if age >= 18:
        print (f"{name} {adult}")
    else:
        print(f"{name} {not_adult}")

is_adult("Guy", 18)
is_adult("Jacob", 17)
is_adult("Jacob", 18)

'''

#Task 4 Write a function called calculate_discount(price, percent)
# that returns the discounted price. For example, calculate_discount(100, 20) should return 80.0. Print the result.

''' 
def calculate_discount (price, percent):
    new_price = price * (1 - (percent/100))
    print (new_price)

calculate_discount(100, 20)
calculate_discount(100, 30)
calculate_discount(100, 40)

'''

#Task 5 Write a function called max_of_two(a, b) that returns the larger of two numbers.
# Test it with several pairs of numbers.

'''
def max_of_two (a, b):
    if a > b:
        print (a)
    else:
        print (b)

max_of_two(20, 30)
max_of_two(40, 50)
max_of_two(30, 40)
max_of_two(50, 40)
max_of_two(300, 40)
max_of_two(-400, 4)
'''

#Task 6 Write a function called power(base, exponent=2) that returns base raised to the exponent.
# By default it should calculate the square. Test: power(5) should return 25, power(2, 3) should return 8.

'''
def power (base, exponent=2):
    return base ** exponent

print (power(2, 2))
print (power(2, 3))
print (power(3, 4))
'''

#Task 7 Write a function called find_longest(words)
# that takes a list of strings and returns the longest one. Test it with a list of 5 words.

'''
def find_longest (words):
    word_1 = ""
    for word in words:
        if len (word) > len(word_1):
            word_1 = word
    return word_1

words = ["hi", "open", "worldly", "old", "newer"]
print (find_longest(words))
'''

#Task 8 Write a function called sum_above(numbers, threshold) that takes a list of numbers and a threshold value, and
# returns the sum of all numbers that are above the threshold. Test: sum_above([10, 20, 30, 40], 25) should return 70.

'''def sum_above (numbers, threshold):
    sum = 0
    for number in numbers:
        if number > threshold:
            sum += number
    return sum

numbers = [10, 20, 30, 40]
print (sum_above(numbers, 25))
'''

#Task 9 Rewrite your introduce(name, age) function from earlier using f-strings.
# Add a third parameter, city, with a default value.
# Print something like: 'My name is Alice, I am 25 years old, and I live in London.'


'''
def introduce (name, age, city="Columbia"):
    print (f"My name is {name}, and I am {age} years old, and I live in {city}.")

introduce("Alice", 25, "London")
'''

#AQA MOD 2 WEEK 2 DAY 2

#TASK 1 Create a dictionary called car with keys: brand, model, year, and color.
# Print each value. Then change the color and add a new key "mileage" with value 15000. Print the updated dictionary.


'''
car = {"brand": "Toyota", "model": "Prius", "year": 2018, "color": "green"}
for key, value in car.items():
    print (value)
car ["color"] = "blue"
car ["mileage"] = 15000

print ("\n")


for key, value in car.items():
    print (key, value)

'''

#Task 2 Create a dictionary called grades with 4 student names as keys and their scores as values.
# Loop with .items() and print each student and grade. Then print only students who scored 80 or above.

'''
grades = {"John": 98, "Alice": 85, "Jane": 99, "Caleb": 70}
for key, value in grades.items():
    print (key, value)

for key, value in grades.items():
    if value >= 90:
        print (f"{key} has a grade greater than 90")
'''

#Task 3 Create a list of 3 product dictionaries with keys: name, price, in_stock (True/False).
# Loop and print only products that are in stock and cost less than 100.

'''
stories = [
    {
        "name": "Stretch", "price": 15.00, "in_stock": True
    },
    {
        "name": "Xbox", "price": 850.00, "in_stock": True
    },
    {
        "name": "Game Boy", "price": 150, "in_stock": False
    }
]


selected_products = []

for product in stories:

    if product["in_stock"] == True and product["price"] < 100:
        selected_products.append(product["name"])

for item in selected_products:
    print (item)

'''

#Task 4 Create a nested dictionary called school with keys "math" and "english".
# Each should contain a sub-dict with "teacher" (string) and "students" (list of names).
# Print the math teacher and all English students.

'''school = {
    "math": {
        "teacher" : "John",
        "students": ["Lisa","Elizabeth", "Jane"]
    },
    "english": {
        "teacher" : "Zachary",
        "students": ["John","Barry", "Wally"]
    }
}

print (school["math"]["teacher"])
print (school["english"]["students"])
'''


# Task 5 Write a function analyze_grades(grades) that takes a list of grades and returns
# a tuple of 3 values: the average, the minimum, and the maximum.
# Test it with [85, 72, 91, 68, 79] and unpack the result into 3 variables.



'''
def analyze_grades (grades):
    total = 0
    start = []
    low_end = min(grades)
    high_end = max(grades)
    for grade in grades:
        total += grade
    average = total/len(grades)
    start.append(average)
    start.append(low_end)
    start.append(high_end)
    start_tuple = tuple(start)
    return start_tuple


grades = [85, 72, 91, 68, 79]
x = analyze_grades(grades)
lowest = min(x)
highest = max(x)
print (analyze_grades(grades))
print (f"Minimum: {lowest}, Max: {highest}")


'''

#Task 6 Write a function safe_divide(a, b) that returns a / b. Handle ZeroDivisionError (return 0) and
# TypeError (print an error message and return None). Test with: safe_divide(10, 3), safe_divide(10, 0),
# safe_divide('hello', 5).

'''
def safe_divide (a, b):
    try:
        result = a / b
        print (f"{a}/ {b} = {result}")
    except ZeroDivisionError:
        print (f"Error: division by zero!")
    except TypeError:
        print (f"Inputs must be numbers.")
    finally:
        print ("Operation complete!\n")

safe_divide(10, 3)
safe_divide(10, 1)
safe_divide(10, 0)
safe_divide('hello', 1)
'''


#Type 7 Write a function safe_get(dictionary, key) that tries to return dictionary[key].
# If the key doesn't exist, return 'N/A'. Test it with a dictionary that has some keys present and some missing.

'''
def safe_get (dictionary, key):
    try:
        print  (dictionary[key])
    except KeyError:
        print ("N/A")

dct_1 = {"key1": 1, "key2": 2}
dct_2 = {"key3": 1, "key4": 2}

safe_get(dct_1, "key1")
safe_get(dct_2, "key2")

'''

#Bonus task: In test automation, you often need to read test data from files or write results to files. Python makes this easy with open().


'''
with open("test_results.txt", "w") as file:
    file.write("Test 1: PASSED\n")
    file.write("Test 2: FAILED\n")
    file.write("Test 3: PASSED\n")
print("File written!")

File written!
"w" - write mode. Creates the file or overwrites it if it exists.
with ... as file: - the with block automatically closes the file when done.
\n - adds a new line character at the end of each string.
Reading from a File
with open("test_results.txt", "r") as file:
    for line in file:
        print(line.strip())
Test 1: PASSED
Test 2: FAILED
Test 3: PASSED
.strip() removes the newline character at the end of each line. Without it you'd get blank lines between results because the file has \n and print() adds another.

Combine reading with try/except to handle missing files:

try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Check the filename.")
File not found! Check the filename.

'''

#Task 8 Write a function save_results(filename, results) that writes each item in the results list to the file on a new line.
# Then write read_results(filename) that reads the file and returns a list of strings (one per line).
# Use try/except for FileNotFoundError in the read function. Test both.


'''def save_results (filename, results):
    with open(filename, "w") as file:
        for line in file:
            file.write(f"{line},\n")
    print ("File written!")


def read_results (filename):
    try:
        with open("missing.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found! Check the filename.")



results = ["hello", "Great day", "world star runner"]
save_results("test_results.txt", results)
read_results("test_results.txt")


'''


'''
def student_average(students, name):
    avg = 0
    total = 0
    # standardizing the name that is being searched to eliminate the possiblity of not matching capitalizations
    searching = name.lower()
    for key, value in students.items():
        # key.lower() should be making the key lowercase to match the searching variable
        if key.lower() == searching:
            # looping through the values and adding them to the total
            for value in students[key].values():
                total += value
            avg = total / len(students[key])
    return avg

'''
# Start of homework going into 30 APR 26
'''
Write a function class_report(students) that returns a dictionary with the following info:
!"top_student" — name of the student with the highest overall average 

!"class_average" — average grade across all students and all subjects (?)
!"subject_averages" — a dictionary with the average grade for each subject across all students
!"failed_subjects" — list of (student_name, subject) pairs where the grade is below 75

building the function:

First step is to get each student's total average. 
To do this, I need to go into the students directory at level 1, that will make the "key" 
at this level "Alice", "Bob", and "Charlie".
key, value in student.items():
At this key, for each key in the sub-dictionary, adding the sub-value to the total for that item

'''

'''
def best_in_subject(students, subject):
    # Creating dictionary of student names with values of grade for the subject
    competitors = {}
    for key, value in students.items():
        for k, v in students[key].items():
            if k == subject:
                competitors[key] = v
    return max(competitors, key=competitors.get)


def highest_average (students):
    student_averages = {}
    # pushing the students dictionary into this to find the average of each student
    for key, value in students.items():
        # creating a variable for the # of classes, to calculate the average
        no_of_classes = len(students[key])
        # cycling through the variables,
        total = 0
        for k, v in students[key].items():
            total += v
            avg = total / no_of_classes
        student_averages[key] = avg
    return max(student_averages, key=student_averages.get)

def class_average (students):
    total = 0
    for key, value in students.items():
        number_of_students = len(students)
        for k, v in value.items():
            number_of_classes = len(students[key])
            total += v
        full_average = total / (number_of_students*number_of_classes)
    return {full_average}

def subject_average (students):
    total = 0
    #create a dictionary that consolidates all the classes
    class_name = {}
    for key, value in students.items():
        number_of_students = len(students)
        for k, v in students[key].items():
            if k not in class_name:
                class_name[k] = total
            class_name[k] += v
    for key, value in class_name.items():
        class_name[key] = value / number_of_students
    return (class_name)

def failed_subjects (students):
    # I know I could just create a dictionary with each of these
    # items then force Python to do the conversion, but
    # that seems too easy and... I kind of just want to do it this way
    # so it prints the list on each occurence of a failure
    failed_students = []
    for key, value in students.items():
        for k, v in value.items():
            if v < 75:
                failed_students.append(key)
                failed_students.append(k)
    return (failed_students)

def class_report(students):
    print (highest_average(students))
    print (class_average(students))
    print (subject_average(students))
    print (failed_subjects(students))



students = {
    "Alice": {"math": 90, "english": 85, "science": 92},
    "Bob": {"math": 70, "english": 75, "science": 80},
    "Charlie": {"math": 88, "english": 92, "science": 78}
}


class_report(students)

'''


'''
Write a function merge_inventories(store_a, store_b) that takes two 
dictionaries representing item counts in two stores and returns a single 
dictionary with the total count of each item. If an item exists in only one store, 
include it as-is.

store_a = {"apple": 10, "bread": 5, "milk": 8}
store_b = {"apple": 3, "milk": 7, "cheese": 4}

Expected output: {'apple': 13, 'bread': 5, 'milk': 15, 'cheese': 4}

'''
def merge_inventories (store_a, store_b):

    for key, value in store_b.items():
        if key not in store_a:
            store_a[key] = value
        else:
            store_a[key] += value
    return store_a

store_a = {"apple": 10, "bread": 5, "milk": 8}
store_b = {"apple": 3, "milk": 7, "cheese": 4}

print (merge_inventories(store_a, store_b))