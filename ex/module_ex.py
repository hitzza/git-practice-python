import fah_converter

print("Enter a celsicus value:")
celsius = float(input())
fahrenheit = fah_converter.convert_c_to_f(celsius)
print("That's", fahrenheit, "degrees Fahrenheit")

#패키지 폴더별로 __init__.py구성하기
#해당 폴더가 패키지임을 알리는 초기화 스크립트
#없을경우 해당 폴더를 패키지로 간주하지 않음(python 3.3이상은 없어도 상관 없음)