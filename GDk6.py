#Techgym7-2-A-1

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

# x、y座標
#-1から1まで0.1刻み
ar_min = -1.0
ar_max = 1.0
notch = 0.1

X =
Y =

#グリッド数
grid_num =

# 出力を格納するグリッド
Z =

#シグモイド関数
def sigmoid_function(x):
    

# x、y座標の入力の重み、バイアス
w_x = 2.5
w_y = 3.0
bias = 0.1

# グリッドの各マスでニューロンの演算
for i in range(grid_num):
    for j in range(grid_num):
        

# グリッドの表示
plt.imshow(Z, "gray", vmin = 0.0, vmax = 1.0)
plt.colorbar()
plt.show()
