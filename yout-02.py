greeting = 'Hello'
name = 'Sinan'

message_1 = greeting + ', ' + name + '. Welcome!'

message_2 = '{}, {}. Welcome!'.format(greeting, name)

# f strings option
message_3 = f'{greeting}, {name.upper()}. Welcome!'

print(message_1)
print(message_2)
print(message_3)

# help stuff
print(dir(name)) # overall options
print(help(str)) # more details
print(help(str.lower)) # further details
