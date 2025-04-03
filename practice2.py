#continue & break
#반복문 내에서 사용가능
absent=[2,5] #결석
no_book=[7] #책이없음
for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue #밑에 문장을 실행하지 않고 반복
    elif student in no_book:
        print('오늘 수업은 여기까지 {0},교무실로'.format(student))
        break
    print('{0},책을 읽어'.format(student))
#--------------------------------------------------
#한줄 for
# 출석번호 1,2,3,4 앞에 100을 붙여야함 -> 101, 102,103,104
students=[1,2,3,4,5]
students=[i+100 for i in students]
print(students)
#학생이름을 길이로 변환
students=['Iron man','Thor','Groot']
students=[len(i) for i in students]
print(students)
#학생이름을 대문자로 변환
students=['Iron man','Thor','Groot']
students=[i.upper() for i in students]
print(students)
#------------------------------------------------------
#quiz
#50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성
#조건1 : 승객별 운행 소여시간은 5~50분 사이의 난수
#조건2 : 당신은 소요시간 5~15분 사이의 승객만 매칭
#출력문 예제
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 16분)
# 총 탑승 승객 : 2명
from random import *
cnt=0
for i in range(1,51): #1~50명
    time=randrange(5,51) #5분~50분
    if 5<=time <=15: #5분~15분 이내의 손님, 탑승 승객수 증가 
        print('[o] {0}번째 손님 (소요시간 : {1}분)'.format(i,time))
        cnt +=1
    else: #매칭 실패한 경우
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i,time))
print('총 탑승 승객 : {0}명'.format(cnt))
#-----------------------------------------------------------
#함수
def open_account():
    print('새로운 계좌가 생성되었습니다')

open_account()
#-------------------------------------------------------------------------------
#전달값과 반환값
def deposit(balance,money): #입금하려는 금액, 잔액
    print('입금이 완료되었습니다. 잔액은{0} 원입니다'.format(balance+money))
    return balance+money

def withdraw(balance,money): #출금
    if balance>=money: #잔액이 출금보다 많으면
        print('출금이 완료되었습니다. 잔액은 {0}원입니다'.format(balance-money))
        return balance-money
    else:
        print('출금이 완료되지 않았습니다. 잔액은 {0}원입니다'.format(balance))
        return balance

def withdraw_night(balance,money):
    commission = 100 #수수료
    return commission,balance-money-commission

balance=0
balance=deposit(balance,1000)
#balance=withdraw(balance,500)
commission,balance=withdraw_night(balance,500)
print('수수료는 {0}원이며, 잔액은 {1}원입니다.'.format(commission,balance))
#-------------------------------------------------------------------------------
#기본값
#def profile(name,age,main_lang):
#    print('이름 : {0}\t나이 : {1}\t주 사용언어 : {2}'.format(name,age,main_lang))

#profile('유재석',20,'파이썬')
#profile('김태호',25,'자바')
# 같은 학교, 같은 반, 같은 수업
def profile(name,age=17,main_lang='파이썬'):
    print('이름 : {0}\t나이 : {1}\t주 사용언어 : {2}'.format(name,age,main_lang))

profile('유재석')
profile('김태호')
#---------------------------------------------------------------------------------
#키워드 값
def profile(name,age,main_lang):
    print(name,age,main_lang)

profile(name='유재석',main_lang='파이썬',age=20)
profile(main_lang='자바',age=25,name='김태호')
#---------------------------------------------------------------------------------
#가변인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print('이름 : {0}\t나이 : {1}\t'.format(name,age),end=' ')
#     print(lang1,lang2,lang3,lang4,lang5)
def profile(name,age,*language): # * 가변인자
    print('이름 : {0}\t나이 : {1}\t'.format(name,age),end=' ')
    for lang in language:
        print(lang,end=' ')
    print() #줄바꿈
profile('유재석',20,'Python','Java','C','C++','C#','JavaScript')
profile('김태호',25,'Kotlin','Swift')
#------------------------------------------------------------------------------------
#지역변수(함수 내에서만 사용)와 전역변수(프로그램 내에서 사용)
gun=10
def checkpoint(soldiers): #경계근무
    global gun #전역공간에 있는 gun 사용
    gun=gun-soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))

def checkpoint_ret(gun,soldiers):
    gun=gun-soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun

print('전체 총 : {0}'.format(gun))
#checkpoint(2) #2명이나감
gun=checkpoint_ret(gun,2)
print('남은 총 : {0}'.format(gun))
#-----------------------------------------------------------------------------
#함수 퀴즈
#표준 체중을 구하는 프로그램
#표준체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식) 
#남자 : 키 x 키 x 22
#여자 : 키 x 키 x 21
#조건 1 : 표준 체중은 별도의 함수 내에서 계산
#           * 함수명 : std_weight
#           * 전달값 : 키(height),성별(gender)
#조건 2 : 표준 체중은 소수점 둘째 자리까지 표시
#출력 예제
#키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height,gender): #키는 m단위
    if gender=='남자':
        return height*height*22
    else:
        return height*height*21
height=175 #cm단위
gender='남자'
weight=round(std_weight(height/100,gender),2) #round를 이용해 소수점 두자리까지 표시
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height,gender,weight))
#----------------------------------------------------------------------------
#표준 입출력
print('Python','Java','JavaScript',sep=',',end='?') #end=문장의 끝을 ?로 바꾸면서 줄바꿈을 없앰
print('무엇이 더 재밌을까요')

import sys
print('Python','Java',file=sys.stdout) #표준출력
print('Python','Java',file=sys.stderr) #표준에러

scores={'수학':0,'영어':50,'코딩':100}
for subject,score in scores.items(): 
    print(subject.ljust(8),str(score).rjust(4),sep=':') #ljust(8)=총 8칸의 공간을 확보한 뒤 왼쪽으로 정렬 left, rjust(4)=총 4칸의 공간을 확보한 뒤 오른쪽으로 정렬 right

for num in range(1,21):
    print('대기번호 : '+str(num).zfill(3)) #zfill(3)=3칸을 확보하고 빈공간을 0으로채워라

answer=input('아무 값이나 입력 : ')
print('입력하신 값은 '+answer+'입니다')