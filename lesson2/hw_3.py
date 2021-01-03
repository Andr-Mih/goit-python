result = 0
while True:
    if result != 0:
        val_1 = result
    if result == 0:
        val_1 = input('Enter operand : ')
        while True:
            try:
             val_1 = float(val_1)
            except ValueError:

             print(f'Value {val_1} is not number')
             val_1 = input('Enter number 1 again: ')

            else:
                break

    operation = input('Enter type of operation: ')
    while True:
        if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '=':
            break
        else:

            print('Incorrect operator')
            operation = input('Enter type of operation again: ')

    if operation != '=':
        val_2 = input('Enter operand: ')
        while True:
            try:
                val_2 = float(val_2)
            except ValueError:

                print(f'Value {val_2} is not number')
                val_2 = input('Enter number 2 again: ') 

            # Zero Division check
            if operation == '/' and val_2 == 0:

                print('Zero division')
                val_2 = input('Enter number 2 again: ')

            else:
                break
            
     # Calculation
    if operation == '+':
        result = val_1 + val_2
    elif operation == '-':
        result = val_1 - val_2
    elif operation == '*':
        result = val_1 * val_2
    elif operation == '/':
        result = val_1 / val_2
    if operation == '=':
        break
    

print(result)
