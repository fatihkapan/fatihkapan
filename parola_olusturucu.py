import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_uzunlugu = int(input("Parolanızın uzunluğunu giriniz"))
parola = ""
for i in range(parola_uzunlugu):
    karakter = random.choice(karakterler)
    parola += karakter
print(parola)
