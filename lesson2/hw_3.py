# Enter number 1
val_1 = input('Enter number 1 : ')
while True:
    try:
        val_1 = int(val_1)
    except ValueError:
        print(f'Value {val_1} is not number')
        val_1 = input('Enter number 1 again: ')
    else:
        break
print(val_1)

# Enter operand
operation = input('Enter type of operation: ')
while True:
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        break
    print('Is not correct operation ')
    operation = input('Enter type of operation: ')
print (val_1, operation)

# Enter number 2
val_2 = input('Enter number 2 : ')
while True:
    try:
        val_2 = int(val_2)
    except ValueError:
        print(f'Value {val_2} is not number')
        val_2 = input('Enter number 2 again: ')
    else:
        break
print(val_1, operation, val_2)

# Submit the calculation
user_done = input('Plese enter = for calculate: ')
while user_done != '=':
    print('Incorrect')
    user_done = input('Plese enter = for calculate: ')

# Calculation
if operation == '+':
    result = val_1 + val_2
elif operation == '-':
    result = val_1 - val_2
elif operation == '*':
    result = val_1 * val_2
else:
    result = val_1 / val_2

print(val_1, operation, val_2, user_done, result)
