
# to be used with importing_module.py
print('Imported find_idx module...')
test = 'Test string'

def find_index(to_search, target):
    '''find the index of a value in a squence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return 'Not in the squence'