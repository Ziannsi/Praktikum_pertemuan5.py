def faktorial(n):
    if n < 0:
        raise ValueError("Faktorial tidak terdefinisi untuk angka negatif.")
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)
print(faktorial(5))  