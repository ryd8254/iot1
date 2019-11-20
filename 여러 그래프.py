


import matplotlib.pyplot as plt

plt.figure()
'''
    하나의 창에 여러개의 그래프를 넣기 위한 함수
    subplot(m, n, idx) m : 행, n : 열, idx : 위치를 의미함
'''

plt.subplot(2,1,1)
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])

plt.subplot(2,1,2)
plt.plot([5,6,7,8], [5,6,7,8])

plt.show()
