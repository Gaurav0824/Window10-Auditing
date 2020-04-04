# %%
import subprocess
import re
#import win32com.shell.shell as shell
import time


'''b=['ALIAS  ',
 'BASEBOARD  ',
 'BIOS  ',
 'BOOTCONFIG  ',
 'CDROM  ',
 'COMPUTERSYSTEM  ',
 'CPU  ',
 'CSPRODUCT  ',
 'DCOMAPP  ',
 'DESKTOP  ',
 'DESKTOPMONITOR  ',
 'DEVICEMEMORYADDRESS  ',
 'DISKDRIVE  ',
 'DISKQUOTA  ',
 'DMACHANNEL  ',
 'ENVIRONMENT  ',
 'GROUP  ',
 'IDECONTROLLER  ',
 'IRQ  ',
 'JOB  ',
 'LOADORDER  ',
 'LOGICALDISK  ',
 'LOGON  ',
 'MEMCACHE  ',
 'MEMORYCHIP  ',
 'MEMPHYSICAL  ',
 'NETCLIENT  ',
 'NETLOGIN  ',
 'NETPROTOCOL  ',
 'NETUSE  ',
 'NIC  ',
 'NICCONFIG  ',
 'NTDOMAIN  ',
 'NTEVENTLOG  ',
 'ONBOARDDEVICE  ',
 'OS  ',
 'PAGEFILE  ',
 'PAGEFILESET  ',
 'PARTITION  ',
 'PORT  ',
 'PORTCONNECTOR  ',
 'PRINTER  ',
 'PRINTERCONFIG  ',
 'PRINTJOB  ',
 'PROCESS  ',
 'QFE  ',
 'RDNIC  ',
 'RDPERMISSIONS  ',
 'RDTOGGLE  ',
 'RECOVEROS  ',
 'REGISTRY  ',
 'SCSICONTROLLER  ',
 'SERVER  ',
 'SERVICE  ',
 'SHARE  ',
 'SOUNDDEV  ',
 'STARTUP  ',
 'SYSACCOUNT  ',
 'SYSDRIVER  ',
 'SYSTEMENCLOSURE  ',
 'SYSTEMSLOT  ',
 'TIMEZONE  ',
 'USERACCOUNT  ',
 'VOLUME  ']'''
def wmic(policy):
        
        command='wmic '+policy+' LIST brief'
        #if opt==2:
         #   command='wmic service get DesktopInteract,ErrorControl,Name,ServiceType,StartMode'
       # if opt==5:
        #    command=' wmic service get name, processid, startmode, state, status, exitcode,servicetype /format: table'
        try:    
            a=eval("subprocess.getoutput(command)")
            print(a)    
        except:
            print("Error \n Cannot proceed")
        input()

#re.findall('[A-Z]+ ',a)

#re.findall('[A-Z]+ \s',a)
i=int()
a=[]
while True:
    '''for i in range(len(c)):
        print('{:<2} :{}'.format(i+1 ,c[i]))
    i=(input("Enter Option number"))
    if i=='':
        break
    elif i.isdigit()==True:
        wmic(int(i))
    else: 
        print("Invalid Value\n\nProgram will close in next 3 seconds")
        time.sleep(3)
        break'''
    with open(r'C:\Users\Gaurav\Winpol.txt') as file:
        i=1
        for line in file:
            line1=re.search(r"[A-Z]+\s+-.+",line).group()
            print("{:<3}:{}".format(i,line1))
            i+=1
            b=re.findall('[A-Z]+ \s',line)
            #print(b)
            a.extend(b)
    #print(a)
    i=(input("Enter Option number"))
    if i=='':
        break
    elif i.isdigit()==True:
        wmic((a[int(i)]))
    else: 
        print("Invalid Value\n\nProgram will close in next 3 seconds")
        time.sleep(3)
        break
#re.findall('[A-Z]+ .*-',a)


# %%


