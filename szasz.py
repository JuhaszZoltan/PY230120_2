# Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
# hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

szam:int = int(input('írj be egy egész számot: '))

# if szam % 3 == 0 or szam % 5 == 0: print('igen')
# else: print('nem')

if not (szam % 3 and szam % 5): print('Y')
else: print('N')

# Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
# képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!

szam:int = int(input('írj be egy pozitív egész számot: '))

# for n in range(1, szam):
#     if n % 3 == 0: print(n)

for n in range(0, szam, 3)[1:]:
    print(n, end=' ')

