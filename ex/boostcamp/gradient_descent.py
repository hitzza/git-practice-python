from mimetypes import init
import sympy as sym #sympy = 미분함수
from sympy.abc import x, y #import한 기호를 실제 방정식 기호처럼 사용가능하게 하는 모듈
import numpy as np

#print(sym.diff(sym.poly(x**2 + 2*x + 3), x))#x**2 + 2*x + 3를 x로 미분하라는 의미
#Poly(2*x + 2, x, domain='ZZ')

#미분은 함수f의 주어진점 (x, f(x))에서의 접선의 기울기를 구하는 것
#미분값을 더하면 경사 상승법(gradient ascent)라 하며 함수의 극대값의 위치를 구할때 사용
#반대로 미분값을 빼면 경사 하강법(gradient descent)라 하고, 극소값의 위치를 구할떄 사용

#경사 하강법 알고리즘
#Input : gradient, init, lr, eps
#Output : var
#gradient - 미분을 계산하는 함수, init - 시작점, lr -학습률, eps - 알고리즘 종료 조건
'''
var = init
grad = gradient(var)
while (abs(grad) >  eps):
    var = var - lr * grad
    grad = gradient(var)
'''
#함수가 fx = x**2 + 2x + 3일때 경사 하강법으로 최소점 찾기
#변수가 하나일 경우
'''
def func(val):#미분해주는 함수
    fun = sym.poly(x**2 + 2*x + 3)
    return fun.subs(x, val), fun#subs(x,val)은 x에 val을 대입하라는 뜻인듯, [0]: 대입한 결과 값 ,[1]미분계수

def func_gradient(fun, val):#미분한 값을 리턴해주는 함수
    _, function = fun(val)#_ =결과값, function = 미분계수
    diff = sym.diff(function, x)
    return diff.subs(x, val), diff

def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon = 1e-5):#lr_rate = 0.01 epsilon = 1e-05 == 0.00001 
    cnt = 0#연산 횟수
    val = init_point
    diff, _ = func_gradient(fun, init_point)
    while np.abs(diff) > epsilon:#abs - 절대값
        val = val - lr_rate*diff #경사 하강법을 이용한 값을 val에 저장
        diff, _ = func_gradient(func, val)#diff에 입력받은 값을 미분한 결과 저장
        cnt += 1
    
    print("함수 : {}, 연산 횟수: {}, 최소점({}, {})".format(fun(val)[1], cnt, val, fun(val)[0]))

gradient_descent(fun = func, init_point= np.random.uniform(-2,2))
'''

#변수가 벡터일 경우(변수의 방향이 여러 방향) 편미분을 사용
#print(sym.diff(sym.poly(x**2 + 2*x*y + 3) * sym.cos(x + 2*y), x))
#경사 하강법 알고리즘
#Input : gradient, init, lr, eps
#Output : var
#gradient - 그레디언트 벡터를 계산하는 함수, init - 시작점, lr -학습률, eps - 알고리즘 종료 조건
#경사 하강법 알고리즘은 그대로 적용된다. 그러나 벡터는 절대값 대신 노름(norm)을 계산해서 종료 조건을 설정한다.
'''
var = init
grad = gradient(var)
while(norm(grad) > eps):
    var = var - lr * grad
    grad = gradient(var)
'''
def eval_(fun, val):
    val_x, val_y = val#입력받은 벡터값 val_x, val_y에 할당
    fun_eval = fun.subs(x, val_x).subs(y, val_y)#x,y에 val_x,val_y값 대입
    return fun_eval

def func_multi(val):
    x_, y_ = val
    func = sym.poly(x**2 + 2*y**2)
    return eval_(func, [x_, y_]), func #미분한 값을 리턴

def func_gradient(fun, val):
    x_, y_ = val
    _, function = fun(val)
    diff_x = sym.diff(function, x)
    diff_y = sym.diff(function, y)
    grad_vec = np.array([eval_(diff_x, [x_, y_]), eval_(diff_y, [x_, y_])], dtype=float)
    return grad_vec, [diff_x, diff_y] #x,y 각각 편미분한 값을 np.array 형태로 반환

def gradient_descent(fun, init_point, lr_rate = 1e-2, epsilon =1e-5):
    cnt = 0#횟수 카운트
    val = init_point
    diff, _ = func_gradient(fun, val)
    while np.linalg.norm(diff) > epsilon:
        val = val - lr_rate *diff
        diff, _ = func_gradient(fun, val)
        cnt += 1
    
    print("함수: {}, 연산횟수: {}, 최소점: ({}, {})".format(fun(val)[1], cnt, val, fun(val)[0]))

pt = [np.random.uniform(-2, 2), np.random.uniform(-2, 2)]
gradient_descent(fun = func_multi, init_point= pt)