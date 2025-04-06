class Unit:
    def __init__(self):
        print('유닛 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__() #다중상속 받을 때 super()를 사용하면 순서상 맨 처음에 상속받는 클래스만 init함수가 호출됨
        Unit.__init__(self)
        Flyable.__init__(self)
# 드랍쉽
dropship=FlyableUnit()