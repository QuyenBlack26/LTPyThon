# cho nhap 2 so nguyen a va b tren cung 1 dong cach nhau boi dau phay 
from tracemalloc import start

# In ra cac bang cuu chuong tu a den b khi (a>b) hoac in tu b den a khi (a<b)
print("Nhap 2 so nguyen a va b tren cung 1 dong cach nhau boi dau phay :")
a, b = map(int, input('Nhap gia tri vao : ').split(','))
def BangCuuChuong(start, end):
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        print(f"Bang cuu chuong {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()
BangCuuChuong(a, b)
     
print("Nhap 1 so nguyen duong n :")
n = int(input('Nhap gia tri vao : '))

# Liet ke cac so nguyen to n
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Cac so nguyen to n la :")
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=' ')
        
# Liet ke cac uoc so nguyen to n
print("\nCac uoc so nguyen to n la :")
for i in range(2, n + 1):
    if n % i == 0 and is_prime(i):
        print(i, end=' ')
        
        

