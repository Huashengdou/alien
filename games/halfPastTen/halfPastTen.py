
playerName = input("请输入玩家姓名：")
print("welcome "+ playerName)
money = input("请输入玩家筹码：")

if int(money) < 0:
    print("input error,please repeate")
else:
    print(playerName + " 输入的筹码为 " + money)

a = 1
b = 2
print("#%3d#%3d"%(a,b))