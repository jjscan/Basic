import pyautogui
import sys

pyautogui.PAUSE = 0.8
pyautogui.click(24, 1065, duration=0.25)  # 시작 버튼

pyautogui.typewrite('gedit')  # 메모장을 검색한다
pyautogui.press('enter')

# 메모장에 타자 치기
time.sleep(7)
pyautogui.typewrite('Hello World !')  # Hellow World! 를 적는다
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('hanguel')  # 한/영 키보드를 누른다
pyautogui.typewrite('안녕 세상아 !')  # 안녕 세상아를 적는다
pyautogui.press('enter')

pyautogui.typewrite('안녕 세상아 !')   # 단, 한국어는 인식 안됨
