
playerName = input("请输入第一个玩家姓名：")
print("welcome "+ playerName)
card1 = input("请输入第一张牌：")
card2 = input("请输入第二张牌：")

print("第一张牌为："+ card1)
print("第二张牌为："+ card2)

if card1[0] == "A":
    card1_number = 1
elif card1[0] == 'J' or card1[0] == "Q" or card1[0] == "K":
    card1_number = 0.5
elif len(card1) >= 2:
    card1_number = 10
else:
    card1_number = int(card1[0])

print(card1_number)
money = input("请输入玩家筹码：")

if int(money) < 0:
    print("input error,please repeate")
else:
    print(playerName + " 输入的筹码为 " + money)

a = 1
b = 2
print("#%3d#%3d"%(a,b))