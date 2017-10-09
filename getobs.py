# -*- coding:utf-8 -*-
import pyodbc

opfile='d:\\new.txt'
f = file(opfile,'w')

obstime='\'2017-01-13 14:00:00\''

cnxn =pyodbc.connect('DRIVER={SQL Server};SERVER=10.48.36.45;PORT=1433;DATABASE=HebElmt;UID=sa;PWD=123456')
cursor =cnxn.cursor()


sql_se= 'select ElmtNewZ.stationNum ,Humidity ,PressSeaLevel ,Tmpt ,TmptDew ,PrcpMinutes ,WindDirect10m ,WindVelocity10m ,\
        WindExtD ,WindExtV ,Latitude ,Longitude from [HebElmt].[dbo].[ElmtNewZ] ,[HebElmt].[dbo].[TabStation]\
        where [HebElmt].[dbo].[ElmtNewZ].[StationNum]=[HebElmt].[dbo].[TabStation].[StationNum]'
sql_se= sql_se + ' and [HebElmt].[dbo].[ElmtNewZ].[ObservTime]=' + obstime
sql_se2=''' and [HebElmt].[dbo].[TabStation].[City] != '内蒙' and [HebElmt].[dbo].[TabStation].[City] != '山西'
        and [HebElmt].[dbo].[TabStation].[City] != '北京'  and [HebElmt].[dbo].[TabStation].[City] != '天津'
        and [HebElmt].[dbo].[TabStation].[City] != '辽宁'  and [HebElmt].[dbo].[TabStation].[City] != '河南'
        and [HebElmt].[dbo].[TabStation].[City] != '山东'
        '''
sql_se=sql_se+sql_se2
print sql_se
        
		
cursor.execute(sql_se)
rows=cursor.fetchall()

#while 1:
#    rows = cursor.fetchone()
#    if not rows:
#        break
    #print rows[1]
#	f.write(rows[1])

for row in rows:
	#f.write('%6s %5s %.3f %.3f 1.000 1 %.2f 1.000 %.2f\n'%("ADPSFC",row[0],float(row[10])/100.,float(row[11])/100.,float(row[2]),float(row[2])))
	f.write('%6s %5s %.3f %.3f 1.000  2 %.2f 1.000 %.2f\n'%("ADPSFC",row[0],float(row[10])/100.,float(row[11])/100.,float(row[2]),float(row[2])))
	f.write('%6s %5s %.3f %.3f 1.000 11 %.2f 1.000 %.2f\n'%("ADPSFC",row[0],float(row[10])/100.,float(row[11])/100.,float(row[2]),float(row[3])/10.))
	f.write('%6s %5s %.3f %.3f 1.000 52 %.2f 1.000 %.2f\n'%("ADPSFC",row[0],float(row[10])/100.,float(row[11])/100.,float(row[2]),float(row[1])))
	f.write('%6s %5s %.3f %.3f 1.000 32 %.2f 1.000 %.2f\n'%("ADPSFC",row[0],float(row[10])/100.,float(row[11])/100.,float(row[2]),float(row[7])/10.))
	f.write('%6s %5s %.3f %.3f 1.000 17 %.2f 1.000 %.2f\n'%("ADPSFC",row[0],float(row[10])/100.,float(row[11])/100.,float(row[2]),float(row[4])+273.15))
	#f.write('%6s %5s\n'%("ADPSFC",row[0]))




f.close()
