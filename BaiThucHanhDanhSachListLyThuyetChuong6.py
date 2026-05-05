# BaiThucHanhDanhSachListLyThuyetChuong6.py
#Viet chuong trinh nhap nhieu lan cac so nguyen duong, sau moi  lan nhap , chuong trinh se hoi nguoi dung co muon tiep tuc nhap hay khong (yes/no). neu chon yes (y) thi cho nguoi dung nhap tiep, neu chon no (n) chuong trinh se thuc hien:
#a. in ra cac so nguyen to co trong list
#b. tinh trung binh cong cac so am, trung binh cac so duong
#c. so long nhat va so nho nhat trong list
#d. cho biet cac so list co duoc sap xep theo thu tu tang dan hay chua
from math import sqrt, pi
DanhSach = []
while True:
    print ('Nhap mot so nguyen duong : ')
    n = int(input())
    if n > 0:
        DanhSach.append(n)
    else:
        print ('Vui long nhap mot so nguyen duong')
        continue
    print ('Ban co muon tiep tuc nhap khong ? (yes/no) : ')
    tieptuc = input().lower()
    if tieptuc == 'no' or tieptuc == 'n':
        break
    else:
        if tieptuc == 'yes' or tieptuc == 'y':
            continue
# a. in ra cac so nguyen to co trong list
def SoNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 
annofuction = lambda n : SoNguyenTo(n)
print ('Cac so nguyen to co trong list la : ')
for num in DanhSach:
    if annofuction(num):
        print('[', num, ']', end=' ')
        print("\n ")     
# b. tinh trung binh cong cac so am, trung binh cac so duong
TongAm = 0
DemAm = 0
TongDuong = 0
DemDuong = 0
def TinhTrungBinh(Tong = 0, Dem = 0):
    if Dem > 0:
        return Tong / Dem
    else:
        return 0
for num in DanhSach:
    if num < 0:
        TongAm += num
        DemAm += 1
    elif num > 0:
        TongDuong += num
        DemDuong += 1
Dem = lambda x : x if x > 0 else 0
print ('Trung binh cong cac so am la : ', TinhTrungBinh(TongAm, DemAm))
print ('Trung binh cong cac so duong la : ', TinhTrungBinh(TongDuong, DemDuong))

# c. so long nhat va so nho nhat trong list
if len(DanhSach) > 0:
    SoLonNhat = max(DanhSach)
    SoNhoNhat = min(DanhSach)
    print ('So lon nhat trong list la : ', SoLonNhat)
    print ('So nho nhat trong list la : ', SoNhoNhat)
else:
    print ('Danh sach rong')
# d. cho biet cac so list co duoc sap xep theo thu tu tang dan hay chua
List = lambda x: x if x > 0 else 0
if all(List(DanhSach[i]) <= List(DanhSach[i + 1]) for i in range(len(DanhSach) - 1)):
    print ('Cac so trong list da duoc sap xep theo thu tu tang dan')
else:    print ('Cac so trong list chua duoc sap xep theo thu tu tang dan')
    
    
    