import pyautogui as m
import random

#9,142 49,187 범위 내에 크롬이 있다.

def rand(chrome_button):
	x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
	y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])
	# random.uniform(a,b)는 a와b사이 수 중에 랜덤한 값을 반환한다.

	return x,y

def main():
	chrome_button = {
		'top_left' : { 'x' : 9, 'y' : 142},
		'bottom_right' : {'x' : 49, 'y' : 187}
	}

	x,y =rand(chrome_button)
	#rand()ㅎ마수에 chrome의 사각형 좌표를 넣고 이 중에서 x와 y를 반환 받는다.
	m.moveTo(x, y, duration = 2)
	# 마우스의 위치를 x, y의 위치로 1초동안 이동한다.

if __name__ == '__main__':
	main()
