print('Wprowadź imię')
first_name = input()

age = int(input('Wprowadź wiek:  '))

gender = bool(int(input('Czy jesteś konietą? Jesli tak, wpisz "1", jeśli nie, wpisz"0"')))

if age <= 18:
    print('Cześć', first_name, ' ')
else:
    if gender:
        print(f'Szanowna Pani {first_name}, ma Pania {age} lat.')
    else:
        Print(f'Szanowny Panie {first_name}, ma Pan {age} lat.')
if first_name[-1] == 'a':
    print('Twoje imię kończy się na "a', 'Witamy Panią')
    print('Twoje imię nie kończy się na "a", 'Witamy Pana'')


