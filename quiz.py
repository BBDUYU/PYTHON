#퀴즈
#댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게된다
#추첨 프로그램을 작성하시오

#조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
#조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#조건3 : random 모듈의 shuffle과 sample 활용

#출력예제
# -- 당첨자 발표 --
#치킨 당첨자 : 1
#커피 당첨자 : [2,3,4]
# -- 축하합니다 --

from random import *
users=range(1,21) #1부터 20까지 생성
print(type(users)) #type = range
users=list(users) #type을 list로 변경
print(users)
shuffle(users)
print(users)

winners=sample(users,4) #4명 중 1명은 치킨, 3명은 커피
print('-- 당첨자 발표 --')
print('치킨 당첨자 : {}'.format(winners[0]))
print('커피 당첨자 : {}'.format(winners[1:]))
print('-- 축하합니다 --')

#--------------------------------------------------------------------
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
#--------------------------------------------------------------------
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
#--------------------------------------------------------------------
#퀴즈
#회사에서 매주 1회 작성해야 하는 보고서가 있다
#보고서는 항상 아래와 같은 형태로 출력되어야 한다

#- X 주차 주간 보고 -
#부서 : 
#이름 :
#업무 요약 :

#1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같다
# for i in range(1,51):
    # with open(str(i)+'주차.txt','w',encoding='utf-8') as report_file:
        # report_file.write('- {0} 주차 주간 보고 -'.format(i))
        # report_file.write('\n부서 :')     
        # report_file.write('\n이름 :')
        # report_file.write('\n업무 요약 : ')
#--------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------
#예외처리 퀴즈
# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있다
# 대기 손님의 치킨요리 시간을 줄이고자 자동 주문 시스템을 제작하였다
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오
# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
#   출력 메시지 : 잘못된 값을 입력하였습니다
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#   치킨 소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#   출력 메시지 : 재고가 소진되어 더 이상 주문을 받지 않겠습니다
# [코드]
class SoldOutError(Exception):
    pass

chicken=10
waiting=1 #홀 안은 만석 대기번호 1부터 시작
while(True):
    try:
        print('[남은 치킨 : {0}]'.format(chicken))
        order=int(input('치킨 몇 마리 주문하시겠습니까>'))
        if order>chicken: #남은 치킨보다 주문량이 많을 때
            print('재료가 부족합니다')
        elif order<=0:
            raise ValueError
        else:
            print('[대기번호 {0}] {1}마리 주문이 완료되었습니다'.format(waiting,order))
            waiting +=1
            chicken -=order
        if chicken==0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력하였습니다')
    except SoldOutError:
        print('재고가 소진되어 더 이상 주문을 받지 않겠습니다')
        break
#------------------------------------------------------------------
#퀴즈
#프로젝트 내에 나만의 시그니처를 남기는 모듈
# 조건 : 모듈 파일명은 byme.py로 작성
# 모듈 사용 예제
import byme
byme.sign()

# 출력 예제
# 이 프로그램은 나도코딩에 의해 만들어졌습니다
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@gmail.com
