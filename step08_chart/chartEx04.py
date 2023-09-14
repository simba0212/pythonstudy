import matplotlib.pyplot as plt

# fig = plt.figure(figsize=(10,10)) # 새 figure
# plt.show()

# fig = plt.figure()
# # 창을 가로 한 칸, 세로 한 칸으로 분할하고 그 중 첫번째 칸에 as라는 이름의 axes 생성
# ax = fig.add_subplot(1,1,1)
# plt.show()

fig = plt.figure()
# 창을 가로 한 칸, 세로 한 칸으로 분할하고 그 중 첫번째 칸에 as라는 이름의 axes 생성
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
plt.show()