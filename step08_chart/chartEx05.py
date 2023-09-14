import matplotlib.pyplot as plt

fig = plt.figure()

# 한글깨짐 처리
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size']=15

ax = fig.add_subplot(1, 1, 1)



ax.set_xlim([0., 10.])  # x축에 대해서 0~10
ax.set_ylim([0., 2.5])  # y축에 대해서 0.0 ~ 2.5
ax.set_title('Chart 연습', size=15)
ax.set_xlabel('x-axis', size=10)
ax.set_ylabel('y-axis', size=10)

plt.show()
