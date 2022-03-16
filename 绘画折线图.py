# 年度报告折折线图
import matplotlib.pyplot as plt

Benz = [3367, 4321, 4460]
Audi = [3580, 4067, 2799]
Bmw = [2830, 3397, 4910]
seq = [2018, 2019, 2020]

plt.xticks(seq)  # 规定X轴的刻度数量

lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineAudi, = plt.plot(seq, Audi, '-o', label='Audi')
lineBmw, = plt.plot(seq, Bmw, '-^', label='Bmw')
plt.legend(handles=[lineBenz, lineAudi, lineBmw], loc='upper left', bbox_to_anchor=(1, 1))
# 添加图例
plt.title('Sales Reporter', fontsize=24)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of the Sales', fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.savefig('sales_reporter.jpg',bbox_inches='tight')  # 保存图片
plt.show()


