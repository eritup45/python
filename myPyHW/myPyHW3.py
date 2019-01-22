#解答版:印出乘法表
#coding = utf-8
def get_line(number):
    line = ''
    str_foramt = "{left}*{right} = {result}  "
    for i in range(1,number+1):
        tmp = str_foramt.format(left=i,right = number,result=i*number)
        line += tmp
    return line

for i in range(1,10):
    print get_line(i)

#我的:印出乘法表(成功)
#maxnum=10
#for i in range(1,maxnum):
#    for j in range(1,maxnum):
#        if(j==i and j==maxnum-1):
#            print('%d*%d' %(j,i))
#        elif(j==maxnum-1):
#            print('')
#        elif(j>i):
#            print('',end='  ')
#        else:
#            print('%d*%d' %(j,i), end=' ')