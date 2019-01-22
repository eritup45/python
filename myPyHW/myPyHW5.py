#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
#求它在第10次落地时，共经过多少米？第10次反弹多高？
height = 100.0
time = 10
Sum=0
for i in range(1,time+1):
    Sum=height + height/2 + Sum
    height=height / 2
print('Total: %f' %Sum)
print('The height of %d times reboudance: %f' %(time,height/2))

