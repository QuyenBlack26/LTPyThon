s = '''Chiều chiều trước bến Văn Lâu Ai ngồi, ai câu, ai sầu, ai thảm Ai thương, ai cảm, ai nhớ, ai trông Thuyền ai thấp thoáng ven sông Đưa câu mái vẩy chạnh lòng nước non '''

print ('Chuong Trinh chuoi trong Word')
n = input("Nhap chuoi can dem : ")
print("So lan xuat hien cua chuoi '", n, "' trong chuoi s la:", s.count(n, 0, len(s)))

print ('Nhap mot chuoi ')
string = input("Nhap chuoi : ")
x = input("Nhap chuoi can dem : ")
print("So lan xuat hien cua chuoi '", x, "' trong chuoi string la:", string.count(x, 0, len(string)))