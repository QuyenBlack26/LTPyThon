print ('Danh Sach so nguyen n')
n = int(input("Nhap so nguyen duong n : "))
i = 0
sotong = 0
sotich = 1
while n > 0:
    sodau = n % 10
    n = n // 10
    sotong += sodau
    sotich *= sodau
print ('Tong cac chu so : ', sotong)
print ('Tich cac chu so : ', sotich)