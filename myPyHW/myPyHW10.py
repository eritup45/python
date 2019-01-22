#实现字符串find方法，返回子串所在的位置
#coding=utf-8

def find(string,sub):
    for i in range(len(string)):
        for j in range(len(sub)):
            while(string[i]==sub[j]):
                if(j == len(sub)-1):
                    return i-len(sub)+1
                i += 1
                j += 1
    return 0

string = 'I love python!'
sub = '!'
sub2 = 'pyth'
print(find(string,sub))
print(find(string,sub2))