exit_e = 0
number1 = input("Enter a number (or a letter to exit): ")
try:
    int(number1)
except ValueError:
    try:
        float(number1)
    except ValueError:
        exit_e = 1
while exit_e != 1:
    operator = input("Enter an operation: ")
    number2 = int(input("Enter another number: "))
    if operator == '+':
        print("Result: ",int(number1) + number2 , '\n\n')
        number1 = input("Enter a number (or a letter to exit): ")
        try:
            int(number1)
        except ValueError:
            try:
                float(number1)
            except ValueError:
                exit_e = 1   
    elif operator == '-':
        print("Result: ",int(number1) - number2 , '\n\n')
        number1 = input("Enter a number (or a letter to exit): ")
        try:
            int(number1)
        except ValueError:
            try:
                float(number1)
            except ValueError:
                exit_e = 1
    elif operator == '*':
        print("Result: ",int(number1) * number2 , '\n\n')
        number1 = input("Enter a number (or a letter to exit): ")
        try:
            int(number1)
        except ValueError:
            try:
                float(number1)
            except ValueError:
                exit_e = 1
    else:
        print("Result: ",int(number1) // number2 , '\n\n')
        number1 = input("Enter a number (or a letter to exit): ")
        try:
            int(number1)
        except ValueError:
            try:
                float(number1)
            except ValueError:
                exit_e = 1
