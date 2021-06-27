#range 範圍
#Python內建功能:清單產生器

import random
range(10)
for i in range(10):
	r = random.randint(1, 100)
	print('這是產生第', i + 1, '次產生隨機數', r)

#range的應用
#range(開始值, 結束值, 遞增值)

#range(2, 5) = [2, 3, 4]
#range(2, 5, 2) = [2, 4]  range中最後一個2 是遞增值/遞減值