#class
# 마린 : 공격 유닛, 군인, 총을 쏨
# name='마린' #유닛의 이름
# hp=40 #유닛의 체력
# damage=5 #유닛의 공격력
# 
# print('{0} 유닛이 생성되었습니다'.format(name))
# print('체력 {0}, 공격력 {1}'.format(hp,damage))
# 
#탱크 : 공격 유닛, 탱크, 포를 쏨
# tank_name='탱크'
# tank_hp=150
# tank_damage=35
# 
# print('{0} 유닛이 생성되었습니다'.format(tank_name))
# print('체력 {0}, 공격력 {1}'.format(tank_hp,tank_damage))
# 
# def attack(name, location, damage):
    # print('{0} : {1} 방향으로 적군을 공격한다. [공격력 : {2}]'.format(name,location,damage))
# attack(name,'1시',damage)
# attack(tank_name,'1시',tank_damage)

# 일반 유닛
class Unit:
    def __init__(self,name,hp): # init 생성자 
        self.name=name #멤버변수 : 클래스 내에서 정의된 변수
        self.hp=hp

# marine1 = Unit('마린',40,5)
# marine2 = Unit('마린',40,5)
# tank=Unit('탱크',150,35)
# 레이스 : 공중 유닛, 비행기
# wraith1=Unit('레이스',80,5)
# print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name,wraith1.damage))
# 
# wraith2=Unit('빼앗은 레이스',80,5)
# wraith2.clocking=True
# 
# if wraith2.clocking==True:
    # print('{0}는 현재 클로킹 상태입니다'.format(wraith2.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,damage): # init 생성자 
        Unit.__init__(self,name,hp) #상속
        self.damage=damage
    def attack(self,location):
        print('{0} : {1} 방향으로 공격합니다 [공격력 : {2}]'.format(self.name,location,self.damage))
        
    def damaged(self,damage):
        print('{0} : {1} 데미지를 입었습니다'.format(self.name,damage))
        self.hp -=damage
        print('{0} : 현재 체력은 {1}'.format(self.name,self.hp))
        if self.hp <=0:
            print('{0} : 파괴되었습니다'.format(self.name))

#메딕 : 의무병

#드랍쉽 : 공중유닛, 수송기, 공격 X

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self,name,location):
        print('{0} : {1} 방향으로 날아갑니다 [속도 : {2}]'.format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable): #다중상속
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp, damage)
        Flyable.__init__(self,flying_speed)

#발키리 : 공중 공격 유닛
valkyrie=FlyableAttackUnit('발키리',200,6,5)
valkyrie.fly(valkyrie.name,'3시')

#파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃',50,16)
firebat1.attack('5시')

firebat1.damaged(25)
firebat1.damaged(25)
#------------------------------------------------------------------------
#   Unit            Flyable
#    |                 |
#   AttackUnit         |
#     \                |
#      \               |
#       FlyableAttackUnit
#------------------------------------------------------------------------