"""5)	Дано набор из целых чисел, содержащий по крайней мере два нуля.
Вывести сумму чисел из данного набора, расположенных между последними двумя нулями
(если последние нули идут подряд, то вывести 0)."""
a=[]
a=input().split()
i=-1
while a[i]!='0':
    i-=1
i-=1
sum=0
while a[i]!='0':
    sum+=int(a[i])
    i-=1
print(sum)
