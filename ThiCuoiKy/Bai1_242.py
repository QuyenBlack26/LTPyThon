print("Nhap chieu dai day hinh khoi chu nhat: ")
dai = float(input('Nhap gia tri vao : '))

print("Nhap chieu rong day hinh khoi chu nhat :")
rong = float(input('Nhap gia tri vao : '))

print("Nhap Chieu cao hinh khoi chu nhat :")
cao = float(input('Nhap gia tri vao : '))

# So le la so luong so le sau dau phay cua ket qua,ta se su dung dinhdang de dinh dang so le ma no in ra
sole = int(input('So luong so le can hien thi :'))
dinhdang = '{:.'+str(sole)+'f}'

print('Dien tich day hinh chu nhat = ',float(dinhdang.format(dai*rong)) ,"cm\u00b2")

print('The tich hinh khoi =',float(dinhdang.format(dai*rong*cao)),"cm\u00b3")
