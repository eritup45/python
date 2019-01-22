#判断字符串是否为回文
def isPalindrome(string):
    for i in range(int(len(string)/2+1)):
        if(string[i] == string[-i-1]):
            result='It is palindrome'
            continue
        else:
            result='It isn\'t palindrome'
            return result
    return result

print(isPalindrome('lkdssdkl'))