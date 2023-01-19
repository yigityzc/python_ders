liste = []
for i in range(0,5):
    liste.append(eval(input()))

def sıralam_fonksiyon(n):
    return abs(n*n-20)

liste.sort(key=sıralam_fonksiyon)
print(liste)
