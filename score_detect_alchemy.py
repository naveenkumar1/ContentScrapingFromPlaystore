__author__ = 'HP 15'
import requests
import json
inputfile=open('output/com.infonow.bofacontent.txt').read().split('\n')
resultfile=open("alchemy_result_bofa.txt","w+")
for id in inputfile:
    n='http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment?outputMode=json&showSourceText=1&apikey=db7ed74365433979bf3f7c1eeb07fb0a105055fe&text='+id
    r=requests.get(n)
    result=r.json()
    json.dump(result,resultfile)
    resultfile.write(',\n')
#     print 1
#     resultfile.write(str("text :")+str(result["text"]+'\n'))
#     resultfile.write(str("type :")+str(result["docSentiment"]["type"]+'\n'))
#     if result["docSentiment"]["type"]!='neutral':
#         resultfile.write(str("score :")+str(result["docSentiment"]["score"]+'\n'))
#     resultfile.write('},'+'\n')
# resultfile.close()
print "completed"

