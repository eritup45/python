#使用递归函数从终端输入5个字符串，倒序输出，比如输入的是 1，4，2，6，3，在输入完3以后，倒序输出 3 ，6 ，2 ，4， 1
def recur(n):
    value = input('Please input a string: ')
    n -= 1
    if(n == 0):
        print(value)
        return
    else:
        recur(n)
        print(value)

recur(5)    

    