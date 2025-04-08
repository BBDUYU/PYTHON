from random import *

# 유닛
class Unit:
    def __init__(self,name,hp,speed): # init 생성자 
        self.name=name #멤버변수 : 클래스 내에서 정의된 변수
        self.hp=hp
        self.speed=speed
        print('{0} 유닛이 생성되었습니다'.format(name))

    def move(self, location):
        print('{0} : {1} 방향으로 이동 [속도 {2}]'.format(self.name,location,self.speed))

    def damaged(self,damage):
        print('{0} : {1} 데미지를 입었습니다'.format(self.name,damage))
        self.hp -=damage
        print('{0} : 현재 체력은 {1}'.format(self.name,self.hp))
        if self.hp <=0:
            print('{0} : 파괴되었습니다'.format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage): # init 생성자 
        Unit.__init__(self,name,hp,speed) #상속
        self.damage=damage
    def attack(self,location):
        print('{0} : {1} 방향으로 공격합니다 [공격력 : {2}]'.format(self.name,location,self.damage))
        
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,'마린',40,1,5)
    #스팀팩 : 일정시간 이동 및 공격속도 증가, 체력10감소
    def stimpack(self):
        if self.hp >10:
            self.hp -=10
            print('{0} : 스팀팩을 사용합니다 (HP 10 감소)'.format(self.name))
        else:
            print('{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다'.format(self.name))

class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜 강한 공격 가능. 이동불가
    seize_developed=False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self,'탱크',150,1,35)
        self.seize_mode=False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        #현재 시즈모드가 아닐 때
        if self.seize_mode==False:
            print('{0} : 시즈모드로 전환합니다'.format(self.name))
            self.damage *=2
            self.seize_mode=True
            self.speed=0
        #현재 시즈모드일 때
        else:
            print('{0} : 시즈모드를 해제합니다'.format(self.name))
            self.damage /=2
            self.seize_mode=False
            self.speed=1
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self,name,location):
        print('{0} : {1} 방향으로 비행 [속도 : {2}]'.format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable): #다중상속
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp,0, damage) #지상 speed=0
        Flyable.__init__(self,flying_speed)
    def move(self,location):
        self.fly(self.name,location)

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,'레이스',80,20,5)
        self.clocked=False #클로킹 모드 (해제상태)
    
    def clocking(self):
        if self.clocked==True: #클로킹 모드일 때
            print('{0} : 클로킹 모드를 해제합니다'.format(self.name))
            self.clocked=False
        else: #클로킹 모드가 아닐 때
            print('{0} : 클로킹 모드 설정합니다'.format(self.name))
            self.clocked=True

def game_start():
    print('[알림] 게임을 시작합니다')

def game_over():
    print('Player : gg')
    print('[Player] 님이 게임에서 퇴장하셨습니다')

# 실제 게임 진행
game_start()
#마린 3 생성
m1=Marine()
m2=Marine()
m3=Marine()
#탱크 2 생성
t1=Tank()
t2=Tank()
#레이스 1 생성
w1=Wraith()

#유닛 일괄 관리
attack_units =[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move('1시')
#탱크 시즈모드
Tank.seize_developed=True
print('[알림] 탱크 시즈모드 개발이 완료되었습니다')

#공격모드 준비 (탱크:시즈모드, 레이스:클로킹, 마린:스팀팩)
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack('1시')

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음 (5~20)

#게임종료
game_over()

#   Unit                 Flyable
#    |                      |
# AttackUnit                |
#  |      |  \              |
# Marine Tank \             |
#              \            |
#               FlyableAttackUnit
#                        |
#                      Wraith      