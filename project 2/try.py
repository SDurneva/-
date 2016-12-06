f = open('inputs.txt', 'r',encoding='utf-8')
entries1 = f.read()
entries = entries1.split('\n')
c = ''
for n in entries:
    if c in entries:
        entries.remove(c)
print(entries)