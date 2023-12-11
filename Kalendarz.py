s = 6
d = 31
for a in range(-s, d+1):
    if (a + s) % 7 == 0:
        print('\033[0;31m', end='')
    if (a + s) % 7 == 6:
        print('\033[0;31m', end='')
    if a <= 0:
        print(end='\t')
    else:
        print(a, end='\033[0m\t')
    if (a + s) % 7 == 0:
        print()

