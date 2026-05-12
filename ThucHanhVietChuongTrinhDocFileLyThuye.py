#viet chuong  trinh doc file van ban tren may tinh (text.txt)
# 1. Xuat ra file van ban moi giam dung luong luu tru so voi file van ban goc
# 2. Doc file sau khi giam dung luong va tra ve dinh dang van ban ban dau 
# BaiThucHanhVietChuongTrinhDocFileLyThuye.py
# goi y : huong 1 : chia nho cac ky tu thanh cac mang doc lap va luu tru vi tri xuat hien cua cac ky tu do
# huong 2 : su dung tap hop de luu tru cac ky tu da xuat hien va xoa cac ky tu trung lap
# huong 3 : su dung tu dien de luu tru cac ky tu va so
# lan xuat hien cua cac ky tu do
from collections import Counter
# huong 1 : chia nho cac ky tu thanh cac mang doc lap va luu tru vi tri xuat hien cua cac ky tu do
with open('text.txt', 'r') as file: 
    content = file.read() 
    char_positions = {}
    for index, char in enumerate(content):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(index)
    print("Vị trí xuất hiện của các ký tự:")
    for char, positions in char_positions.items():
        print(f"Ký tự '{char}': {positions}")   
# huong 2 : su dung tap hop de luu tru cac ky tu da xuat hien va xoa cac ky tu trung lap
