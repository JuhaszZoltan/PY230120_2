szoveg:str = input('írj be egy tetszőleges szöveget: ')

print(szoveg.replace(' ', '\n'))

for k in szoveg:
    if k == ' ': print(end='\n')
    else: print(k, end='')