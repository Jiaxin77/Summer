import numpy as np

aero_arr = np.loadtxt('airfoil_self_noise.dat')
print(type(aero_arr))

# 将数据集内样本数量赋值给变量nb_samples
# >>>> show me the code <<<<

#nb_samples = len(aero_arr)
nb_samples = aero_arr.shape[0]


# >>>> show me the code <<<<

aero_arr




import cv2
import matplotlib.pyplot as plt

messi = cv2.imread('messi5.jpg')


# 修改messi，使图片颜色正常显示，赋值给变量messi_rgb
# >>>> make messi colorful again <<<<

#顺序颠倒，搓螺旋丸题中有的
#还未ok【！！！】
messi_rgb = messi 


# >>>> make messi colorful again <<<<

plt.imshow(messi_rgb)
'''
输入数据

频率(Hertzs)
攻角(degrees)
弦长(meters)
流速(meters per second)
吸力面位移厚度(meters)
输出结果

声压(decibels)
'''
#简单机器学习

import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


aero_arr = np.loadtxt('airfoil_self_noise.dat')

X = aero_arr[:,:5]
y = aero_arr[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 构建线性回归模型
regr = linear_model.LinearRegression()

# 基于训练数据进行拟合
# >>>> replace the ____ <<<<
regr.fit(X_train,y_train)

# 对测试数据做预测
# >>>> replace the ____ <<<<
y_pred = regr.predict(X_test)


# 评估预测结果
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print('Variance score: %.2f' % r2_score(y_test, y_pred))