import pyautogui as m

#모듈을 추가해주고 이것을 m이라고 부르겠다.

try:
	while True:
		x, y = m.position()
		# 마우스의 x 좌표와 y 좌표를  구한다.
	
		print('x : {}. y : {} '.format(x, y))
		# 그리고 마우스의  좌표를 출력한다.
except KeyboardInterrupt:
	print('Ctrl + C를 눌러서 프로그램 종료그램을 종료합니다.')


