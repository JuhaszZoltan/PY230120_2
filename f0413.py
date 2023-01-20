mghk:str = 'aáeéiíoóöőuúüű'
szo:str = input('írj be egy tetszőleges szót: ').lower()

msz:int = 0
for k in szo:
    if k in mghk: msz += 1

print(f'magtánhangzók száma a szóban: {msz} db')