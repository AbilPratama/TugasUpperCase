def hitungHurufBesar(teks):

    jumlah = 0
    for char in teks:
        if char.isupper():
            jumlah += 1
    return jumlah
