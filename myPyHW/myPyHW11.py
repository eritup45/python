#编写函数split(string,sep),根据分隔符sep分割字符串string
#coding=utf-8

def split(string,sep):
    lst=[]
    start = 0
    index = string.find(sep)
    while(index != -1):
        lst.append(string[start:index])
        start = index + 1
        index = string.find(sep, start, len(string))
    lst.append(string[start:])
    return lst

string = "abc,de,fg,hij"
sep = ","
print(split(string,sep))