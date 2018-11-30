from die import Die

# 创建一个骰子
die = Die()

# 掷色子并将结果存在一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)