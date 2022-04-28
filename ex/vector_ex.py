#vector란? 숫자를 원소로 가지는 list 또는 array
#벡터의 norm 노름은 원점에서부터의 거리
#l1 노름은 각 성분의 변화량의 절대값을 모두 더한값
#l2 노름은 피타고라스 정리를 이용해 유클리드 거리를 계산
import numpy as np
def l1_norm(x):
    x_norm = np.abs(x)#abs - 절대값 구하는 함수
    x_norm = np.sum(x_norm)
    return x_norm

def l2_norm(x):
    x_norm = x * x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)#sqrt - 제곱근을 구하는 함수
    return x_norm