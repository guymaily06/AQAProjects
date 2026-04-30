'''
Create a class Student with three attributes: name, age, and grade.

Initialize them through __init__. Create two student objects and print their attributes.

Add a method introduce() to the Student class that prints: "Hi, I'm Alice. I'm 16 years old and my grade is 90."

Add a method is_passing() that returns True if grade is 60 or higher, False otherwise. Test with two students.

student_1 = Student(“Bob”, 21, {"math": 90, "english": 85, "science": 92})

Modify the class so that instead of a single grade, each student has a dictionary grades with subject names as keys.
Add a method average_grade() that returns the average of all grades.

Add a method add_grade(subject, grade) that adds a new subject and its grade to the student's grades dictionary.
Add another method update_grade(subject, new_grade) that changes an existing grade. If the subject doesn't exist, print a message.

def update_grade (subject, new_grade):
#assuming the new_grade is the corrected grade
self.grades.get(subject, "Student is not enrolled in that subject")

'''

class Student:

    def __init__  (self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def greeting (self):
        print (f"Hi, I'm {self.name}. I'm {self.age} years old and my grade is {self.grades}")

    def is_passing (self):
        if self.average_grade() >= 60:
            return True
        else:
            return False

    def average_grade (self):
        no_of_classes = len(self.grades)
        total = 0
        for key, value in self.grades.items():
            total += value
            average = total / no_of_classes
        return average

    def add_grade (self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = grade
        else:
            print (f"Student already enrolled in {subject}.")
        return self.grades

    def update_grade(self, subject, new_grade):
        # assuming the new_grade is the corrected grade
        if subject in self.grades:
            self.grades[subject] = new_grade
        else:
            print ("Student is not enrolled in that subject")
        return self.grades

    def info (self):
        print (f"{self.name} studies at {Student.school_name}")

    def __str__(self):
        return f"Student: {self.name} is {self.age} year(s) old with an average of {self.average_grade()}."


class Classroom:
    def __init__ (self, name):
        self.students = []
        self.name = name

    def add_student (self, new_student):
        if new_student not in self.students:
            self.students.append(new_student)
        else:
            print (f"Student already enrolled in {new_student}.")
        return self.students

    def class_info(self):
        for student in self.students:
            print(student)

    def class_average(self):
        total = 0
        for student in self.students:
            total += student.average_grade()
            average = total / len(self.students)
        print (average)

    def top_student (self):
        max = 0
        the_greatest = ""
        for student in self.students:
            if student.average_grade() > max:
                the_greatest = student.name
                max = student.average_grade()
        return the_greatest




'''
Add a class variable school_name = "Greenwood High" that's shared across all students. 
Add a method info() that prints something like: "Alice studies at Greenwood High."
Then change Student.school_name to a different value and verify it changes for all students.

Add the special method __str__ to the class so that print(student) displays a readable string like:
 
 "Student(name=Alice, age=16, average=89.0)". Test with print(student_1).
 
 Create a separate class Classroom that has:
An attribute students (a list of Student objects)
! A method add_student(student) to add one:
    Each of these are student objects. They will have the associated age(int) and classes (dictionary)
A method class_average() that returns the average grade across all students:
    Each student has the method average_grade() to calculate this (calling that method)
    Need to "calculate" len(classroom) to average the averages
    
    
A method top_student() that returns the Student object with the highest average
    Max option for a dictionary of the students and averages
    
Build a School class that manages multiple Classroom objects. It should:
Have a name and a dictionary of classrooms (key = classroom name, value = Classroom object)
Method add_classroom(name) — creates a new empty classroom
Method enroll(classroom_name, student) — adds a student to the named classroom
    
Method school_report() — returns a dictionary with: total students, school-wide average, 
and a dict of {classroom_name: top_student_name}
Handle errors: if you try to enroll in a classroom that doesn't exist, raise a ValueError with a clear message
'''
class School:
    def __init__ (self, name, class_dict):
        self.name = name
        #class_dict has key = classroom name value = classroom object
        self.class_dict = {}

    def add_classroom (self, name):
        year = Classroom (name)
        if name not in self.class_dict:
            self.class_dict[name] = year
        else:
            print (f"This class is already in the school {self.name}.")
    def school_info (self):
        print (self.name)
        print (len(self.class_dict))
        for value in self.class_dict.values():
            print (value)

    def enroll (self, classroom_name, student):
        if classroom_name in self.class_dict:
            self.class_dict[classroom_name].add_student(student)
        else:
            self.class_dict[classroom_name] = student
        return self.class_dict

#student_1 = Student ("John", 18, {"math": 80, "english":85, "science":90})
#student_2 = Student ("Alice", 17, {"math": 88, "english":95, "science":90})
#student_1.greeting()
#student_2.greeting()

#print (student_1.is_passing())
#print (student_2.is_passing())

#print (student_1.average_grade())
#print (student_2.average_grade())

'''
student_1.add_grade("computers", 85)
student_2.add_grade("computers", 85)

student_1.update_grade("english", 90)
student_2.update_grade("math", 85)

student_1.greeting()
student_2.greeting()

student_2.info()
student_1.info()
'''
'''student_1 = Student ("Alice", 17, {"math": 88, "english":95, "science":90})
student_2 = Student ("John", 17, {"math": 68, "english":55, "science":90})
senior_class = Classroom("Class of '26")
senior_class.add_student(student_1)
senior_class.add_student(student_2)
'''

#senior_class.class_average()
#print (senior_class.top_student())
senior_class = Classroom("Class of '26")
greenwood = School ("Greenwood High",{})
greenwood.add_classroom(senior_class)
#Enrollment starts here. Need to "fill" the classroom with students
greenwood.school_info()
'''
student_3 = Student ("Matt", 18, {"english":99, "science":95})
student_3.add_grade("math", 99)
greenwood.enroll("Class of '27", student_3)
greenwood.school_info()
'''