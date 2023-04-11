import math
print('Nhap hai canh ke cua tam giac vuong:')
a=int(input())
b=int(input())
CanhHuyen=math.sqrt(a*b)
print('Canh ke thu nhat la:',a,end=(', '))
print('canh ke thu hai la:',b,end=(', '))
print('co canh huyen =',round(CanhHuyen,2))
