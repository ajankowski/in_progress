liczba_ksiezniczek = random.randint(0, 100)
# liczba_ksiezniczek = 54

while True:
    zgadywanie = input('rycerzu, o jakiej liczbie księżniczek myślę?\n')

    if zgadywanie.isdigit():
        zgadywanie = int(zgadywanie)
        if zgadywanie == liczba_ksiezniczek:
            print('zgadłeś rycerzu', 'huraaaaaaa!!!!!!')
            break
        elif zgadywanie > liczba_ksiezniczek:
            print('zgadujesz za dużo')
        elif zgadywanie < liczba_ksiezniczek:
            print('zgadujesz za mało')
    else:
        print('to nie jest liczba')
