# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/18/18
    Time:   9:10 AM
    Package 
    File    test_2.py
    Description
    
'''
def p():
    print('------------------------------------------------------------')

def test_start(first, *args):
    print('first parameter : ', first)
    i = 1
    for arg in args:
        print('another parameter : ', arg)
        i += 1
    # total = len(*args) + 1
    print('total number of parameter : ', i)

test_start('python_day_1', 'python_day_2', 'python_day_3')

p()

def print_all(*args):
    for arg in args:
        if type(arg) is list:
            for ele in arg:
                print(ele)
        elif type(arg) is dict:
            for key, val in arg.items():
                print('ele : \t\t', 'key = ', key, '\tval = ', val)
        else :
            print('ele : ', arg)

arg_1 = ['1', '2', '3']
arg_2 = '4'
arg_3 = ['5', '6']
arg_4 = {'A' : 1, 'B' : 2, 'C' : 3}

print_all(arg_1, arg_2, arg_3, arg_4)
p()

def print_dict(**kwargs):
    i = 1
    for arg in kwargs:
        if type(arg) is dict:
            print(arg)
        else :
            print('the {}th'.format(i), ' element is not dict type')
        i += 1
    p()

dict_1 = {'A' : 'a', 'B' : 'b'}
dict_2 = {'a' : 1}
lst_1 = [1, 2, 3]
p1 = 'string'


# print_dict('dict_1', dict_2)

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name_1 = 'angel', name_2 = 'xj')
p()
print('import text beginning')

