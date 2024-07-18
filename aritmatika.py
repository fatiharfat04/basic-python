# operasi aritmatika

"""prioritas operasi, presedence operational:
    1. (), kurung akan selalu mengambil langkah pertama
    2. eksponen = **
    3. kali & bagi = * / % ** //
    4. tambah & kurang = + -   
"""

a = 10
b = 3

tambah = a + b
kurang = a - b
kali = a * b
bagi = a / b

eksponen_atau_pangkat = a ** b  # a pangkat b
modulus = a % b  # modulus adalah sisa bagi dari 2 bilangan
floor_division = a // b  # hasil dari pembagian, dibulatkan ke bawah

print(tambah)
print(kurang)
print(kali)
print(bagi)
print(eksponen_atau_pangkat)
print(modulus)