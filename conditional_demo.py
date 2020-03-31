# age = int(input('Please enter your age: '))

# if age >= 21:
#     print('Yes, you can!')
# else:
#     print('No, you cannot!')

def countdown(n):
    import time
    time.sleep(1)

    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
