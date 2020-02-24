if True:
    print('True')
if False:
    print('False but would not print it')

# is and == is different. 'is' if it is exactly the same object

language = 'Java'

if language == 'Python':
    print('language is', language)
elif language == 'Java':
    print('language is', language)
else:
    print('no match')

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('not admin')

if not logged_in:
    print('Admin page')
else:
    print('not admin')


a = [1, 2, 3]
b = a
print(a == b)
print(a is b)
print(id(a) is id(b))
print('-----------')
condition = 10 # 0 and None, empty string or list & dictionary happen to be false inherently
if condition:
    print('True')
else:
    print('False')

