print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension [:]')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension [:]')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0:-1] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0::2] #START:END longkap 2
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
#untuk menciptakan list baru dari elemen list yang sudah ada

print('\nMembuat list baru')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: buang diujung')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
print(daftar_buku[0::2])