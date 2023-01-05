ki = True
while ki:
    x = int(input('Choose a number:'))
    y = int(input('Choose another number:'))
    z = input('choose an operation(+,-,*,/)or Write exit to finish:')
    if z == '+':
        k = x+y
        print(f'Result:{k}')
    elif z == '-':
        k = x-y
        print(f'Result:{k}')
    elif z == '*':
        k = x*y
        print(f'Result:{k}')
    elif z == '/':
        k = x/y
        print(f'Result:{k}')
    elif z == 'exit':
        ki = False
