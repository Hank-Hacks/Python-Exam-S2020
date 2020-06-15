#hbehaeg1:04092020:find-covid19.py

import covid19

'''
Find which countrues have total cases > 100 & CFR > 8
Find which countries have both cases > 100 and CMR > 20
'''

f2=open('covid19-CFR-results.dat', 'w')

for i in covid19.countries:
	if covid19.total_cases(i) > 100 and covid19.CFR(i) > 8:
		f2.write("%s" % i + "%.2f" % covid19.CFR(i) + "\n")
f2.close()

f3=open('covid19-CMR-results.dat', 'w')

for i in covid19.countries:
	if covid19.total_cases(i) > 100 and covid19.CMR(i) > 20:
		f3.write("%s	" % i + "%.2e" % covid19.CMR(i) + "\n")

f3.close()
	



