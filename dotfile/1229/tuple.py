#튜플은 리스트와 다르게 불변
# 그래서 추가 삭제 수정 불가능
OS= ['우분투','우분투 민트','칼리리눅스','아치리눅스']
OS[0]= ['데비안OS']
OS[1]= ['레드헷OS']
print(OS)       #변경이 가능하지만 튜플은 불가능
#튜플은 만들기 위해 각 요소 뒤에(.)를 붙인다.
#하나일 경우는 반드시 불여주며,여러 개일 경우,
#마지막 요소의(,)는 생략 가능하다.
Class=()    
Class=('데이터베이스','컴퓨터개론','데이터베이스','C언어') #튜플은 소괄호
print(Class)
#Class[0]='JAVA' Compile Error


