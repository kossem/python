from socket import *
import threading
turn = False
pr = threading.Lock()
def on(turn):
    if(turn == True): 
    	return "already turned"
    return "turn on the Svetofor"
 
def off(turn):
    if(turn == False): 
    	return "already turned off the Svetofor"
    return "turn off the Svetofor"

def svet(port): 
    global turn
    global color
    global pr
    color = "green"
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('', port))
    while True:
        data, addr = sock.recvfrom(1024)
        pr.acquire()
        try:

            if data == "check status":
            	if (turn == True):
            		sock.sendto(color, addr)
            	else:
            		sock.sendto("Svetofor off", addr)
            elif data == "on":
                sock.sendto(on(turn), addr)
                turn = True
            elif data == "off":
                sock.sendto(off(turn), addr)
                turn = False
            elif data == "set color red":
            	if(turn == True):
                	sock.sendto("New color - red", addr)
                	color = "red" 
                else:
                	sock.sendto("Svetofor off", addr)
            elif data == "set color green":
            	if(turn == True):
                	sock.sendto("New color - green", addr)
                	color = "green" 
                else:
                	sock.sendto("Svetofor off", addr)
            elif data == "set color yellow":
            	if(turn == True):
                	sock.sendto("New color - yellow", addr)
                	color = "yellow" 
                else:
                	sock.sendto("Svetofor off", addr)                	
            else: sock.sendto("request error", addr)
            
        finally:
            pr.release()
 
a = threading.Thread(target=svet, args=(1450,))
b = threading.Thread(target=svet, args=(6060,))
c = threading.Thread(target=svet, args=(8080,))
a.start()
b.start()
c.start()
