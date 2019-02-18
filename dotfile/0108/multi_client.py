import socket
import threading
 
HOST = '172.16.100.98'
PORT = 7942
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def recvChat():
   while True:
      try:
         data = s.recv(1024)
         if not data:
            break
         print(data.decode('utf-8'))
      except:
         pass
 
def sendChat():
   while True:
      data = input()
      data = data.encode('utf-8')
      s.send(data)

      if data == '/logout':
         break

   s.close()
             
threading._start_new_thread(sendChat, ())
threading._start_new_thread(recvChat, ())

while True:
	pass

