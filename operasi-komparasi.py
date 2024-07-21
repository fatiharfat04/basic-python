# operasi komparasi atau perbandingan
# <, >, <=, >=, ==, !=, is, is not
# setiap hasil dari komparasi adalah boolean

# Contoh nilai untuk komparasi
a = 10
b = 20

# 1. Sama dengan (==)
print(f"{a} == {b}: {a == b}")

# 2. Tidak sama dengan (!=)
print(f"{a} != {b}: {a != b}")

# 3. Lebih besar dari (>)
print(f"{a} > {b}: {a > b}")

# 4. Lebih kecil dari (<)
print(f"{a} < {b}: {a < b}")

# 5. Lebih besar atau sama dengan (>=)
print(f"{a} >= {b}: {a >= b}")

# 6. Lebih kecil atau sama dengan (<=)
print(f"{a} <= {b}: {a <= b}")



# Contoh nilai untuk komparasi
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# 7. Identitas (is)
print(f"x is y: {x is y}")   # False, karena x dan y adalah dua objek yang berbeda di memori
print(f"x is z: {x is z}")   # True, karena x dan z merujuk ke objek yang sama di memori

# 8. Bukan identitas (is not)
print(f"x is not y: {x is not y}")  # True, karena x dan y adalah dua objek yang berbeda di memori
print(f"x is not z: {x is not z}")  # False, karena x dan z merujuk ke objek yang sama di memori
