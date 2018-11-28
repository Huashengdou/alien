import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x ** 2 for x in x_value]
# edgecolors删除数据点轮廓，s是数据点大小
# 自定义颜色，c代表
plt.scatter(x_value, y_value,c = 'red', edgecolors='none', s=50)
#plt.scatter(2, 4, s=200)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Hahaha", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square", fontsize=24)

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([10, 1100, 0, 1100000])
plt.show()