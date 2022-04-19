#Inheritance 상속
'''
class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은",self.name, "이구요, 제 나이는", self.age, "살 입니다.")
    #def __str__(self):
    #    return print(f"저의 이름은 {self.name}이고 나이는 {self.age}입니다")

#class Korean(Person):
#    pass

#first_korean = Korean("name", 10)
#print(first_korean)
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)#부모 객체 사용
        self.salary = salary
        self.hire_date = hire_date#속성값 추가

    def do_work(self):
        print("열심히 일을 합니다.")

    def about_me(self):#부모 클래스 함수 재정의
        super().about_me()#부모 클래스 함수 사용
        print("제 급여는", self.salary,"원 이구요, 제 입사일은 ", self.hire_date,"입니다.")

hi = Employee("name", 10, "male", 3000, "1010")
print(hi.about_me())
'''
#polymorphism 다형성
'''
class Animal:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Cat(Animal):
    def talk(self):
        return "Meow!"

class Dog(Animal):
    def talk(self):
        return "Woof! Woof!"
print(Dog.talk("dog"))
print(Cat.talk("cat"))
animals = [Cat('Missy'), Cat('Mr. Mistoffeless'), Dog('Lassie')]
for animal in animals:
    print(animal.name + ':' + animal.talk())
'''
#visibility 
class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []#변수 앞에 __를 사용햐면 private 변수 선언 타객체가 접근 못함

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)
    
    @property  #property decorator 숨겨진 변수를 반환하게 해줌
    def items(self):
        return self.__items

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory)
#my_inventory.__items.append("aaa")

items = my_inventory.items
items.append("aa")
print(my_inventory)
print(my_inventory.get_number_of_items())