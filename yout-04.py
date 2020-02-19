# list tuple and sets
# tuple sequential data
# sets unordered without duplicates
# len = counts
# -1 indexing last item

courses = ['history', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))
print(courses[0 : -1]) # doesnt include last # 0 == empty before/after the column the same starts begining or finished at the end
print(courses)
courses.append('Art')
print(courses)
courses.insert(1, 'Sos')
print(courses)

courses_2 = ['Scie', 'Mus']
courses.insert(1, courses_2) # inserts as list in a list
courses.append(courses_2) # appends as list in a list
courses.extend(courses_2) # extend is the option put individually
print(courses)

courses.remove('Scie')
print(courses)

popped = courses.pop()
print(courses)
print(popped)

print('=======================sorting=========================')

courses = ['history', 'Math', 'Physics', 'CompSci']
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]

nums.sort(reverse=True)
print(sum(nums))
print('=======================indexing=========================')
courses = ['history', 'Math', 'Physics', 'CompSci']
print(courses.index('Math'))
print('Math' in courses)

for something in courses:
    print(something)

new_list = []
for something in enumerate(courses, start=1):
    new_list.append(something)
print(new_list)
print('=======================string to list convert=========================')

courses = ['history', 'Math', 'Physics', 'CompSci']

course_str = ' - '.join(courses)
print(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)
print('=======================tuples=========================')
# tuples imutable , list mutable
list_1 = ['history', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'ART'
print(list_1)
print(list_2) # notice that list 2 also changed. because they were the same  is mutable object

tuple_1 = ('history', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
#tuple_1[0] = 'ART' #throws error
print(tuple_1)
print(list_2) # notice that list 2 also changed. because they were the same  is mutable object

print('=======================sets=========================')
# no order , no duplicates, optimised for share or dont share with another data or check if it ios in

set_courses = {'history', 'Math', 'Physics', 'CompSci', 'Math'}
print(set_courses) # removed the duplicate math
print(len(set_courses))
print('Math' in set_courses)

set_courses_2 = {'history', 'Math', 'Physics', 'CompSci', 'Math'}
# https://www.youtube.com/watch?v=W8KRzm-HUcc