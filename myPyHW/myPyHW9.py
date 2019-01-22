#二分查找法  lst = [1,3,6,7,8,10,15,18]
#coding=utf-8

def binarySearch(lst,target,start,end):
    mid = int( (start + end) / 2)
    if(start > end):
        print('Not found')
        return
    if(target < lst[mid]):
        string=binarySearch(lst,target,start,mid-1)
    elif(target > lst[mid]):
        string=binarySearch(lst,target,mid+1,end)
    elif(target == lst[mid]):
        print('Found')
        return

lst = [1,3,6,7,8,10,15,18]
binarySearch(lst,3,0,len(lst)-1)
 
        