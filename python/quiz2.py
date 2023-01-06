ki = True
while ki:
    x = int(input('Choose a number:\n'))#\n은 띄어쓰기
    y = int(input('Choose another number:\n'))
    z = input('choose an operation(+,-,*,/)or Write exit to finish:\n')
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
