from math import *
#a Viết chương trình tính giá trị tuyệt đối của một số nguyên n nhập từ bàn phím sử dụng lambda function.
print ('Nhap gia tri n : ')
n = int(input())
Giatrituyetdoi = lambda n : abs(n)
print ('Gia tri tuyet doi cua n la : ', Giatrituyetdoi(n))
# b ham nhan 1 doi so n va tra ve gia tri n + 15
print ('Nhap gia tri n de cong voi 15: ')
n = int(input())
Hamcong15 = lambda n : n + 15
print ('Gia tri cua n + 15 la : ', Hamcong15(n))
# c ham nhan 2 doi so nguyen (x,y), tra ve tich cua x va y
print ('Nhap hai doi so x va y : ')
print ('Nhap gia tri x : ')
x = int(input())
print ('Nhap gia tri y : ')
y = int(input())
Tich = lambda x, y : x * y
print ('Tich cua x va y la : ', Tich(x, y))
# d ham nhan 1 doi so nguyenn . cho biet n co la boi so cua 13 hoac 19 hay khong
print ('Nhap gia tri n co la boi so cua 13 hoac 19 : ')  
n = int(input())
BoiSo = lambda n : (n % 13 == 0) or (n % 19 == 0)
if BoiSo(n):
    print (n, "la boi so cua 13 hoac 19 ")
else:
    print (n, "khong phai la boi so cua 13 hoac 19")
# e ham nhan 1 doi so nguyen r la ban kinh cua hinh tron, tra ve dien tich cua hinh tron do
print ('Nhap ban kinh r : ')
r = int(input())
Dientich = lambda r : pi * r**2
print ('Dien tich cua hinh tron la : ', Dientich(r))
# f ham nhan 2 doi so thuc d, r la chieu dai va chieu rong cua hinh chu nhat, tra ve hinh chu nhat do
print ('Nhap chieu dai d va chieu rong r cua hinh chu nhat ')
print ('Nhap chieu dai d : ')
d = float(input())
print ('Nhap chieu rong r : ')
r = float(input())
DientichHCN = lambda d, r : d * r
print ('Dien tich cua hinh chu nhat la : ', DientichHCN(d, r))
# g ham nhan 1 doi so nguyen n, cho biet n co la so chinh phuong hay khong
print ('Nhap gia tri so nguyen n de kiem tra co phai la so chinh phuong khong : ')
n = int(input())
SoChinhPhuong = lambda n : int(sqrt(n))**2 == n 
if SoChinhPhuong(n):
    print (n, "la so chinh phuong") 
else:
    print (n, "khong phai la so chinh phuong")
# h ham nhan 1 doi so nguyen n, cho biet n co la so nguyen to hay khong
print ('Nhap gia tri n de kiem tra co phai la so nguyen to khong : ')
n = int(input())
def SoNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 
annofuction = lambda n : SoNguyenTo(n)
if annofuction(n):
    print (n, "la so nguyen to")
else:
    print (n, "khong phai la so nguyen to") 
# i ham nhan 3 ham so nguyen a, b, c, cho biet a, b, c, co la 3 canh hop le cua tam giac hay khong? neu la 3 canh hop le cua tam giac, cho biet tam giac do la tam giac gi?
print ('Nhap ba canh a, b, c de kiem tra co phai la 3 canh hop le cua tam giac khong ')
print ('Nhap canh a : ')
a = float(input())
print ('Nhap canh b : ')
b = float(input())
print ('Nhap canh c : ')
c = float(input())
def KiemTraTamGiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giac deu"
        elif a == b or a == c or b == c:
            return "Tam giac can"
        else:
            return "Tam giac thuong"
    else:
        return "Khong phai la tam giac hop le"
annofuction = lambda a, b, c : KiemTraTamGiac(a, b, c)
print (annofuction(a, b, c))

    
