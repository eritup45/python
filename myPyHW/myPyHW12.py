#实现字符串replace方法
#coding=utf-8

#解答作法
def replace(string,old,new):
    lst = string.split(old)
    if len(lst) == 1:
        return lst[0]
    else:
        return new.join(lst)

string = "abcdeaba"
print(replace(string,'a','c'))

#我的作法(成功)
"""def replace(string,old,new):
    nstr = ''
    start = 0
    index = string.find(old)
    while(index != -1):
        nstr += string[start:index]
        nstr += new
        start = index + 1
        index = string.find(old,start)
    nstr += string[start:]
    return nstr

string = "abcdeaba"
print(replace(string,'a','c'))"""