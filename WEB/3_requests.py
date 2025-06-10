import requests
res=requests.get('http://google.com') #원하는 페이지 접속
#res=requests.get('http://nadocoding.tistory.com')
res.raise_for_status() #정보를 받아왔는지 확인

# print('응답코드 :',res.status_code)#200이면 정상 403이면 접근권한X

# if res.status_code == requests.codes.ok:
    # print('정상')
# else:
    # print('문제가 생겼습니다.[에러코드:',res.status_code,']')

print(len(res.text))
print(res.text)
with open('mygoogle.html','w',encoding='utf8') as f:
    f.write(res.text) # 받아온 정보를 파일로 생성