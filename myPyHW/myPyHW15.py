#合并两个有序序列
#coding=utf-8

def merge_lst(lst1,lst2):
    lst = []
    i=0
    j=0
    while(i < len(lst1) and j < len(lst2)):
        if(lst2[j] < lst1[i]):
            lst.append(lst2[j])
            j += 1
        elif(lst2[j] >= lst1[i]):
            lst.append(lst1[i])
            i += 1
    for a in range(i,len(lst1)):
        lst.append(lst1[a])
    for b in range(j,len(lst2)):
        lst.append(lst2[b])
    return lst            

lst1 = [2,4,6,9]
lst2 = [3,5,8,10]
print(merge_lst(lst1,lst2))