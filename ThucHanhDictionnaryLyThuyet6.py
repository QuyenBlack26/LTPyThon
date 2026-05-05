#cho nhap 2 chuoi (s1 va s2) 
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")
# a) In ra những ký tự trong cả 2 chuỗi. 
common_characters = set(s1) & set(s2)
print("Những ký tự có trong cả 2 chuỗi:", common_characters)
# b) Đếm số ký tự trong s1 không có trong s2 và ngược lại.
def unique_characters(str1, str2):
    return set(str1) - set(str2)
unique_in_s1 = unique_characters(s1, s2)
unique_in_s2 = unique_characters(s2, s1)
print("Số ký tự có trong s1 nhưng không có trong s2:", len(unique_in_s1))
print("Số ký tự có trong s2 nhưng không có trong s1:", len(unique_in_s2))
# c) In ra những ký tự có trong S1 nhưng không có trong S2 và những ký tự có trong S2 nhưng không có trong S1.đưa mỗi chuỗi vào 1 dict (dict1 và dict2). Thực hiện dò tìm S1 trên dict2 và tìm S2 trên dict1
dict1 = {char: True for char in s1}
dict2 = {char: True for char in s2}
unique_in_s1 = [char for char in s1 if char not in dict2]
unique_in_s2 = [char for char in s2 if char not in dict1]
print("Những ký tự có trong s1 nhưng không có trong s2:", unique_in_s1)
print("Những ký tự có trong s2 nhưng không có trong s1:", unique_in_s2)

