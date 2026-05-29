# ham nhan mot 1 doi so nguyen n , boi so n co phai boi so 13 hoac 19 hay khong su dung lamda
print("Nhap mot so nguyen n :")
n = int(input('Nhap gia tri vao : '))
is_multiple_of_13_or_19 = lambda x: x % 13 == 0 or x % 19 == 0
if is_multiple_of_13_or_19(n):
    print(f"{n} la boi so cua 13 hoac 19.")
else:
    print(f"{n} khong la boi so cua 13 hoac 19.")
    
# Ham nhan 3 ham so nguyen a, b, c . cho biet 3 canh hop le cua 1 tam giac hay khong, cho biet no la tam giac gi su dung lambda
print("Nhap 3 canh a, b, c :")
a = float(input('Nhap gia tri a vao : '))
b = float(input('Nhap gia tri b vao : '))
c = float(input('Nhap gia tri c vao : '))
is_valid_triangle = lambda x, y, z: x + y > z and x + z > y and y + z > x
if is_valid_triangle(a, b, c):  
    if a == b == c:
        print("Day la tam giac deu.")
    elif a == b or b == c or a == c:
        print("Day la tam giac can.")
    else:
        print("Day la tam giac thuong.")
else:
    print("Day khong phai la 3 canh hop le cua 1 tam giac.")
    

