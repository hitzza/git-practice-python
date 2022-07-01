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
    return 
    
#두 벡터 사이의 각도 구해보기(l2에서만 가능)
#제2 코사인 법칙에 의해 두 벡터 사이의 각도를 계산할 수 있다.
#cosθ = <x,y>(성분곱)/||x||2 * ||y||2
def angle(x,y):#inner함수로 내적을 계산
    v = np.inner(x,y) / (l2_norm(x) * l2_norm(y))
    theta = np.arccos(v)
    return theta
#내적은 정사영(orthogonal projection)된 벡타의 길이와 관련있다
#Proj(x)의 길이는 코사인법칙에 의해 ||x||cosθ가 된다
#내적(성분곱)<x,y> = (||x||2 * ||y||2)cosθ
#내적은 두 벡터의 유사도(similariyt)를 측정하는데 사용 가능하다