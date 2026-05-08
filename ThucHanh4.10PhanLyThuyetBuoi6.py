#iii Viet chuong trinh cho nhap so dien thoai (s ) dunng tap hop. in ra cac so tu 0 den 9 khong xuat hien trong so dien thoai vua nhap
# BaiThucHanh4.10PhanLyThuyetBuoi6.py
s = input("Nhập số điện thoại: ")
DanhDaySo = set('0123456789')
DanhDaySoTrongSoDienThoai = set(s)
SoKhongXuatHien = DanhDaySo - DanhDaySoTrongSoDienThoai
print("Các số từ 0 đến 9 không xuất hiện trong số điện thoại vừa nhập là:", SoKhongXuatHien)

