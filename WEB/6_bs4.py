import requests
from bs4 import BeautifulSoup

url='https://comic.naver.com/index'
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') 
# print(soup.title)
# print(soup.title.get_text())
# print(soup.div) # soup 객체에서 처음발견되는 div element 출력
# print(soup.div.attrs) # div element의 속성정보를 출력
# print(soup.div['id']) # div element의 속성 값 정보를 출력

#class=GlobalNavigationBar__link--WMOzG 인 a를 찾아라
print(soup.find('a',attrs={'class':'GlobalNavigationBar__link--WMOzG'})) #셀레니움 변경으로 None : 
#class=GlobalNavigationBar__link--WMOzG인걸 찾아라
print(soup.find(attrs={'class':'GlobalNavigationBar__link--WMOzG'})) #셀레니움 변경으로 None

# 예상 결과
# <a class="GlobalNavigationBar__link--WMOzG" aria-current="true" href="/index">홈</a>

rank1=soup.find('a',attrs={'class':'ContentAuthor__author--CTAAP'})
print(rank1.a.get_text())
# next_sibling : 다음 element로 넘어감
# previous_sibling : 이전 element로 돌아감