# -*- coding: cp936 -*-
import struct,os,sys,urllib,re

httpad = 'http://10.48.179.107/'
localdir = 'c:\\zabbix\\'
if os.path.exists(localdir):
    print localdir + "exists"
else:
    print localdir + " didn't exists,now create"
    os.mkdir(localdir)

#�ļ��б�
files = {'zabbix_agentd.exe','zabbix_get.exe','zabbix_sender.exe','zabbix_agentd.conf'}

#��ȡƽ̨λ��
if struct.calcsize("P")*8 == '64' :
    print '64bit system'
    urls = 'za_64bit/'
else:
    print '32bit system'
    urls = 'za_32bit/'

#����ƽ̨��Ӧ���ļ�
for i in files:
    url = httpad + urls + i
    localfile = localdir + i
    print url
    print localfile
    urllib.urlretrieve(url,localfile)


#��ȡIP
ips = os.popen('ipconfig | findstr "IP Address" |findstr "10.48"').read()
#����hostname
hostname = 'GAME_'+ips.split(':')[1].split('.')[3]

#�޸������ļ�
f = open(localdir+'zabbix_agentd.conf','r+')
host = f.read()
host = host.replace('HOSTNAME_REAL',hostname)
f.seek(0)
f.write(host)
f.close()
#�޸���hostname



#��װ����
os.popen('C:\\zabbix\\zabbix_agentd.exe -c C:\\zabbix\\zabbix_agentd.conf -i')

os.popen('net start "Zabbix Agent"') 
sys.exit("zabbix install success !") 

