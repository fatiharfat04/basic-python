""" casting tipe data atau merubah tipe data 
    ke tipe data yang lain """
# tipe data : int, str, float, bool



# INTEGER
print("____INTEGER")
data_int = 9

data_str = str(data_int)
data_float = float(data_int)
data_bool = bool(data_int) # akan menjadi false ketika nilai integer sama dengan 0
print(f"data: {data_int} dengan tipe: {type(data_int)}")
print(f"data: {data_str} dengan tipe: {type(data_str)}")
print(f"data: {data_float} dengan tipe: {type(data_float)}")
print(f"data: {data_bool} dengan tipe: {type(data_bool)}")


# FLOAT
print("____FLOAT")
data_float = 9.9

data_str = str(data_float)
data_int = int(data_float) # akan dibulatkan ke bawah
data_bool = bool(data_float)
print(f"data: {data_int} dengan tipe: {type(data_int)}")
print(f"data: {data_str} dengan tipe: {type(data_str)}")
print(f"data: {data_float} dengan tipe: {type(data_float)}")
print(f"data: {data_bool} dengan tipe: {type(data_bool)}")


# STRING
print("____STRING")
data_str = "9"

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str) # akan menjadi false ketika nilai string kosong ("")
print(f"data: {data_str} dengan tipe: {type(data_str)}")
print(f"data: {data_int} dengan tipe: {type(data_int)}")
print(f"data: {data_float} dengan tipe: {type(data_float)}")
print(f"data: {data_bool} dengan tipe: {type(data_bool)}")


# BOOLEAN
print("____BOOLEAN")
data_bool = True

data_str = str(data_bool)
data_int = int(data_bool)
data_float = float(data_bool)
print(f"data: {data_bool} dengan tipe: {type(data_bool)}")
print(f"data: {data_str} dengan tipe: {type(data_str)}")
print(f"data: {data_int} dengan tipe: {type(data_int)}")
print(f"data: {data_float} dengan tipe: {type(data_float)}")
