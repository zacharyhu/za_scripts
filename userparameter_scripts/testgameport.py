#    @zacharyhu 
#   2013.01.22


import socket,sys,re


HOST = sys.argv[1]
PORT = sys.argv[2]
s = None
#print HOST + ' -- PORT :' + PORT
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    #print 'could not open socket'
    #sys.exit(1)
    online = '-1'
#s.sendall('Hello, world')
else:
    data = s.recv(1024)
    s.close()
    #get online data such as online="119/216"
    p = re.compile('online=\"[0-9]{1,3}/[0-9]{1,3}\"')
    p_num = re.compile('[0-9]{1,3}')
    online = p_num.findall(p.findall(data)[0])[0]

#print 'Received', repr(data)
print online
