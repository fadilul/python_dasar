import random 

bil = random.radint(1,100)# menghasilkan bilangan acak pada rentan 1 sampai dengan 100
tebakan_benar = False
tebakan_mask = 7
jumlah_tebakan = 0 

print("komputer telah memilih sebuah bilangan acak dari 1 sampai dengan 100")

while not tebakan_benar and jumlah_tebakan < tebakan_mask:
    