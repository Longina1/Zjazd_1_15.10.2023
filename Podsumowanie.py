for a in range(0,11):
    for b in range(0,11):
        if a == 0 and b == 0:
            print('*', sep='', end='\t')
        elif a == 0:
            print(b, end='\t')
        elif b == 0:
            print(a, end='\t')
        elif a == b:
            print('\033[43m', a*b, '\033[0m', sep='', end='\t')
        else:
            print(a*b, end='\t')
    print()

