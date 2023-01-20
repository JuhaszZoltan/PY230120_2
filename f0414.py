szoveg:str = input('írj be egy tetszőleges szöveget: ')

e:str = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
n:str = 'aeiooouuuAEIOOOUUU'

emsz:str = ''
for k in szoveg:
    if k in e: emsz += n[e.index(k)]
    else: emsz += k
print(f'a szöveg ékezet mentesen: {emsz}')

emsz_v2:str = szoveg
for k in e:
    if k in szoveg: emsz_v2 = emsz_v2.replace(k, n[e.index(k)])
print(f'a szöveg ékezet mentesen máshogy: {emsz_v2}')