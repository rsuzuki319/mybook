#!/usr/bin/env python
import sys
import csv
#import mojimoji
import time
import datetime
from datetime import timedelta
import random
from datetime import date
import urllib.request
import json
import pprint
from datetime import datetime
import pytz

def read_econfig():
    configfnm='econfig.txt'
        
    with open(configfnm,'r') as ff:
        wconfig=ff.read(100)
    print (wconfig)
    confs=wconfig.split(';')
    return confs

def set_config(filenm,data) :
    cont=''
    for i in range(len(data)):
        if (i==0):
            cont=str(data[i])
        else:
            cont=cont+","+str(data[i])  
    with open(filenm,'w') as entry:
        entry.write(cont)
    r=cont
    
    return r
def update_config(yobi,qnum):
    newconf=[]
    configfnm='mdayconfig.txt'
    if (yobi=='1'):
        configfnm='mdayconfig.txt'
    elif (yobi=='2'):
        configfnm='tdayconfig.txt'
    else:
        print ("NO actionyobi, then monday")
        configfnm='mdayconfig.txt'        
    with open(configfnm,'r') as ff:
        wconfig=ff.read(100)
        print (wconfig)
        confs=wconfig.split(',')
        newconf.append(confs[0])
        newconf.append(confs[1])
        newconf.append(qnum)
        newconf.append(confs[3])
    set_config(configfnm,newconf)
    return






def get_nk225mini_quote_test(tkey,tdate,vii):
    #debug
    val=str(28000+vii)
    cprice=['2021-07-22',val,'08:45']
    return cprice

    fsymbol='166060019'    
    url = 'http://localhost:18080/kabusapi/board/'+fsymbol+'@2'    
    #url = 'http://localhost:18080/kabusapi/board/166030019@2'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)
    cprice=[]
    try:
        
        
        with urllib.request.urlopen(req) as res:
            #print(res.status, res.reason)
            for header in res.getheaders():
                #print(header)
                pass
            #print()
            content = json.loads(res.read())
            #pprint.pprint(content)
            print (content['CurrentPrice'])
            print (content["CurrentPriceTime"])
            fulltime=str(content["CurrentPriceTime"])
            ctime=fulltime[11:16]
            print (ctime)
            cprice=[tdate,content['CurrentPrice'],ctime]
            print (cprice)
            return cprice

       
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
#********************************************
#******************************************

def read_entry_quote2(yobi):
    r=[]
    if (yobi=='1'):
        filenm='mentryq.txt'
        filenmrev='mentryqr.txt'
    elif (yobi=='2'):
        filenm='tentryq.txt'
        filenmrev='tentryqr.txt'
    else:
        print ("NO yobi 1 or 2")
        filenm='mentryq.txt'
        filenmrev='mentryqr.txt'
    with open(filenm,'r') as entry:
        res=entry.read(200)
        wres=res
        if (res==''):
            pass
        else:
            r.append([wres])
    with open(filenmrev,'r') as entry2:
        wres2=entry2.read(200)
        
        if (wres2==''):
            pass
        else:
            r.append([wres2])
       
    return r

def get_entry_data3(actionyobi,one):
    #debug
    r=[actionyobi,27800]
    return
    acts=read_entry_quote2(actionyobi)
    myose=0
    if (one==1):
        wone=1
    else:
        wone=0
    if (acts):
        act=acts[wone][0].split(',')
        print ("entry-data ",act)
        if (len(act)>0):
            myose=float(act[0])
        else:
            myose=0
    
    return [actionyobi,myose]
def send_first_order5(yobi,direction,qnum,night):
    print ("debug send order after reverse",yobi,direction,qnum,night)
    return
    #*********************************
    fsymbol='166060019'
    with open('kabutoken.txt','r') as token:
        tkey=token.read(100)
    #12-20 sepcial qty 1
    exchange=23
    if (night=='1'):
        exchange=24
    else:
        exchange=23

        obj3 = { 'Password': 'xxxx',
        'Symbol': fsymbol,
        'Exchange': exchange,
        'TradeType': 1,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': direction, #Uri=1 kai=2
        'Qty': qnum,
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    json_data3 = json.dumps(obj3).encode('utf-8')
    print (json_data3)
    
    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data3, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
         
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)



