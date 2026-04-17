print ('Danh Sach so nguyen n')
n = int(input("Nhap so nguyen duong n : "))
i = 0
sochan = 0
sole = 0
while n > 0:
    sodau = n % 10
    n = n // 10
    print ('gia tri cach so moi so : ',sodau)
    if (sodau%2==0):
        sochan += 1
    else:
        sole += 1
    print ('So chan co duoc : ', sochan)
    print ('So le co duoc : ', sole)
