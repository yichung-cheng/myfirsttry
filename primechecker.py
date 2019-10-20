#找出範圍 a 內所有質數

a = int(input()) #輸入要檢查範圍
for i in range(2, a+1): # 2 ~ a 一個個檢查
    flag = True # 找到可以整除的數就變成 False
    for j in range(2,i): #從 2 到 i-1檢查 p.s.其實這裡可以優化 想想看
        if(i % j == 0): #不是質數
            flag = False 
            break
    if flag:
        print(i)
