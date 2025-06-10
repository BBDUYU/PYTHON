import re
p=re.compile('ca.e') 
# . : 하나의 문자       ex) ca.e > care, cafe, case (o), caffe (x)
# ^ : 문자열의 시작     ex) ^de  > desk, destination (o), fade(x)
# $ : 문자열의 끝       ex) se$  > case, base (o), face(x)

def print_match(m):
    #print(m.group()) # 매치되지 않으면 에러발생
    if m:
        print(m.group())
    else:
        print('매칭되지 않음')

m=p.match('careeeeee') # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
