import matplotlib.pyplot as plt

fig = plt.Figure(1, (6, 8), dpi=200) # 确定图形高为6，宽为8；图形清晰度

# 子图1
ax1 = plt.subplot(211) # 2行，1列，第1个图，这样一个图就是：高3、宽8
					   # 绘制单个图像使用 plt.subplot(111)

# 具体绘图
plt.plot()  # 折线图
plt.scatter()  # 散点图


# 参数设置
plt.xlabel('Relative Time(s)', fontsize=14)
plt.ylabel('Distance to stop bar(m)', fontsize=14)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(np.arange(0, 1100, 100), fontsize=14)
plt.yticks(np.arange(0, 90, 10), fontsize=14)
plt.title('Figure_name', fontsize=20)

plt.tight_layout()  # 避免保存的图片文字被裁减
plt.axis('off')  # 去除坐标轴
plt.legend()  # 显示图注


# 子图2
ax2 = plt.subplot(212) # 2行，1列，第2个图
# ...与上面类似


# 存储图片
file_path = 'image/xxx.png'
plt.savefig(file_path, dpi=200)