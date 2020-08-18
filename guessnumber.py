import random
num=random.randint(1,10)
i=0
while i<5:
    ans=int(input('請輸入數字:'))
    if ans < num:
        print('太小了')
    elif ans > num:
        print('太大了')
    elif ans == num:    
        print('恭喜答對')
        print(i)
        break
    else:
        print('錯了')
    i=i+1