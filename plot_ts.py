import numpy as np
import datetime,time
from datetime import timedelta
import string
import matplotlib.pyplot as plt
import pylab as pl
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

now = datetime.datetime.now()
#print "Year: %d" % now.year
yyyy= now.year
mm=now.month
dd=now.day
hh=now.hour
#print now
print "timenowis  ",yyyy,mm,dd,hh
d2 = now + datetime.timedelta(-2)
yyyy2='%04d' % d2.year
mm2='%02d' % d2.month
dd2='%02d' % d2.day
print "the day before yesterday is  ",d2,yyyy2,mm2,dd2
#veri_jobdate=2016071900
veri_jobdate=yyyy2+mm2+dd2+"00"
veri_jobdate2=yyyy2+"-"+mm2+"-"+dd2+" "+"00:00:00"
print "veri_jobdate2=",veri_jobdate2
#veri_jobdate3=time.strptime(reri_jobdate2,'%Y-%m-%d %H:%M:%S')
veri_jobdate3=datetime.datetime.strptime(veri_jobdate2, "%Y-%m-%d %X")
print "veri_jobdate3=",veri_jobdate3

step=3
veri_valid=3
i=0
#path_name="/public/home/hbqx2/met/MET_results/scores/point_stat/RMAPS/d02/acc_3hr/"+veri_jobdate+"/"
path_name="F:\\MET\\results\\"
ts0_3hr=np.zeros(16)
ts20_3hr=np.zeros(16)
#xtimes=np.empty(16,'datetime64[ns]')
xtimes=np.empty(16,dtype=np.string_)
while veri_valid<=48:
    
    print veri_valid
    veri_date = veri_jobdate3 + datetime.timedelta(hours=veri_valid)
    print "veri_date=",veri_date
    yyyy3='%04d' % veri_date.year
    mm3='%02d' % veri_date.month
    dd3='%02d' % veri_date.day
    hh3='%02d' % veri_date.hour
    veri_valid='%02d' % veri_valid
    file_name_cts="point_stat_RMAPS_"+veri_valid+"0000L_"+yyyy3+mm3+dd3+"_"+hh3+"0000V_cts.txt"
    print file_name_cts
    a=np.genfromtxt(fname=path_name+file_name_cts,skip_header=1)
    print a.shape,a.dtype,"a[0,60]=",a[0,60]
    ts0_3hr[i]=a[0,60]
    ts20_3hr[i]=a[1,60]
    xtimes[i]=veri_date
    print ts0_3hr[i],ts20_3hr[i],xtimes[i]
    i+=1
    veri_valid=string.atoi(veri_valid)
    veri_valid+=step
    
    
    
############### plotting with matplotlib  ########################################################    
    
print ts0_3hr,ts20_3hr
begindate = veri_jobdate3 + datetime.timedelta(hours=3)
dates = [begindate + timedelta(hours=i) for i in range(0,48,3)]
print dates
xaxis=np.arange(3,51,3)
print xaxis

#pl.plot_date(pl.date2num(dates), ts0_3hr, linestyle='-')
fig=plt.figure()
ylim(0,1)
plt.xlabel('valid_time')
plt.ylabel('ts_score')
plt.grid()

ax=subplot(111)
ax.plot(xaxis,ts0_3hr,color="blue", linewidth=2.5, linestyle="-", marker='*',label="ts0_3hr")
ax.plot(xaxis,ts20_3hr,color="red", linewidth=2.5, linestyle="-", marker='s',label="ts20_3hr")

plt.legend(loc='upper write')
ax.xmajorLocator   = MultipleLocator(3) #将x主刻度标签设置为3的倍数 
ax.xmajorFormatter = FormatStrFormatter('%02d') #设置x轴标签文本的格式
ax.xminorLocator   = MultipleLocator(3) #将x轴次刻度标签设置为3的倍数

ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
#set_xticks(np.linspace(0,1,9))  
#set_xticklabels( ('275', '280', '285', '290', '295',  '300',  '305',  '310', '315'))  
#set_yticks(np.linspace(0,1,8))  
#set_yticklabels( ('0.60', '0.65', '0.70', '0.75', '0.80','0.85','0.90','0.95'))
#xticks=([3,12,24,36,48])

titleStr=veri_jobdate2+'   ts_score' 
plt.title(titleStr) 
figpath='d:\pics\\'
figname=veri_jobdate+'ts_score'+'.png'

plt.show
plt.savefig(figpath+figname)
plt.clf()
    
    