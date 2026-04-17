print ('Danh Sach so nguyen n')
n = int(input("Nhap so nguyen duong n : "))
i = 0
solonnhat = 0
while n > 0:
    sodau = n % 10
    n = n // 10
    if sodau > solonnhat:
        solonnhat = sodau
print ('So lon nhat : ', solonnhat)