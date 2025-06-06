# %%
'''
    link: https://www.codewars.com/kata/5302d846be2a9189af0001e4/train/python
    Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.
    
    Example:
    ['John', 'Smith'], 'Phoenix', 'Arizona'
    This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!
'''

# %%
def say_hello(name, city, state):
    full_name = ' '.join(name)
    return f'Hello, {full_name}! Welcome to {city}, {state}!'

result = say_hello(name=['John', 'Smith'], city='Phoenix', state='Arizona')
print(result)
