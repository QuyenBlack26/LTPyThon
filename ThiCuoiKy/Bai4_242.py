#Xay dung ham an danh voi ket qua cua ham la kieu boolean su dung lambda.In ra so trong khoan tu 1 den 1000
print("Cac so dong nhat tu 1 den 10000 la :")
# So đong nhat: cac chu so đeu giong nhau
so_dong_nhat_all = lambda n: all(ch == str(n)[0] for ch in str(n))
so_dong_nhat_any = lambda n: not any(ch != str(n)[0] for ch in str(n))
print("\n So dong nhat:")
print([i for i in range(1, 10001) if so_dong_nhat_all(i)])
print("\nSo dong nhat (cach 2):")
print([i for i in range(1, 10001) if so_dong_nhat_any(i)])

#So hoan thien
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n
print("\nSo hoan thien:")
print([i for i in range(1, 10001) if so_hoan_thien(i)])

        