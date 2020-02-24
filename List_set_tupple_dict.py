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