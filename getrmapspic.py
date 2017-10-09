import os,sys
import datetime,time
from datetime import timedelta

now=datetime.datetime.now()
yyyy='%04d' % now.year
mm='%02d' % now.month
dd='%02d' % now.day
hh=now.hour
mi=now.minute
yesterday=now+datetime.timedelta(days=-1)
dby=now+datetime.timedelta(days=-2)
yyyydby='%04d' % dby.year
mmdby='%02d' % dby.month
dddby='%02d' % dby.day
dbyday=yyyydby+mmdby+dddby

def del_all_pics():  #dangerous
    os.system('del H:\\YBGJ\\RMAPS\\500h_spl_10wind\\*')
    os.system('del H:\\YBGJ\\RMAPS\\500h_850wind_850rh\\*')
    os.system('del H:\\YBGJ\\RMAPS\\500h_700wind_700rh\\*')
    os.system('del H:\\YBGJ\\RMAPS\\dp3\\*')
    os.system('del H:\\YBGJ\\RMAPS\\dp24\\*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\1h\\*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\3h\\*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\6h\\*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\12h\\*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\24h\\*')
    os.system('del H:\\YBGJ\\RMAPS\\t700\\*')
    os.system('del H:\\YBGJ\\RMAPS\\t850\\*')
    os.system('del H:\\YBGJ\\RMAPS\\t2m\\*')
    os.system('del H:\\YBGJ\\RMAPS\\ts\\*')
    os.system('del H:\\YBGJ\\RMAPS\\dt12\\*')
    os.system('del H:\\YBGJ\\RMAPS\\dt24\\*')
    os.system('del H:\\YBGJ\\RMAPS\\dt850_24\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tmax12\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tmin12\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tmax24\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tmin24\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tsmin24\\*')
    os.system('del H:\\YBGJ\\RMAPS\\wind10\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53696\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53698\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53798\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53892\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54401\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54423\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54449\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54511\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54515\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54527\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54534\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54602\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54616\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54701\\*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54702\\*')
    os.system('del H:\\YBGJ\\RMAPS\\sta_time\\*')

