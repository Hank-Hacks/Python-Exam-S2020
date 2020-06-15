#hbehaeg1:04092020:covid-19.py
#a.)

'''
This module will be used to calculate case fatality risk in addition to crude mortality rate
'''
import sys

#b.)

f1=open('covid19.csv')
L2=f1.readlines()
L2.pop(0)

countries=[]
for i in L2:
	c=i.split(',')
	if c[6] not in countries:
		countries.append(c[6])

#c.)

Dcases={}
for i in countries:
	cases=[]
	for x in L2:
		if i in x:
			l=x.split(',')
			num=int(l[4])
			cases.append(num)
			Dcases[i]=cases

#d.)

Ddeaths={}
for i in countries:
	deaths=[]
	for x in L2:
		if i in x:
			d=x.split(',')
			numd=int(d[5])
			deaths.append(numd)
			Ddeaths[i]=deaths


#e.)
Dpop={}
for i in countries:
	for x in L2:
		if i in x:
			list=x.split(',')
			pop=int(list[9])
			Dpop[i]=pop

#f.)

def total_cases(country):
	tc=0
	tcl=Dcases[country]
	for i in tcl:
		tc=tc + i
	return tc

#g.)

def total_deaths(country):
	td=0
	tdl=Ddeaths[country]
	for i in tdl:
        	td=td + i
	return td

#h.)

def CFR(country):
	CFR=float((total_deaths(country)/total_cases(country))*100)
	return CFR

#i.)

def CMR(country):
	CMR=float((total_deaths(country)/Dpop[country])*100000)
	return CMR

#j.)

def daily_cases_deaths(country):
	print("Cases and Deaths")
	for i in range(len(Dcases[country])):
		cdl=print("%i" % Dcases[country][i] + "	  " + "%i" % Ddeaths[country][i] + "\n")
	return cdl

#k.)

if __name__ == "__main__":
	country=sys.argv[1]
	print("Covid-19 data for " + country)
	w=daily_cases_deaths(country)
	x=total_cases(country)
	y=total_deaths(country)
	z=Dpop[country]
	a=CFR(country)
	b=CMR(country)
	print(w)
	print("Total cases: %i" % x)
	print("Total deaths: %i" % y)
	print("Total population: %i" % z)
	print("The CFR is: %.2f" % a)
	print("The CMR is: %.2e" % b)


