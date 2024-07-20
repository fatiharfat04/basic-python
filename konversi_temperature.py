# latihan konversi satuan temperature

# program konversi celcius ke satuan lain
# print("\n PROGRAM KONVERSI TEMPERATURE \n")

# celcius = float(input("masukkan celcius: "))
# print("suhu adalah:", celcius, "Celcius")


# # reamur
# print("___reamur")
# reamur = (4/5) * celcius
# print("suhu dalam reamur adalah:", reamur, "Reamur")

# # fahrenheit
# print("___fahrenheit")
# fahrenheit = ((9/5) * celcius) + 32
# print("suhu dalam fahrenheit adalah:", fahrenheit, "Fahrenheit")

# # kelvin
# print("___kelvin")
# kelvin = celcius + 273
# print("suhu dalam kelvin adalah:", kelvin, "Kelvin")

# PR-----

# c = float(input("masukkan celcius:"))
# print(c, "ini adalah celcius")

# f = ((9/5) * c) + 32
# print(f, "adalah hasil konversi celcius ke fahrenheit")

# f_to_k = (f + 459.67) * 5/9
# print(f_to_k)




c = float(input("masukkan celcius:"))
print(c, "ini adalah celcius")

k = c + 273.15
f = (k * 9/5) - 459.67
print(f)