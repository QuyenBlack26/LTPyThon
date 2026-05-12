tien = [1 , 2, 5, 10, 20, 50, 100,200, 500]

n = int(input("Nhap so tien can doi ra gia tri so to tien : "))
def DoiTien(n):
    so_to = [0] * len(tien)
    for i in range(len(tien)-1, -1, -1):
        while n >= tien[i]:
            n -= tien[i]
            so_to[i] += 1
    return so_to

so_to = DoiTien(n)
print ('So to 500 : ', so_to[8])
print ('So to 200 : ', so_to[7])
print ('So to 100 : ', so_to[6])
print ('So to 50 : ', so_to[5])
print ('So to 20 : ', so_to[4])
print ('So to 10 : ', so_to[3])
print ('So to 5 : ', so_to[2])
print ('So to 2 : ', so_to[1])
print ('So to 1 : ', so_to[0])
print ('Tong so to : ', sum(so_to))