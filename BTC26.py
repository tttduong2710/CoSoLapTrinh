HoTen=input('Ho ten: ')
SNC=int(input('So ngay cong: '))
DGNC=int(input('Don gia ngay cong: '))
HSPC=float(input('He so phu cap: '))
TU=int(input('Tam ung: '))
Luong=DGNC*SNC*HSPC
ThucLinh=Luong-TU
print('Nhan vien',HoTen,',',end=)
print('Co tien luong='+str(round(Luong,1),end=','))
print(' Tam ung='+str(TU),'va Thuc linh='+str(round(ThucLinh,1)))
