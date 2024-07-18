# input

data = input("masukkan data: ")
print(data, type(data))

""" nilai dari input pasti berupa tipe data str, 
    maka jika ingin mengubahnya menjadi tipe data yang lain,
    kita bisa menggunakan "casting tipe data" 
"""
angka = int(input("masukkan angka: "))
print(angka, type(angka))

""" bagaimana dengan boolean?, simpelnya kita harus 
    mengubah input ke int kemudian baru casting ke boolean """

boolean = bool(int(input("masukkan nilai boolean: ")))
print(boolean, type(boolean))