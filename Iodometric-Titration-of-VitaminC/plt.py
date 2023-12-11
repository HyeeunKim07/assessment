import matplotlib.pyplot as plt
import numpy as np

# 적정 시간과 비타민 C 양 데이터
time = [0, 1, 2, 3, 4, 5]  # 시간 (분)
vitamin_c_amount = [0.1, 0.08, 0.06, 0.04, 0.02, 0.0]  # 비타민 C 양 (mol)

# 그래프 생성
plt.plot(time, vitamin_c_amount, marker='o', linestyle='-', color='b')

# 축과 제목 설정
plt.xlabel('Time (min)')
plt.ylabel('Vitamin C Amount (mol)')
plt.title('Vitamin C Titration')

# 그래프 출력
plt.show()
