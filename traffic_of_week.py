import numpy as np
import csv
import matplotlib.pyplot as plt
#------------------------------------------------------------------------day1 일
f1=open('C:\python\day8\\traffic\day5.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day1 = []
for row in data1:
    AllTrafic_day1.append(int(row[10]))
#------------------------------------------------------------------------day2 월
f1=open('C:\python\day8\\traffic\day6.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day2 = []
for row in data1:
    AllTrafic_day2.append(int(row[10]))
#------------------------------------------------------------------------day3 화
f1=open('C:\python\day8\\traffic\day7.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day3 = []
for row in data1:
    AllTrafic_day3.append(int(row[10]))
#------------------------------------------------------------------------day4 수
f1=open('C:\python\day8\\traffic\day8.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day4 = []
for row in data1:
    AllTrafic_day4.append(int(row[10]))
#------------------------------------------------------------------------day5 목
f1=open('C:\python\day8\\traffic\day9.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day5 = []
for row in data1:
    AllTrafic_day5.append(int(row[10]))
#------------------------------------------------------------------------day6 금
f1=open('C:\python\day8\\traffic\day10.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day6 = []
for row in data1:
    AllTrafic_day6.append(int(row[10]))
#------------------------------------------------------------------------day7 토
f1=open('C:\python\day8\\traffic\day11.csv','r',encoding="cp949")
data1=csv.reader(f1)
next(data1,None)
AllTrafic_day7 = []
for row in data1:
    AllTrafic_day7.append(int(row[10]))

plt.subplot(2,4,1)
plt.plot(AllTrafic_day1)
plt.title('sunday')
plt.ylabel('traffic')
plt.subplot(2,4,2)
plt.plot(AllTrafic_day2)
plt.title('monday')
plt.ylabel('traffic')
plt.subplot(2,4,3)
plt.plot(AllTrafic_day3)
plt.title('tuesday')
plt.ylabel('traffic')
plt.subplot(2,4,4)
plt.plot(AllTrafic_day4)
plt.title('wendsday')
plt.ylabel('traffic')
plt.subplot(2,4,5)
plt.plot(AllTrafic_day5)
plt.title('thursday')
plt.ylabel('traffic')
plt.subplot(2,4,6)
plt.plot(AllTrafic_day6)
plt.title('friday')
plt.ylabel('traffic')
plt.subplot(2,4,7)
plt.plot(AllTrafic_day7)
plt.title('satarday')
plt.ylabel('traffic')


AllTrafic_day1 = sum(AllTrafic_day1)
AllTrafic_day2 = sum(AllTrafic_day2)
AllTrafic_day3 = sum(AllTrafic_day3)
AllTrafic_day4 = sum(AllTrafic_day4)
AllTrafic_day5 = sum(AllTrafic_day5)
AllTrafic_day6 = sum(AllTrafic_day6)
AllTrafic_day7 = sum(AllTrafic_day7)

AllTraffic = {'sun':AllTrafic_day1,'mon':AllTrafic_day2,'tue':AllTrafic_day3,'wed':AllTrafic_day4,'thu':AllTrafic_day5,'fri':AllTrafic_day6,'sat':AllTrafic_day7}

plt.subplot(2,4,8)
plt.plot(AllTraffic.keys(),AllTraffic.values())
plt.title('All Traffic of week')
plt.xlabel('day of week')
plt.ylabel('traffic')
plt.show()



