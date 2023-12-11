my_list = ['kot', 'pies', 'stół', 'krzesło', 'biurko', 'okno']

print('Pętla1')

print('\nPętla2')

print('\nPętla3')
print(len(my_list))
for i in range(len(my_list)):
    print(my_list[i]+my_list[i-1])
    if len(my_list[i]) > 4:
        print('długie słowo\n.................')

print('\nPętla4')
for i in my_list:
    print(i)
    if len(i) > 4:
        print('długie słowo\n.................')

print('\nPętla5 - czy dane słowo jest w liście')
word = 'pies'
for i in my_list:
    if i == word:
        print('Znaleziono słowo', i)

print('\nPętla6 - czy dane słowo jest w liście')
word = 'pies'
if word in my_list:
    print('Znaleziono słowo', word)



