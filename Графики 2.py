# импортируем модули
import numpy as np
import matplotlib.pyplot as plt
# функция
y = lambda x: np.sin(x)
# создаём рисунок с координатную плоскость
fig = plt.subplots()
# создаём область, в которой будет
# - отображаться график
x = np.linspace(
# значения x, которые будут отображены
-3, 3,
# количество элементов в созданном массиве
# - качество прорисовки графика 
100)
# рисуем график
plt.plot(x, y(x))
# показываем график
plt.show()
