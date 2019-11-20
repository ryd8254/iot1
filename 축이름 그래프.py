from matplotlib import font_manager, rc

import matplotlib
import matplotlib.pyplot as plt

font_location = 'C:/Windows/Fonts/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_location).get_name()

matplotlib.rc('font', family=font_name)

plt.title('matplotlib 활용')
plt.xlabel('X축')
plt.ylabel('Y축')
plt.plot([1,2,3,4,],[1,2,3,4,])
plt.text(3.5,3.0, '평균 : 2.5')
plt.grid(True)
plt.show()
