result = 0

for i in range(10):
    print(f'In iteration {i}, current result is {result}.')

    result += i+1

    print(f'After adding {i+1}, the result becomes {result}.')
    print()

print(f'Final result is {result}.')