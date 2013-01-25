# -*- coding: cp936 -*-
import struct,os,sys,urllib,re

httpad = 'http://10.48.179.107/'
localdir = 'c:\\zabbix\\'
if os.path.exists(localdir):
    print localdir + "exists"
else:
    print localdir + " didn't exists,now create"
    os.mkdir(localdir)

#文件列表
files = {'zabbix_agentd.exe','zabbix_get.exe','zabbix_sender.exe','zabbix_agentd.conf'}

#获取平台位数
if struct.calcsize("P")*8 == '64' :
    print '64bit system'
    urls = 'za_64bit/'
else:
    print '32bit system'
    urls = 'za_32bit/'

#下载平台对应的文件
for i in files:
    url = httpad + urls + i
    localfile = localdir + i
    print url
    print localfile
    urllib.urlretrieve(url,localfile)


#获取IP
ips = os.popen('ipconfig | findstr "IP Address" |findstr "10.48"').read()
#配置hostname
hostname = 'GAME_'+ips.split(':')[1].split('.')[3]

#修改配置文件
f = open(localdir+'zabbix_agentd.conf','r+')
host = f.read()
host = host.replace('HOSTNAME_REAL',hostname)
f.seek(0)
f.write(host)
f.close()
#修改了hostname



#安装服务
os.popen('C:\\zabbix\\zabbix_agentd.exe -c C:\\zabbix\\zabbix_agentd.conf -i')

os.popen('net start "Zabbix Agent"') 
sys.exit("zabbix install success !") 

