#三角形周长和面积
# coding=utf-8
def getEdges(lst):
    if len(lst) != 3:
        return False, (0, 0, 0)
    try:
        # raw_input 获得用户的输入,得到的是字符串,这里把字符串转成float数值
        edge_lst = [float(item) for item in lst]
    except:
        return False, (0, 0, 0)
    return True, (edge_lst[0], edge_lst[1], edge_lst[2])
def triangleFunction():
    line = input('输入三角形的三个边长,用空格隔开,退出请输入q:')
    lst = line.split(' ')
    if(line == 'q'):
        return
    inputCorrect, edges = getEdges(lst)
    if(inputCorrect == False):
        print('input not correct')
        return 
    perimeter = 0
    for i in range(3):
        perimeter += edges[i]
    print('perimeter: ',perimeter)
    half_perimeter = perimeter/2
    area = (half_perimeter*(half_perimeter-edges[0])*(half_perimeter-edges[1])*(half_perimeter-edges[2])) ** 0.5
    print('area: ',area)

if(__name__ == '__main__'):
    triangleFunction()