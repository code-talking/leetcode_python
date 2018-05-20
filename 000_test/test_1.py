# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/17/18
    Time:   8:24 PM
    Package 
    File    test_1.py
    Description
    
'''
def p():
    print('--------------------------------------------')

# a = [1, 2, 3, 4, 5]
# print(a)
#
# b = [x ** 2 for x in a]
# print(b)
# p()

students = [
    ('John', 'A', 15),
    ('Jane', 'B', 20),
    ('Dave', 'A', 12),
    ('Peter', 'C', 4)
]

print(students)
print(id(students))
p()

sorted(students, key = lambda students: students[2])
print('students的地址\t\t\t', id(students))
print('sorted(students)的地址\t\t', id(sorted(students, key = lambda students: students[2])))
p()

students.sort(key = lambda students : students[2])
print('using list.sort()')
print(students)
print(id(students))
p()
p()

new_students = sorted(students, key = lambda  students : (students[1], - students[2]))
print(new_students)