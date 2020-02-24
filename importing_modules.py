import my_function_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'x')
print(index)


print('=== or can only import the function------')
from my_function_module import find_index, test
import  sys # to check what directories that python looking for module to import

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'x')
print(index)
print(test)

print(sys.path) # all the locations where the module should be

print('======other stuffff=---------')

import os

print(os.getcwd())
print(os.__file__) # shows entire std library

print('========joke=================')

import antigravity
antigravity