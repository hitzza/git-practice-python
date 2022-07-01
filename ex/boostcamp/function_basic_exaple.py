def calculrate_regtangle_area(x, y):
    result = x * y
    return result
'''
def ex_funtion(x):
    x = 2 
    fx = 2*x + 7
    gx = x**2
    fgx = 2*gx +7
    gfx = fx**2
    result = fx + gx + fgx + gfx
    return result, fx, gx, fgx, gfx
'''
#me
def f(x):
    return 2 * x + 7
def g(x):
    return x**2
x = 2
#ex


rectangle_x = 10
rectangle_y = 20
print("사각형의 x는 %d 입니다" %(rectangle_x))
print("사각형의 y는 %d 입니다" %(rectangle_y))
print("사각형의 넓이는 %d 입니다" %(calculrate_regtangle_area(rectangle_x,rectangle_y)))
#print("함수 답",ex_funtion(2))
print(f(x) + g(x) + f(g(x)) + g(f(x)))
#input & format ex
print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
input_c = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요:"))#input으로 받은 데이터 타입은 항항 str
change_f = (9/5) * input_c + 32
print(f"섭씨온도 : {input_c} 화씨온도:{change_f:.2f}")