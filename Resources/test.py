import OSC
import time, threading

receive_address = '127.0.0.1', 12001


def printing_handler(addr, tags, stuff, source):
    print "---"
    arg1 = stuff[0]
    arg2 = stuff[1]
    arg3 = stuff[2]
    print "received",arg1,arg2,arg3
    print "---"

s = OSC.OSCServer(receive_address) 
s.addMsgHandler("/numero", printing_handler) 

st = threading.Thread( target = s.serve_forever )
st.start()