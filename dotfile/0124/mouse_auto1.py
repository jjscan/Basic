import pyautogui as m
import random

#9,142 49,187 범위 내에 크롬이 있다.

chrome_button = {
	'top_left' : { 'x' : 9, 'y' : 142},
	'bottom_right' : {'x' : 49, 'y' : 187}
}

x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])
# random.uniform(a,b)는 a와b사이 수 중에 랜덤한 값을 반환한다.

m.moveTo(x, y, duration = 2)
# 마우스의 위치를 x, y의 위치로 1초동안 이동한다.

