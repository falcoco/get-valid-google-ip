#author inreality
import requests

li = []
with open('I:/googleip.txt','r') as f:	#This file should be consisted of source ips. Modify the loaction
	for line in f.readlines():
		li.append(line.strip())

count = 0
with open('I:/valid_ip.txt','a') as f:	#Valid ips are recorded in this file. Please modify it. 

	for x in xrange(0,len(li)):
		try:
			r = requests.get('http://'+li[x], timeout = 1)
			if r.status_code==200:
				f.write(li[x]+'\n')
				print li[x]+'\t'+'is a valid google ip and is recorded!\n'
				count=count+1
		except requests.exceptions.ConnectionError as e:
			print li[x]+'\t'+'is not a valid address currently\n'
		finally:
			pass
	print 'Test completed!'+'\t'+str(count)+' valid ips are recorded'