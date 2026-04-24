#Cho nhap so nguyen n .Tinh tong cac chu so trong n
print('Danh Sach so nguyen n')
n = int(input("Nhap so nguyen duong n : "))
def Songuyen(n):
    if n < 10:
        return n
    return Songuyen(n//10) + n%10
print (Songuyen(n))

print('Danh Sach so giai thua n')
n = int(input("Nhap giai thua n : "))
def GiaiThua(n):
    if (n == 1):
        return n
    return GiaiThua(n-1)*n
print(GiaiThua(n))

print('Danh Sach so nguyen n')
a = int(input("Nhap so nguyen duong a : "))
b = int(input("Nhap so nguyen duong b : "))
def Tinh(a,b):
    if (b == 0):
        return  1
    return Tinh(a,b-1)*(a)
print("Tinh a mu b : "+ Tinh(a,b))

# uoc chung lon nhat cua 2 so nguyen a va b
print('Danh Sach uoc so chung lon nhat cua 2 so nguyen n')
x = int(input("Nhap so nguyen duong a : "))
y = int(input("Nhap so nguyen duong b : "))
def uocso(x,y):
    if (y == 0):
        return 1
    return uocso(y,x % y)
print(uocso(x,y))

# ham nhan mot so nguyen duong n . tinh so hang thu n cua chuoi fibonaci
print('Ham nhan mot so nguyen duong n . tinh so hang thu n cua chuoi fibonaci')
n = int(input("Nhap so nguyen duong n : "))
def fibonacci(n):
    if (n <= 1):
        return n
    return  fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(n))