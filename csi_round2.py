"""
from datetime import date,timedelta
fromdate = date(2020,1,1)
todate = date(2020,1,1)
daygenerator = (fromdate + timedelta(x) for x in range((todate - fromdate).days+1))
tmp=sum(1 for day in daygenerator if day.weekday() < 5)
print(tmp)
"""
from datetime import datetime,timedelta

f=open('input.txt')
f1=open('output.txt','w')
try:
 day=f.read().split()
 c=0
 n=day[0]
 n1=day[1]
 start=datetime(int(n[-4:]),int(n[3:5]),int(n[0:2]))
 end=datetime(int(n1[-4:]),int(n1[3:5]),int(n1[0:2]))
 
 if start<end  and start>datetime(2019,12,30) and end>datetime(2019,12,30):
  daygenerator = (start + timedelta(x) for x in range((end - start).days+1))
  c=sum(1 for day in daygenerator if day.weekday() < 5)
  f1.write(str(c))
 else:
  f1.write('invalid')
except Exception as e:
 f1.write(str(e))

f.close()
f1.close()


#sir solution
"""
from datetime import *
f=open('input.txt')
y=f.readline()
l1,m1=map(str,y.split(" "))
f.close()
l=list(map(int,l1.split("/")))
m=list(map(int,m1.split("/")))
valid = True
try :
    datetime(l[2],l[1],l[0])
    datetime(m[2],m[1],m[0])
except ValueError :
    valid = False
if(valid) :
    time1=datetime(l[2],l[1],l[0])
    time2=datetime(m[2],m[1],m[0])
    time3=datetime(2019,12,30)
    n=(time2-time1).days
    c=0
    if(time2>=time1 and time1>=time3):
        f1=time1.weekday()
        for i in range(1,n+2):
            if(f1!=5 and f1!=6):
                c+=1
            if(f1!=6):
                f1+=1
            else:
                f1=0
        out=str(c)
    else:
        out="Invalid"
else:
    out="error"
ff=open("output.txt","w")
ff.write(out)
ff.close()
"""
