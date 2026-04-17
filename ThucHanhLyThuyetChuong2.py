print ("Nhap chieu dai cua hinh hop chu nhat : ")
n = float(input('Nhap gia tri vao : '))

print ("Nhap chieu rong cua hinh hop chu nhat : ")
m = float(input('Nhap gia tri vao : '))

print ("Nhap chieu cao cua hinh hop chu nhat : ")
h = float(input('Nhap gia tri vao : '))

sole = (input('So le cua hinh hop chu nhat : '))
dinhdang = '{:.'+sole+'f}'

print ('Dien tich day la : ',float(dinhdang.format(m*n)) ,"cm\u00b2")
print ('Dien tich hinh khoi = ', float(dinhdang.format(m*n*h)), "cm\u00b2")