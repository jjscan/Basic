import pyautogui as m
import random
import time

#9,142 49,187 범위 내에 크롬이 있다.

def rand(chrome_button):
	x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
	y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])
	# random.uniform(a,b)는 a와b사이 수 중에 랜덤한 값을 반환한다.

	return x,y

def click():
	time.sleep(5)
	m.click()
	#파라미터가 없으면 현재 마우스좌표를 클릭
	print('chrome을 클릭하였습니다.')
	
	time.sleep(10)
	m.typewrite('naver.com', interval=0.15)
	#0.15초마다 타이핑
	print('주소에 "naver.com"을 입력하였습니다.')
	
	time.sleep(5)
	m.press('enter')
	# press는 특정 키를 입력할 때
	print('enter를 눌렀을 때')

	return

def login():
	time.sleep(20)
	button = m.locateOnScreen('btn.png')
	# 버튼의 좌표는 왼쪽 위(x,y), 오른쪽 아래(x,y)의 사각형 형태
	#이 좌표의 중심 좌표를 구하고 클릭!!

	center = m.center(button)
	#button은 사각형 좌표고 사각형 중심좌표를 center변수에 저장
	print('button_center : ', center)
	
	m.click(center) #중심좌표 입력
	print('Login 버튼을 클릭하였습니다.')
	

def main():
	chrome_button = {
		'top_left' : { 'x' : 20, 'y' : 55},
		'bottom_right' : {'x' : 30, 'y' : 70}
	}

	x,y =rand(chrome_button)
	#rand()ㅎ마수에 chrome의 사각형 좌표를 넣고 이 중에서 x와 y를 반환 받는다.
	m.moveTo(x, y, duration = 2)
	# 마우스의 위치를 x, y의 위치로 1초동안 이동한다.
	click()
	login()

if __name__ == '__main__':
	main()