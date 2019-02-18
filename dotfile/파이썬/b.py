import win32api,win32con
def mouse_dis(count,count1):
	cont1.message_dis(str(count))	
	while count==0:
		mouse_p=win32api.GetCursorPos()
		cont2.mouse_po(mouse_p[0],mouse_p[1])
		sleep(0.1)

if m_data[i][0]=="m_position":
			cont1.message_dis("마우스 이동 :"+ m_data[i][1]+m_data[i][2])
			m_x=int(m_data[i][1])
			m_y=int(m_data[i][2])
			win32api.SetCursorPos((m_x,m_y))



