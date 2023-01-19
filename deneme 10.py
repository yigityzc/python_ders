def polindrom(*dram):
    toplam = fark = 0
    for sayi in dram:
        if str(sayi)==reversed(str(sayi)):
            print(sayi)
            toplam+=sayi
        else:
            toplam-=sayi
    return toplam
print(polindrom([10,101,55,40,9009]))



