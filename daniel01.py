LOGIN = 'abc'
PASSWORD = '123'


login_entered = input('enter the login ID ')
password_entered = input('enter the password ')

if password_entered == PASSWORD and login_entered == LOGIN:
    print('it is correct')
elif password_entered != PASSWORD and login_entered == LOGIN:
    print('only login ID correct')
elif password_entered == PASSWORD and login_entered != LOGIN:
    print('only password correct')
else:
    print('none correct')