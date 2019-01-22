#实现函数  rfind(string,sub)  ，反向查找sub在string中的位置
#例如字符串 "cde,ab,cdeaba" 反向查找子串cde ，返回值应该为7
#coding=utf-8

def rfind(string,sub):
    index = -1
    for i in range(len(string)-1,-1,-1):
        index = i
        j=0
        while(string[i] == sub[j]):
            i += 1 
            j += 1
            if(j == len(sub)):
                return index

string = "cde,ab,cdeaba"
sub='cde'
print(rfind(string,sub))