def del_pic_2_days_ago(dbyday):
    os.system('del H:\\YBGJ\\RMAPS\\500h_spl_10wind\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\500h_850wind_850rh\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\500h_700wind_700rh\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\dp3\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\dp24\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\1h\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\3h\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\6h\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\12h\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\precipitation\\24h\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\t700\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\t850\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\t2m\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\ts\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\dt12\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\dt24\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\dt850_24\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tmax12\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tmin12\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tmax24\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tmin24\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tsmin24\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\wind10\\'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53696\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53698\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53798\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\53892\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54401\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54423\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54449\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54511\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54515\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54527\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54534\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54602\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54616\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54701\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\tlogp\\54702\\'+'*'+dbyday+'*')
    os.system('del H:\\YBGJ\\RMAPS\\sta_time\\'+'*'+dbyday+'*')
if hh>=10 and hh<=14:
	del_pic_2_days_ago(dbyday)

def copy_rmaps_pics(veri_time):
	cp_high_01='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/high/01/*.* H:\\YBGJ\\RMAPS\\500h_spl_10wind'
	os.system(cp_high_01)
	cp_high_02='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/high/02/*.* H:\\YBGJ\\RMAPS\\500h_850wind_850rh'
	os.system(cp_high_02)
	cp_high_03='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/high/03/*.* H:\\YBGJ\\RMAPS\\500h_700wind_700rh'
	os.system(cp_high_03)
	cp_high_16='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/high/16/*.* H:\\YBGJ\\RMAPS\\dp3'
	os.system(cp_high_16)
	cp_high_17='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/high/17/*.* H:\\YBGJ\\RMAPS\\dp24'
	os.system(cp_high_17)
	cp_surf_10='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/surface/10/*.* H:\\YBGJ\\RMAPS\\precipitation\\1h'
	os.system(cp_surf_10)
	cp_surf_11='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/surface/11/*.* H:\\YBGJ\\RMAPS\\precipitation\\3h'
	os.system(cp_surf_11)
	cp_surf_12='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/surface/12/*.* H:\\YBGJ\\RMAPS\\precipitation\\6h'
	os.system(cp_surf_12)
	cp_surf_13='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/surface/13/*.* H:\\YBGJ\\RMAPS\\precipitation\\12h'
	os.system(cp_surf_13)
	cp_surf_14='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/surface/14/*.* H:\\YBGJ\\RMAPS\\precipitation\\24h'
	os.system(cp_surf_14)
	cp_temp_02='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/02/*.* H:\\YBGJ\\RMAPS\\t700'
	os.system(cp_temp_02)
	cp_temp_03='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/03/*.* H:\\YBGJ\\RMAPS\\t850'
	os.system(cp_temp_03)
	cp_temp_04='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/04/*.* H:\\YBGJ\\RMAPS\\t2m'
	os.system(cp_temp_04)
	cp_temp_05='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/05/*.* H:\\YBGJ\\RMAPS\\ts'
	os.system(cp_temp_05)
	cp_temp_08='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/08/*.* H:\\YBGJ\\RMAPS\\dt12'
	os.system(cp_temp_08)
	cp_temp_09='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/09/*.* H:\\YBGJ\\RMAPS\\dt24'
	os.system(cp_temp_09)
	cp_temp_10='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/10/*.* H:\\YBGJ\\RMAPS\\dt850_24'
	os.system(cp_temp_10)
	cp_temp_15='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/15/*.* H:\\YBGJ\\RMAPS\\tmax12'
	os.system(cp_temp_15)
	cp_temp_16='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/16/*.* H:\\YBGJ\\RMAPS\\tmin12'
	os.system(cp_temp_16)
	cp_temp_17='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/17/*.* H:\\YBGJ\\RMAPS\\tmax24'
	os.system(cp_temp_17)
	cp_temp_18='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/18/*.* H:\\YBGJ\\RMAPS\\tmin24'
	os.system(cp_temp_18)
	cp_temp_26='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/temperature/26/*.* H:\\YBGJ\\RMAPS\\tsmin24'
	os.system(cp_temp_26)
	cp_dang_02='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/dangerous/02/*.* H:\\YBGJ\\RMAPS\\wind10'
	os.system(cp_dang_02)
	cp_stat_01_53696='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/53696* H:\\YBGJ\\RMAPS\\tlogp\\53696'
	os.system(cp_stat_01_53696)
	cp_stat_01_53698='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/53698* H:\\YBGJ\\RMAPS\\tlogp\\53698'
	os.system(cp_stat_01_53698)
	cp_stat_01_53798='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/53798* H:\\YBGJ\\RMAPS\\tlogp\\53798'
	os.system(cp_stat_01_53798)
	cp_stat_01_53892='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/53892* H:\\YBGJ\\RMAPS\\tlogp\\53892'
	os.system(cp_stat_01_53892)
	cp_stat_01_54401='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54401* H:\\YBGJ\\RMAPS\\tlogp\\54401'
	os.system(cp_stat_01_54401)
	cp_stat_01_54423='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54423* H:\\YBGJ\\RMAPS\\tlogp\\54423'
	os.system(cp_stat_01_54423)
	cp_stat_01_54449='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54449* H:\\YBGJ\\RMAPS\\tlogp\\54449'
	os.system(cp_stat_01_54449)
	cp_stat_01_54511='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54511* H:\\YBGJ\\RMAPS\\tlogp\\54511'
	os.system(cp_stat_01_54511)
	cp_stat_01_54515='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54515* H:\\YBGJ\\RMAPS\\tlogp\\54515'
	os.system(cp_stat_01_54515)
	cp_stat_01_54527='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54527* H:\\YBGJ\\RMAPS\\tlogp\\54527'
	os.system(cp_stat_01_54527)
	cp_stat_01_54534='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54534* H:\\YBGJ\\RMAPS\\tlogp\\54534'
	os.system(cp_stat_01_54534)
	cp_stat_01_54602='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54602* H:\\YBGJ\\RMAPS\\tlogp\\54602'
	os.system(cp_stat_01_54602)
	cp_stat_01_54616='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54616* H:\\YBGJ\\RMAPS\\tlogp\\54616'
	os.system(cp_stat_01_54616)
	cp_stat_01_54701='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54701* H:\\YBGJ\\RMAPS\\tlogp\\54701'
	os.system(cp_stat_01_54701)
	cp_stat_01_54702='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/01/54702* H:\\YBGJ\\RMAPS\\tlogp\\54702'
	os.system(cp_stat_01_54702)
	cp_stat_03='d:\\pscp.exe -unsafe -P 25517 -r -l hbqx1 -pw hbqx66 110.249.214.230:/public/home/hbqx1/post/result/picture/'+ veri_time + '/d02/station/03/*.* H:\\YBGJ\\RMAPS\\sta_time'
	os.system(cp_stat_03)

hm=int(hh)*100+int(mi)
print hm
if hm>=1030 and hm<=1200:
	veri_hh='08'
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm>=1330 and hm<=1500:
	veri_hh='11'
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm>=1630 and hm<=1800:
	veri_hh='14'
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm>=1930 and hm<=2100:
	veri_hh='17'
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm>=2230 and hm<=2330:
	veri_hh='20'
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm==0000:
	veri_hh='20'
	yyyy=yesterday.year
	mm=yesterday.month
	dd=yesterday.day
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm>=130 and hm<=300:
	veri_hh='23'
	yyyy=yesterday.year
	mm=yesterday.month
	dd=yesterday.day
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm>=430 and hm<= 600:
	veri_hh='02'
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
elif hm>=715 and hm<=745:
	veri_hh='05'
	veri_time=yyyy+mm+dd+veri_hh
	copy_rmaps_pics(veri_time)
else:
    exit