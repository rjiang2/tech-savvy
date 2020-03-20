# to create a function that returns the absolute value of any number 
def my_abs(number):
"""
returns the absolute value of any number.

number: an int.
"""
# the above is called docstring.
if number < 0:
    return 0 - number
else:
    return number

def main():
    a = -10
    abs_a = my_abs(a)
    print(abs_a) 

    # print(my_abs(-10))

if __name__ == '__main__':
    # this will only be executed when running this file
    # this does not affect other files that import current
    main()