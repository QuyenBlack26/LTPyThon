print ('Danh Sach so nguyen n')
n = int(input("Nhap so nguyen duong n : "))
i = 0
solocphat = True;
while n > 0:
    sodau = n % 10
    n = n // 10
    if (sodau != 6 and sodau != 8):
        solocphat = False
        break;  
if solocphat == True:
    print ('So loc phat  ')
else :
    print ('Khong phai so loc phat  ')

