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