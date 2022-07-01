import numpy as np
#경사 하강법의 단점을 보완하는 확률적 경사 하강법(stochastic gradient descent)


#∇βκ||y - Xβ||2 = δβκ||y - Xβ||2 = -XT.κ * (y - Xβ) / n||y- Xβ||2

#경사 하강법 기반 선형회귀 알고리즘
#Input : X,y,lr,T(학습횟수)
#Output : beta
'''
for t in range(T):
    error = y - X @ beta
    grad = - transpose(X) @ error
    beta = beta - lr * grad
    #∇β||y - Xβ||2**2를 계산해서 β를 업데이트 한다
'''
'''
X = np.array([[1,1], [1,2], [2,2], [2,3]])
y = np.dot(X, np.array([1,2])) + 3

beta_gd = [10.1, 15.1, -6.5]#[1,2,3]이 정답
X_ = np.array([np.append(x,[1])for x in X])#intercept 항 추가

for t in range(5000):
    error = y - X_ @ beta_gd
    #error = error / np.linalg.norm(error)
    grad = - np.transpose(X_) @ error
    beta_gd = beta_gd - 0.01 * grad

print(beta_gd)
#경사 하강법은 볼록한 함수에 대해선 적절한 학습률과 학습 횟수를 선택했을 때 수렴이 보장되어 있다.
#특히 선형회귀의 경우 목적식||y-Xβ||2은 회귀계수 β에 대해 볼록함수이기 떄문에 알고리즘을 충분히 돌리면 수렴이 보장된다.
#하지만 비선형회귀 문제의 경우 목적식이 볼록하지 않을 수 있으므로(딥러닝에선 보통 비선형) 수렴이 항상 보장되지는 않는다.
'''

#확률적 경사하강법(stochastic gradient descent)은 데이터 한개 또는 일부 활용하여 업데이트
#한개만 사용하여 업데이트 하는걸 SGD(확률적 경사 하강법)라 하고 일부 사용하는걸 mini batch라 한다.
#Mini-batch gradient descent(MGD)