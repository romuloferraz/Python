num = int(input('Digite o número a ser transformado:\n'))
base = int(input('Escolha a Base de numeração:\n'
                 '[1] Base Binária\n'
                 '[2] Base Octal\n'
                 '[3] Base Hexadecimal\n'))
if base == 1:
    val = bin(num).replace('0b','')
    print(val)
elif base == 2:
    val = oct(num).replace('0o','')
    print(val)
elif base == 3:
    val = hex(num).replace('0x','')
    print(val)
