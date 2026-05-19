# Mang tu 0 den 1000000 so strobogrammatic
def TachSo(n):
    while n > 0:
        TachS =  n % 10
        n //= 10
        yield TachS

    
def GopSo(digits):
    n = 0
    for digit in digits:
        if digit == 6 or digit == 9:
            digit = 6 if digit == 9 else 9  
        n = n * 10 + digit
    return n

def XetSoStrobogrammatic(n):
    digits = set()
    map = {0, 1, 6, 8, 9}
    for digit in TachSo(n):
        if digit not in map:
            return False

    if n != GopSo(digit for digit in TachSo(n)):
        return False
    else:
        return True

# Ham xet so nguyen to
def XetSoNguyenTo(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def xettu1denn():
    for i in range(1000000):
        if XetSoStrobogrammatic(i):
            print(i, end=' ')
    print()  # In xuống dòng sau mỗi số strobogrammatic


def insoStrobogrammaticNguyenTo(n):
    for i in range(2, n + 1):
        if  XetSoNguyenTo(i) and XetSoStrobogrammatic(i):
            print(i, end=' ')    
    print()  # In xuống dòng sau mỗi số strobogrammatic nguyên tố
# chạy
xettu1denn()
insoStrobogrammaticNguyenTo(1000000)

### C ####
def XetSoStrobogrammaticC(n): 
    digits = set()
    map = {0, 1, 2, 5, 6, 8, 9}
    for digit in TachSo(n):
        if digit not in map:
            return False

    if n != GopSo(digit for digit in TachSo(n)):
        return False
    else:
        return True
            
def xuat2():
    for i in range(1000000):
        if XetSoStrobogrammaticC(i):
            print(i, end=' ')
    print()  # In xuống dòng sau mỗi số strobogrammatic

def insoStrobogrammaticNguyenTo1(n):
    for i in range(2, n + 1):
        if  XetSoNguyenTo(i) and XetSoStrobogrammaticC(i):
            print(i, end=' ')    
    print()  # In xuống dòng sau mỗi số strobogrammatic nguyên tố
    
xuat2()
insoStrobogrammaticNguyenTo1(1000000)