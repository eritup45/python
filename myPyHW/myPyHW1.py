#允许用户从终端输入一个分数，程序输出这个分数所属的考评等级，90到100分是A，60到89是B，60分以下是C
score = input('Enter your grade: ')
score = int(score)
if(score <=100 and score >= 90):
    print('A')
elif(score <=89 and score >= 60):
    print('B')
else:
    print('C')