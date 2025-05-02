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
#---------------------------------------------------------------------------------
#다양한 출력 포맷
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print('{0:>10}'.format(500))
#양수일때 +표시 음수일때 -표시
print('{0:>+10}'.format(500))
print('{0:>+10}'.format(-500))
#왼쪽 정렬, 빈칸을 _로 채움
print('{0:_<10}'.format(500))
#3자리마다 ,
print('{0:,}'.format(1000000000000))
#3자리마다 ,를 찍고 + - 부호 표시
print('{0:+,}'.format(1000000000000))
print('{0:+,}'.format(-1000000000000))
#3자리마다 ,를 찍고 + - 부호 표시, 자릿수 확보, 빈자리 ^로 채우기
print('{0:^<+30,}'.format(1000000000000000)) #빈칸, 정렬, 부호, 자릿수확보,3자리마다 콤마
#소수점 출력
print('{0:f}'.format(5/3))
#소수점 특정 자리수까지만 표시 (소수점 3자리에서 반올림)
print('{0:.2f}'.format(5/3))
#---------------------------------------------------------------------------------
#파일 입출력
# score_file=open('score.txt','w',encoding='utf-8') #파일이름 작성 한글정보
# print('수학 : 0',file=score_file)
# print('영어 : 50',file=score_file)
# score_file.close()

#   파일 수정
# score_file=open('score.txt','a',encoding='utf-8') #a = append 덮어쓰기
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100') #write는 줄바꿈이 없음
# score_file.close()

#   읽는 방법 1
#score_file=open('score.txt','r',encoding='utf-8') #파일 읽기
#print(score_file.read())
#score_file.close

#   읽는 방법 2
# score_file=open('score.txt','r',encoding='utf-8')
# print(score_file.readline()) #줄 별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#   읽는 방법 3
# score_file=open('score.txt','r',encoding='utf-8')
# while True: #무한루프
#     line=score_file.readline() #score_file에서 한줄씩 불러온다
#     if not line: #line이 없으면
#         break #멈춰라
#     print(line) #line이 있으면 print
# score_file.close()

#   읽는 방법 4
score_file=open('score.txt','r',encoding='utf-8')
lines=score_file.readlines() #모든 라인을 list형태로 저장
for line in lines:  #line 변수를 지정해 lines의 내용을 하나씩 표시
    print(line,end="")
score_file.close()

#---------------------------------------------------------------------------
#pickle
#데이터를 pickle을 이용해 파일에 저장후 파일에 저장된 내용을 load를 이용해 불러와 변수에 저장해 사용
import pickle
# profile_file=open('profile.pickle','wb') b = 바이너리 pickle은 작업방식에 b
# profile={'이름' : '박명수','나이':30,'취미': ['축구','골프','코딩']}
# print(profile)
# pickle.dump(profile,profile_file) #profile에 있는 정보를 profile_file에 저장
# profile_file.close()

#profile_pickle에서 데이터를 불러오기
profile_file=open('profile.pickle','rb')
profile=pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
#---------------------------------------------------------------------------
#with
import pickle
with open('profile.pickle','rb') as profile_file: #profile.pickle파일을 열고 profile_file 변수에 파일정보를 저장
    print(pickle.load(profile_file))
    #with문을 탈출하며 open했던 파일을 자동으로 close

# with open('study.txt','w',encoding='utf-8') as study_file:
#     study_file.write('파이썬')

with open('study.txt','r',encoding='utf-8') as study_file:
    print(study_file.read())
#-----------------------------------------------------------------------
#퀴즈
#회사에서 매주 1회 작성해야 하는 보고서가 있다
#보고서는 항상 아래와 같은 형태로 출력되어야 한다

#- X 주차 주간 보고 -
#부서 : 
#이름 :
#업무 요약 :

#1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같다
for i in range(1,51):
    with open(str(i)+'주차.txt','w',encoding='utf-8') as report_file:
        report_file.write('- {0} 주차 주간 보고 -'.format(i))
        report_file.write('\n부서 :')     
        report_file.write('\n이름 :')
        report_file.write('\n업무 요약 : ')
#---------------------------------------------------------------------
