# operasi logika dan boolean
# not, or, and, xor

# Contoh nilai untuk komparasi
a = True
b = False

# 1. Operator logika AND
print(f"{a} and {b}: {a and b}")  # False, karena b adalah False

# 2. Operator logika OR
print(f"{a} or {b}: {a or b}")  # True, karena a adalah True

# 3. Operator logika NOT
print(f"not {a}: {not a}")  # False, karena a adalah True
print(f"not {b}: {not b}")  # True, karena b adalah False



# Contoh nilai untuk komparasi
a = True
b = False

# 4. Operator logika XOR menggunakan bitwise XOR (^)
print(f"{a} ^ {b}: {a ^ b}")  # True, karena hanya salah satu yang True
print(f"{a} ^ {a}: {a ^ a}")  # False, karena keduanya True
print(f"{b} ^ {b}: {b ^ b}")  # False, karena keduanya False
