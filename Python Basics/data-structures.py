# Lists
# students=["Varsha", "Nagashri","Sneha","Mintu"]
# numbers=[1,2,3,4,4,5]
# mixed=[1,"varsha",25.4,True]

# print(students)
# students[1]="Arun"
# students.pop()
# print(students)
# #Length
# print("length of students list array is",len(students))
# #Sum,min,max
# print("Sum of all numbers in Number list is",sum(numbers))
# print("Min number in the numbers list is",min(numbers))
# print("Max number in the numbers list is",max(numbers))
# #Count
# print("Total number of occurences of number 4 is",numbers.count(4))
# #find index
# print("The index of the list item Varsha is",students.index("Varsha"))
# #sort
# students.sort()
# print(students)
# #reverse
# numbers.reverse()
# print(numbers)
# #check membership
# print("Varsha" in students)
# for name in students:
#     print(name)

# print(range(len(students)))
# for i in range(len(students)):
#     print(f"{i}:{students[i]}")

# print(enumerate(students))
# for k,v in enumerate(students):
#     print(f"{k}: {v}")

# squares = []
# for i in range (1,6):
#     squares.append(i** 2)
# print(squares)
# squares =[i ** 2 for i in range(1,6)]
# print(squares)

# Tuple 
# coordinates=(10,20)
# person = ("kavya",25,"tumkur")
# print(person[2])

# name,age,district=person
# print(f"I am {name}, from {district}. I am {age} years old")
# Dictionaries
# mathclass={}
# student={
#     "name":"Varsha",
#     "age":21,
#     "grade":"A"
#     "courses"["Math","Science","Social Science"]
# }
# print(student["name"])
# student["phone"]="8908988900"

# print(student.get("phone,"user's Phone number doesn't exist"))
# student['age']=26
# print(student)
# student.pop("grade")
# print(student)
# for key in student:
# print(f"{key}:{value}"")

# Sets
empty_set=set()
numbers=[1,2,3,1,3,4,3,6,7,888,9]
unique_numbers=set(numbers)
print(numbers)
print(unique_numbers)

unique_numbers.discard(999)