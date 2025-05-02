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
    def __init__(self,name,hp,speed): # init 생성자 
        self.name=name #멤버변수 : 클래스 내에서 정의된 변수
        self.hp=hp
        self.speed=speed
    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동 [속도 {2}]'.format(self.name,location,self.speed))

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
    def __init__(self,name,hp,speed,damage): # init 생성자 
        Unit.__init__(self,name,hp,speed) #상속
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
        print('{0} : {1} 방향으로 비행 [속도 : {2}]'.format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable): #다중상속
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp,0, damage) #지상 speed=0
        Flyable.__init__(self,flying_speed)
    def move(self,location):
        print('[공중 유닛 이동]')
        self.fly(self.name,location)
#벌쳐 : 지상유닛, 기동성 좋음
vulture=AttackUnit('벌쳐',80,10,20)

#배틀크루저 : 공중유닛
battlecruiser=FlyableAttackUnit('배틀크루저',500,25,3)
vulture.move('11시')
#battlecruiser.fly(battlecruiser.name,'9시')
battlecruiser.move('9시')



#파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit('파이어뱃',50,16)
# firebat1.attack('5시')

# firebat1.damaged(25)
# firebat1.damaged(25)
#------------------------------------------------------------------------
#   Unit(move())    Flyable
#    |                 |
#   AttackUnit         |
#     \                |
#      \               |
#       FlyableAttackUnit (move() 재정의)
#------------------------------------------------------------------------

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) #super()는 self없이
        self.location=location

#서플라이 디폿 : 건물, 1개 건물 = 8유닛
supply_depot=BuildingUnit('서플라이 디폿',500,'7시')




#패스
# 아무것도 안하고 일단 넘김
# def game_start():
#     print('[알림] 새로운 게임을 시작합니다')

# def game_over():
#     pass

# game_start()
# game_over()
#-----------------------------------------------------------------------
#퀴즈
#주어진 코드를 활용해 부동산 프로그램을 작성
#출력예제
# 총 3대의 매물이 있습니다
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

#코드

class House:
    #매물 초기화
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year

    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses=[]
house1=House('강남','아파트','매매','10억','2010년')
house2=House('마포','오피스텔','전세','5억','2007년')
house3=House('송파','빌라','월세','500/50','2000년')
houses.append(house1)
houses.append(house2)
houses.append(house3)

print('총 {0}대의 매물이 있습니다'.format(len(houses)))
for house in houses:
    house.show_detail()
#------------------------------------------------------------------------------
#예외처리
try:
    print('나누기 전용 계산기')
    nums=[]
    nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
    nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
    nums.append(int(nums[0]/nums[1]))
    print('{0} / {1} = {2}'.format(nums[0],nums[1],nums[2]))
    
except ValueError:
    print('에러발생')
except ZeroDivisionError as err: #0으로 나눌수 없다는 에러메시지 출력
    print(err) #division by zero
except:
    print('알 수 없는 에러가 발생')
#-----------------------------------------------------------------------------------
#에러 발생시키기
try:
    print('한 자리 숫자 나누기 전용 계산기')
    num1=int(input('첫 번째 숫자를 입력 :'))
    num2=int(input('두 번째 숫자를 입력 :'))
    if num1>=10 or num2>=10:
        raise ValueError
    print('{0}/{1}={2}'.format(num1,num2,int(num1/num2)))
except ValueError:
    print('잘못된 값을 입력하였습니다 한 자리 숫자만 입력하세요')
#-----------------------------------------------------------------------------------
#사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    print('한 자리 숫자 나누기 전용 계산기')
    num1=int(input('첫 번째 숫자를 입력 :'))
    num2=int(input('두 번째 숫자를 입력 :'))
    if num1>=10 or num2>=10:
        raise BigNumberError('입력값 : {0},{1}'.format(num1,num2))
    print('{0}/{1}={2}'.format(num1,num2,int(num1/num2)))
except ValueError:
    print('잘못된 값을 입력하였습니다 한 자리 숫자만 입력하세요')
except BigNumberError as err:
    print('에러가 발생 한 자리 숫자만 입력하세요')
    print(err) #line 200
#------------------------------------------------------------------------------
#finally
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    print('한 자리 숫자 나누기 전용 계산기')
    num1=int(input('첫 번째 숫자를 입력 :'))
    num2=int(input('두 번째 숫자를 입력 :'))
    if num1>=10 or num2>=10:
        raise BigNumberError('입력값 : {0},{1}'.format(num1,num2))
    print('{0}/{1}={2}'.format(num1,num2,int(num1/num2)))
except ValueError:
    print('잘못된 값을 입력하였습니다 한 자리 숫자만 입력하세요')
except BigNumberError as err:
    print('에러가 발생 한 자리 숫자만 입력하세요')
    print(err) #line 200
finally: #에러가 발생하는것에 상관없이 무조건 실행
    print('계산기를 종료합니다') 
#-----------------------------------------------------------------------
#모듈
#import theater_module
#theater_module.price(3) #3명이서 영화
#theater_module.price_morning(4) #4명이서 조조할인
#theater_module.price_soldier(5) #군인 5명

#import theater_module as mv # 별명설정으로 줄이기
#mv.price(3)
#mv.price_morning(4)
#mv.price_soldier

# from theater_module import * # 모듈에있는 모든것을 사용
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price,price_morning # 원하는것만 import
price(5)
price_morning(6)
#-----------------------------------------------------------------------
#내장함수
#https://docs.python.org/3/py-modindex.html
#input : 사용자의 입력을 받는 함수
#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())
lst=[1,2,3]
print(dir(lst))

name='Jim'
print(dir(name))
#------------------------------------------------------------------------
#외장함수
#https://docs.python.org/3/py-modindex.html
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob('*.py')) #확장자가 py인 모든파일

# os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) #현재 디렉터리
# folder = 'sample_dir'
# if os.path.exists(folder):
#     print('이미 존재하는 폴더입니다')
#     os.rmdir(folder)
#     print(folder,'폴더가 삭제되었습니다')
# else:
#     os.makedirs(folder) #폴더생성
#     print(folder,'폴더가 생성되었습니다')
#print(os.listdir()) # 현재 디렉터리와 파일들

#time : 시간 관련 함수
import time
print(time.localtime)
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print('오늘 날짜는 ',datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today=datetime.date.today() #오늘날짜 저장
td=datetime.timedelta(days=100) #100일 저장
print('우리가 만난지 100일은 ',today+td) #오늘부터 100일 후