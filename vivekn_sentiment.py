__author__ = 'HP 15'
import requests
#original-key cff1c76683de1ba6217e4ec7ab908e1dfc8400fb
#temp-mail db7ed74365433979bf3f7c1eeb07fb0a105055fe

inputfile=open('output/com.infonow.bofacontent.txt').read().split('\n')
resultfile=open("sentiment_bofa.txt","w+")
for id in inputfile:
	headers = {'content-type' : 'application/json'}
	data={"txt":id}
	print 1
	url="http://sentiment.vivekn.com/api/text/"
	r=requests.post(url,data,headers)
	resultfile.write(id)
	resultfile.write(r.text)
	resultfile.write('\n')
resultfile.close()

