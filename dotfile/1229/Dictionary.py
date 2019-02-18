#{key1: val1, ...} 키와 값의 쌍으로 이루어짐
dict = {'kor':'80','eng':'77','mat':'90',}
print(dict)
print(dict['eng'])      #eng 항목만  출력
dict['tot']=247         #tot 항목 축가
print(dict) 
dict2={'kor2':88,'eng2':99,'mat':82}
dict.update(dict2)  #dict와 dict2결합
print(dict)
print(dict2)
del dict['mat']     #dict에서 'mat항목 삭제
print(dict)
dict2.clear()       #dict2 모든 항목 삭제
print(dict2)
dict.keys()
print(dict2)
