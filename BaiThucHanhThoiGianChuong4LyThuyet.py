from datetime import *
import calendar

print ('Nam hien tai : ', datetime.now().strftime("%Y"))
print ('Thang hien tai : ', datetime.now().strftime("%B"))
print ('Tuan hien tai la  tuan thu may trong nam : ', datetime.now().strftime("%W"))
print (calendar.monthcalendar(2026,4))
print ('Tuan hien tai la  tuan thu may trong thang : ', datetime.now().strftime("%U"))
print ('Ngay hien tai la ngay thu may trong nam : ', datetime.now().strftime("%j"))
print ('Ngay duong lich hien tai : ', datetime.now().strftime("%D"))
print ('Thu cua ngay hien tai : ', datetime.now().strftime("%A"))
print ('Gio phut giay hien tai : ', datetime.now().strftime("%T"))

s = '''23/4/2024 12:30:45'''
s1 = '''23/4/2026 12:30:45'''
print ('Nhap Ngay, Thang, Nam cua 2 ngay')
ngay1,thang1,nam1 = map(int, input("Nhap ngay 1, thang 1, nam 1 : ").split())
ngay2,thang2,nam2 = map(int, input("Nhap ngay 2, thang 2, nam 2 : ").split())
date1 = date(nam1, thang1, ngay1)
date2 = date(nam2, thang2, ngay2)
# date1 = datetime.strptime(s, "%d/%m/%Y %H:%M:%S")
# date2 = datetime.strptime(s1, "%d/%m/%Y %H:%M:%S")
print ('So ngay giua 2 ngay la : ', abs((date2 - date1).days))


print ('Nhap 1 chuoi thang ngay nam gio ')
thang = input("Nhap thang : ") 
ngay = input("Nhap ngay : ")
nam = input("Nhap nam : ")
gio = input("Nhap gio : ")
phut = input("Nhap phut : ")
# s = ngay + '' + thang + '' + nam + ' ' + gio + '' + phut + ''
# # date = datetime.strptime(s, "%d%m%Y %H%M")
s = datetime(int(nam), int(thang), int(ngay), int(gio), int(phut))
print(s.strftime("%d %m %Y %H:%M%p"))


t1 = datetime.now()
t2 = timedelta(seconds=5)
t3 = t1 + t2    
print ('Thoi gian hien tai la : ', t1.strftime("%H:%M:%S"))
print ('Thoi gian sau 5 giay la : ', t3.strftime("%H:%M:%S"))