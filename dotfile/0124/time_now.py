import subprocess
#리눅스 명령어 사용하기 위해 ,,...
from time import sleep

while True:
	result = subprocess.check_output("date | awk '{print $5}'", shell=True)
	result = str(result)
	
	#print(result[2:10], end='\r')

	result = result[2:10]

	a = result.split(':')[0]
	b = result.split(':')[1]
	c = result.split(':')[2]

	#17:34:50
	#split(':')는 ''사이에 있는 문자로 나누고 그것을 리스트로 저장
	# 0 -> 17
	# 1 -> 34
	# 2 -> 50
	
	print(a,b,c)

	print(result, end='\r')
	sleep(1)

