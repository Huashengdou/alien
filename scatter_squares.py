import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]
plt.scatter(x_value, y_value, s=50)
#plt.scatter(2, 4, s=200)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Hahaha", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square", fontsize=24)

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()