list_1 = ['history', 'Math', 'Physics', 'CompSci']
tuple_1 = ('history', 'Math', 'Physics', 'CompSci')
sets_1 = {'history', 'Math', 'Physics', 'CompSci'}

print(list_1)
print(tuple_1)
print(sets_1)

idx_list = []
x_list = []
for idx, x in enumerate(list_1, start=1):
    idx_list.append(idx)
    x_list.append(x)
print(idx_list)
print(x_list)
list_1_str = ', '.join(list_1)
print(list_1_str)
print(len(list_1_str))
print(' ------   sets ----')

cs_course = {'Hist', 'Math', 'Physics', 'CompSci'}
art_course = {'Hist', 'Math', 'Art', 'Design'}

print(cs_course.intersection(art_course))
print(cs_course.union(art_course))

empty_list = []
empty_list = list()
empty_tupple = ()
empty_tupple = tuple()
empty_set1 = {} # this isnt right, it creates a dictionary
empty_set = set()

print(type(empty_set1))
print(type(empty_set))

print(' -------  dictionary-----')

student = {'name' : 'John', 'age' : 25, 'courses' : ['Math', 'CompSci']}
print(student['name']) # get is better as if key not in the dic, it will fail, get will return none
print(student.get('name'))
print(student.get('phone', 'Not Found'))

#adding new key

student['phone'] = '555-55545'
print(student.get('phone'))
#updating 1
student['name'] = 'Sinan'
print(student.get('name'))
#updating 2 - useful for multiple
student.update({'name': 'Helene', 'age': 34, 'phone': '545465'})
print(student)

#deleting - delete and pop method - pop allows to capture poped out info

del student['age']
print(student)
phone = student.pop('phone')
print(student)
print(phone)
print('===== len and counting looping ====')
student = {'name' : 'John', 'age' : 25, 'courses' : ['Math', 'CompSci']}
student.update({'name': 'Helene', 'age': 34, 'phone': '545465'})
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, values in student.items():
    print(key, values)




