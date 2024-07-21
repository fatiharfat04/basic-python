# membuat gabungan area dari rentang angka 


# # ++++++++3--------10+++++++++

# # meminta user untuk memasukkan angka 
# inputUser = int(input("masukkan angka kurang dari 3\natau\nlebih besar dari 10\n:"))

# # masukkan "kondisi yang diinginkan" ke dalam variabel
# isKurangDari = inputUser < 3
# isLebihDari = inputUser > 10

# # memeriksa angka yang dimasukkan oleh user dan print hasilnya
# isBenar = isKurangDari or isLebihDari
# print("angka yang anda masukkan:", isBenar)


# # ----3++++10----
# inputUser = int(input("masukkan angka lebih dari 3\ndan\nkurang dari 10\n:"))

# kasus2 = 3 < inputUser < 10

# isCorrect = kasus2
# print("angka yang anda masukkan:", isCorrect)





# PR
# kasus 1 = ---0+++5---8+++11---
# kasus 2 = +++0---5+++8---11+++



# kasus 1 = ---0+++5---8+++11---
inputUser1 = int(input("masukkan angka kasus 1: "))
kasus1 = 0 < inputUser1 < 5 or 8 < inputUser1 < 11

# kasus 2 = +++0---5+++8---11+++
inputUser2 = int(input("masukkan angka kasus 2: "))
cond1 = inputUser2 < 0 or inputUser2 > 11
cond2 = 5 < inputUser2 < 8
kasus2 = cond1 or cond2

# print hasil dari keduanya
print("angka kasus 1: ", kasus1, "\nangka kasus 2: ", kasus2)

