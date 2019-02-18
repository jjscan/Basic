from time import sleep as s
# time모듈에서 sleep만 가져와서 s로 정의한다.

def countdown(t):
	while t:	#0초가 아니면
		mins = t // 60	#현재 초 나누기 60 = 분
		secs = t % 60	#초

		#print('Now = %02d:%02d' %(mins,secs), end='\r')
		print('Now = {:02d}:{:02d}'.format(mins,secs), end='\r')
		s(1)
	
		t -= 1
	
	return
	
time = int(input('Count time input >>>'))
#time = 2
countdown(time)
print('timeout!!!')
