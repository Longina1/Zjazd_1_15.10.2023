
while True:
    cena = float(input('Podaj cenę (1-1000):  '))
    if 1 <= cena <= 1000:
        break
    else:
        print('Zła cena, jeszcze raz podaj cenę.')

print('Cena zaakceptowana')
