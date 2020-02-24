def cc_func():
    pass  # pass the function for now not to get an error


print(cc_func())


def hello_func():
    print('Hello Function')


hello_func()


def return_func():
    return 'Hello Function'


return_func()
print(return_func().upper())

print('pass arguments to the function-----')


def halo_function(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(halo_function('Hi', 'Sinan'))
print(halo_function('Hi', name='Sinan'))

print('=============args and kwargs========')


def student_info(*args, **kwargs):  # * and ** check line 45
    print(args)  # creates tupple
    print(kwargs)  # creates a dicyinoart


courses = ['Math', 'Art']
info = {'name': 'Sinan', 'age': 34}
student_info()
student_info('Math', 'Art', name='Sinan', age=34)
student_info(courses, info)
student_info(*courses, **info)
print('=============example========')

# number of days in the month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    """Returns true for leap years and false if not"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def days_in_month(year, month):
    '''returns number of days in the month in entered year'''
    if not 1 <= month <= 12:
        return 'Invalid year'
    elif month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month]
print(days_in_month(2020, 2))