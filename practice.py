# 숫자형
print(5) 
print(-10)
print(3.14)
print(3+5) 
print(2*8)
print(3*(3+1))
# 문자형
print('풍선')
print("나비")
print("ㅋ"*9)

# boolean
print(5>10)
print(2<3)
print(True)
print(False)
print(not True)
print(not(5>10))

# 변수
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult=age>=3

print('우리집 '+animal+'의 이름은 '+name)
print(name+'는'+str(age)+'살이고'+hobby+'를 아주 좋아한다')
print(name+'는 어른일까 '+str(is_adult))


station='사당'
print(station+'행 열차가 들어오고 있습니다')

#연산자
print(1+1)
print(3-2)
print(5*2)

print(2**3) #2^3
print(5%3) #나머지
print(10%3) #1
print(5//3)# 몫
print(10//3)#3
print(10>3)#t
print(4>=7)#f
print(3==3)#t
print(4==2)#f

print(1 !=3) #t
print(not (1!=3)) #F
print((3>0)and(3<5))#t
print((3>0)&(3<5))#t

print((3>0)or(3>5)) #t
print((3>0)|(3>5))#t

#수식
print(2+3*4) #14
print((2+3)*4) #20
number=2+3*4
print(number) #14 
number=number+2
print(number) #16
number+=2
print(number)#18
number*=2
print(number) #36
number/=2
print(number) #18
number-=2
print(number) #16

#숫자 처리 함수
print(abs(-5)) #절대값 
print(pow(4,2)) #4^2
print(max(5,12)) #최대값
print(min(5,12)) #최소값
print(round(3.14)) #반올림
print(round(4.99))

from math import *
print(floor(4.99)) #소수점 내림
print(ceil(3.14)) #소수점 올림
print(sqrt(16)) #제곱근

#랜덤함수
from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만
print(int(random()*10)) # 소수점 제외
print(int(random()*10)+1) #1 ~ 10 미만

print(int(random()*45)+1) #1 ~ 45

print(randrange(1,46)) #1~46미만의 임의의 값 생성

print(randint(1,45))# 1~45이하 

date=randint(4,28)
print('오프라인 스터디 모임 날짜는 매월'+str(date)+'일로 선정되었습니다')

#문자열
sentence='나는 소년입니다'
print(sentence)
sentence2="파이썬"
print(sentence2)
sentence3="""
나는 소년이고,
파이썬
"""
print(sentence3)

#슬라이싱 
jumin='990120-1234567'

print('성별 : '+jumin[7])
print('연 : '+jumin[0:2]) #0~2 직전까지 (0,1)
print('월 : '+jumin[2:4])
print('일 : '+jumin[4:6])

print('생년월일 : '+jumin[:6]) #처음부터 6직전까지
print('뒤 7자리 : '+jumin[7:]) #7부터 끝까지

print('뒤 7자리 (뒤부터): '+jumin[-7:])

#문자열 처리
python='Python is Amazing'
print(python.lower()) #모든문자 소문자
print(python.upper()) #모든문자 대문자

print(python[0].isupper()) #0번째 문자가 대문자인지 맞으면 true
print(len(python)) #글자길이 len()

print(python.replace('Python','Java')) #글자 교체 replace()

index=python.index('n') #글자위치 조회
print(index)

index=python.index('n',index+1) #첫 조회 다음위치 
print(index) 

print(python.find('Java')) # find() : 찾으려는 값이 없을시 -1
print(python.index('Java')) # index() : 찾으려는 값이 없을시 오류

print(python.count('n')) # 찾으려는 단어 갯수

#-------------------------------------------------------------------------------------

#문자열 포맷
print('a'+'b')

    #방법 1
print('나는 %d살입니다' %20) # %d 정수값
print('나는 %s를 좋아합니다' %'파이썬') # %s 문자열
print('Apple 은 %c로 시작합니다' %'A') # %c 한글자

print('나는 %s색과 %s색을 좋아합니다'%('파란','빨간')) # 여러 값 출력 %(' ', ' ')

    #방법 2
print('나는 {}살입니다'.format(20)) #괄호속 값을 {}안에 대입
print('나는 {}색과 {}색을 좋아합니다'.format('파란',"빨간"))

print('나는 {0}색과 {1}색을 좋아합니다'.format('파란',"빨간"))
print('나는 {1}색과 {0}색을 좋아합니다'.format('파란',"빨간")) # 출력 순서 정하기

    #방법 3 
print('나는 {age}살이며,{color}색을 좋아합니다'.format(age=20,color='빨간')) #변수 설정

    #방법 4 (python v3.6이상)
age=20
color='빨간'
print(f'나는 {age}살이며, {color}색을 좋아합니다')

#------------------------------------------------------------------------------

#탈출문자
print('백문이 불여일견 \n백견이 불여일타') #\n 줄바꿈

    #저는 "나도코딩" 입니다 - 출력값
print('저는 "나도코딩" 입니다') 
# \" , \'  : 문장내에서 큰따옴표 작은따옴표 출력 
print("저는 \"나도코딩\"입니다.") 

# \\ : 문장 내에서 \
print('C:\\User\\Nadocoding\\Desktop')

# \r : 커서를 맨앞으로 이동
print('Red Apple\rPine')

# \b : 백스페이스
print('Redd\bApple')

# \t : 탭
print('Red\tApple')

#quiz ) 사이트별로 비밀번호를 만들어주는 프로그램
#ex) http://naver.com
#규칙1 : http:// 부분 제외
#규칙2 : 처음 만나는 점 이후 부분은 제외
#규칙3 : 남은 글자중 처음세자리 + 글자갯수 + 글자 내 'e'갯수 + '!' 로 구성

url='http://naver.com'
my_str=url.replace("http://","") #규칙1
my_str=my_str[:my_str.index(".")] #규칙2
pwd=my_str[:3]+str(len(my_str))+str(my_str.count('e'))+"!" #규칙3
print(pwd)

#---------------------------------------------------------------------------------

#리스트 []
subway1=10
subway2=20
subway3=30

subway=[10,20,30]

subway=['유재석','조세호','박명수']

#조세호는 몇번째 칸에 타고 있는가
print(subway.index('조세호'))

#하하가 다음정류장에서 탐
subway.append('하하')
print(subway)

#정형돈이 유재석과 조세호 사이에 탐
subway.insert(1,'정형돈')
print(subway)

#지하철에 있는 사람들을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명 있는지 확인
subway.append('유재석')
print(subway.count('유재석'))

#정렬
num_list=[5,2,4,3,1]
num_list.sort()
print(num_list)

#내림차순 정렬
num_list.reverse()
print(num_list)

#삭제
num_list.clear()
print(num_list)

#다양한 자료형
mix_list=['조세호',20,True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)

#---------------------------------------------------
#사전

cabinet={3:'유재석',100:'김태호'}
print(cabinet[3])

print(cabinet.get(3))

print(cabinet.get(5))
print('hi')