def send_order4(yobi,direction,hold,qnum,night):
    #*****debug 03-01-2021*******************************
    print ("debug no send order ",yobi,direction,qnum,night)
    return   
    fsymbol='166060019'    
    #url = 'http://localhost:18080/kabusapi/board/'+fsymbol+'@2'   
    with open('kabutoken.txt','r') as token:
        tkey=token.read(100)
    corder=0
    #********************************************************************
    #allways use corder 2020-12-13
    #hanten='0'
    #always qnum=2
    
    if (night=='1'):
        exflag=24
    else:
        exflag=23
    
    if (yobi=='1' ):
        corder=0
    elif (yobi=='2'):
        corder=2
    
    #******************************************
    if (direction=='1'):
        hensai='2'
    elif (direction=='2'):
        hensai='1'
    if (hold):
        obj = { 'Password': 'xxxx',
        'Symbol': fsymbol,
        'Exchange': exflag,
        'TradeType': 2,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': hensai, #Uri=1 kai=2
        'Qty': qnum,
        'ClosePositions':arrhid,  #for Tuesday
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    else:     
        obj = { 'Password': 'xxxx',
        'Symbol': fsymbol,
        'Exchange': exflag,
        'TradeType': 2,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': hensai, #Uri=1 ksi=2
        'Qty': qnum,
        'ClosePositionOrder':corder,  #for Tuesday
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    json_data = json.dumps(obj).encode('utf-8')
    print (json_data)
    
    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
         
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

def auto2(begintime,endtime,actionyobi,direction,initq,qnum,jdate2,eki,loss,ekionly,night,sent,hold,rinitq):
    tdate=jdate2
    yobi=actionyobi
    breakflag=0
    print ("qnum?",qnum)
    
    sent='0'
   
    
    print ('actionyobi,direction,initq,qnum,jdate2,eki,loss,hold')
    print (actionyobi,direction,initq,qnum,jdate2,eki,loss,hold)
    with open('kabutoken.txt','r') as token:
        tkey=token.read(100)
    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jdate=dt_j.strftime('%Y%m%d')
    jdate2=dt_j.strftime('%Y-%m-%d')
    dt_j=datetime.now(timeZ_J)
    jtime=dt_j.strftime('%H:%M')
    ii=0
    #while ((jtime>='08:45' and jtime<='24:00' ) or (jtime>='00:00' and jtime<='05:15')):    
    while (ii<10):    
    


        if (jtime>='16:30' or (jtime>='00:00' and jtime<='05:30')):
            night='1'
        else:
            night='0'
       
        vii=ii*50
        cprice=get_nk225mini_quote_test(tkey,tdate,vii)
        
        #**********************************************
        quote=float(cprice[1])
        
        
        

        
        print ("price",quote)
        if (not quote):
            breakflag=3
            
            #continue to night session
            print ("NO quote because break session")

            
        elif (quote<=(initq-eki) and direction=='1'):
                yobi=actionyobi
                mbuy=quote
                meki=1
                msell=initq
                
                ekiv=initq-mbuy
                print ('ekidahi-1',jdate2,yobi,msell,quote,ekiv,'EKI-1')                
                #actions.append([tdate,yobi,qtime,msell,quote,ekiv,hanten,'EKI',direction])
                if (sent=='1'):
                    
                    
                    hold=''
                    eflag=send_order4(actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    confs=read_config2(actionyobi)
                    oldqnum=int(confs[2])
                    newqnum=oldqnum-qnum
                    update_config(actionyobi,newqnum)
                    qnum=newqnum               
                print ("action-ekidashi-1")                    
                breakflag=1
                break


        elif (quote>=(initq+loss)  and direction=='1' and ekionly=='NO'):
                yobi=actionyobi
                mbuy=quote
                msell=initq
                mlss=1
                lossv=initq-mbuy
                print ('losscut-1',jdate2,yobi,msell,quote,lossv,'LCUT')
                #actions.append([tdate,yobi,qtime,msell,quote,lossv,hanten,'LCUT',direction])
                print ("action loscut-1")
                #*******************NO LOSSCUT????***************************
                if (sent=='1'):
                    

                                           
                    hold=''
                    eflag=send_order4(actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    confs=read_config2(actionyobi)
                    oldqnum=int(confs[2])
                    newqnum=oldqnum-qnum
                    update_config(actionyobi,newqnum) 
                    qnum=newqnum                                     
                breakflag=1
                break              
  
                

        elif (quote>=(initq+eki)  and  direction=='2'):
                print ("limit quote ",mlimit,quote)
                msell=quote
                mbuy=initq
                meki=1
                ekiv=msell-initq
                print ('ekidahi-2',jdate2,mbuy,quote,ekiv,'EKI-2')                
                #actions.append([tdate,yobi,qtime,mbuy,quote,ekiv,hanten,'EKI',direction])
                if (sent=='1'):
                    
                    
                    hold=''
                    eflag=send_order4(actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    confs=read_config2(actionyobi)
                    oldqnum=int(confs[2])
                    newqnum=oldqnum-qnum
                    update_config(actionyobi,newqnum) 
                    qnum=newqnum                                       
                print ("action-ekidashi-2")               
                breakflag=1
                break
                #for reverse losscut and new order
        
                              
        elif (quote<=(initq-loss)  and  direction=='2'):
                
                msell=quote
                mbuy=initq
                mlss=1
                lossv=initq-msell
                print ('losscut-2',jdate2,mbuy,quote,lossv,'LCUT')                
                
                if (sent=='1'):
                    
                    
                    hold=''
                    eflag=send_order4(actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    confs=read_config2(actionyobi)
                    oldqnum=int(confs[2])
                    newqnum=oldqnum-qnum
                    update_config(actionyobi,newqnum)
                    qnum=newqnum                                      
                print ("action-losscut-2")
                breakflag=1
                break

        else:
                print ("NO losscut/ekidashi")
                

                
        
        timeZ_J=pytz.timezone('Asia/Tokyo')
        dt_j=datetime.now(timeZ_J)
        print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
            
        dt_j=datetime.now(timeZ_J)
        jtime=dt_j.strftime('%H:%M')
        ltime=time.strftime('%H:%M')
        print ('night?: ',night)
        time.sleep(10)                       
        ii+=1                           
    else:
        print ("end of session at 05:15 ",breakflag)
        if (breakflag==5):
            pass
        else:    
            breakflag=2
        #set lime


    return breakflag

def read_config2(yobi):
    configfnm='mdayconfig.txt'
    if (yobi=='1'):
        configfnm='mdayconfig.txt'
    elif (yobi=='2'):
        configfnm='tdayconfig.txt'
    else:
        print ("NO actionyobi, then monday")
        configfnm='mdayconfig.txt'        
    with open(configfnm,'r') as ff:
        wconfig=ff.read(100)
    print (wconfig)
    confs=wconfig.split(',')
    return confs



if __name__ == '__main__':
    econfig=read_econfig()
    ieki=float(econfig[0])
    iloss=float(econfig[1])
    aftereki=float(econfig[2])
    afterloss=float(econfig[3])
    revlimit=float(econfig[4])
    print ('eki,loss,aftereki,afterloss,revlimit')
    print (econfig)
    #**************************
    eki=ieki
    loss=iloss
    #****************************
    mlss=0
    mloss=0
    meki=0
    mlimit=0
    mend=0
    holds=[]
    hanten='0'
    this='QNUM'
    args = sys.argv
    ekionly='NO'
#****************************************************** 

    stractyobi=args[1]
    if (stractyobi[0:1]=='M' or stractyobi[0:1]=='1'):
        actionyobi='1'
    elif (stractyobi[0:1]=='T' or stractyobi[0:1]=='2'):
        actionyobi='2'
    else:
        go=input("ERROR NO MON TUE type control-C")
#******************************************************    
    
    qnum=int(args[2])

    
    this='QNUM'
#******************************************************




#********************************************************
    print ("actionyobi",actionyobi)

#************************************
    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jdate=dt_j.strftime('%Y%m%d')
    jdate2=dt_j.strftime('%Y-%m-%d')
    dt_j=datetime.now(timeZ_J)
    jtime=dt_j.strftime('%H:%M')
    yobi=dt_j.strftime('%w')

    



    hold=''
    hqty=0

#**************************************************************
    paras=read_config2(actionyobi)
    
    
    
    endyobi=actionyobi
    confqnum=int(paras[2])
    direction=paras[1]
    
    if (this=='QNUM' and qnum<=confqnum and qnum>0):
        print ("use specified qnum at parameter",qnum)
        
    else:
        
        qnum=confqnum
        print ("use  config qnum",qnum)
    
    
    
    night=paras[3]
    print ("config night 1 day 0:",night)

    
    ekionly='NO'
    
    sent='0' 
    only15m='NO'    
    print ("eki,loss:",eki,loss)
    
    

    
    if (night=='1'):
        exchange=24
    else:
        exchange=23





#last 10 minues for ekidashi/loscut
# at night 00:00
#day 15:45
    if (only15m=='YES'):
        if (night=='0'):
            endtime1='15:00'
            endtime2='15:15'
        elif(night=='1'):
            endtime1='05:15'
            endtime2='05:30'
    else:
    #always   
        endtime1='00:00'
        endtime2='25:00'
    #endtime2='22:15'
    with open('kabutoken.txt','r') as token:
        tkey=token.read(100)
#********************************


    mbuy=tbuy=msell=tsell=0
    x = date.today()
    nextd=x+timedelta(days=1)

    dx=nextd.strftime("%Y-%m-%d")
    tdate=dx
    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jdate=dt_j.strftime('%Y%m%d')
    jdate2=dt_j.strftime('%Y-%m-%d')
    jtime=dt_j.strftime('%H:%M')
    ltime=time.strftime('%H:%M')
    
    #**************************first entry quote*************
    kk=0
    res=0
    #**************wait until starting entry**********
    while (jtime<'08:45' and jtime>='05:30'):
        #debug
        break

        
        
        dt_j=datetime.now(timeZ_J)
        jtime=dt_j.strftime('%H:%M')
        print (jtime)
        print ("do not start yet for monitering")
        time.sleep(20) 
    
    #******start monioring****
    if (jtime>='08:45' or (jtime<='05:30' and jtime>='00:00')):
        entry_data=get_entry_data3(actionyobi,0)
        print ("entry-data ",entry_data)
        
        initq=0
        if (entry_data and entry_data[1]>0):
            initq=entry_data[1]
        else:
            print ("NO Entry data")
            initq=0
        print ("Entry data ",tdate,initq)
    #debug
    
    initq=float(28100)
    rinitq=float(0)
    
    if (initq>20000):    
        print ("start monitoring")
        #sent=0
        #print ("endtime1,endtime2,actionyobi,direction,initq,qnum,jdate2,eki,loss,ekionly,night,sent,hold,rinitq")
        #print (endtime1,endtime2,actionyobi,direction,initq,qnum,jdate2,eki,loss,ekionly,night,sent,hold,rinitq)

        #************************monitoring *****************************************
        print ("beginnig qnum:",qnum)
        res=auto2(endtime1,endtime2,actionyobi,direction,initq,qnum,jdate2,eki,loss,ekionly,night,sent,hold,rinitq)
    else:
        print ("ERROR:initq is wrong!, no monitoring") 

    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jdate=dt_j.strftime('%Y%m%d')
    jdate2=dt_j.strftime('%Y-%m-%d')
    jtime=dt_j.strftime('%H:%M')
    cont=read_config2(actionyobi)
    newqnum=int(cont[2])
    print ("after auto qnum",newqnum)
    
    if (res==1):
        print ("lscut or ekidashi is done")
            #reduce qnum
        
    
    #********************************************************
    #night  must be char
    if (jtime>='08:45' and jtime<='15:15'):
        night='0'
    else:
        night='1'
    if (endyobi==yobi):

        print ("last day of this order",actionyobi,endyobi,yobi)
        hold=''
        print ("result after auto",res)
        if (res==1):
            print ("lscut or ekidashi is done")

            pass
        else:
            
            confs=read_config2(actionyobi)
            currqnum=int(confs[2])            

            eflag=send_order4(actionyobi,direction,hold,currqnum,night)
            print (eflag)
            confs=read_config2(actionyobi)
            oldqnum=int(confs[2])
            newqnum=oldqnum-qnum
            update_config(actionyobi,newqnum)
             


    print ("while monitoring is done")
    
    if (res==4):
        print ("stop because of reverse was done")
    elif (res==5):
        print ("addtional sell/buy 10 units is issued")
    
    