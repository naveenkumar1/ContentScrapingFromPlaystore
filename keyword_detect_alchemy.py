__author__ = 'HP 15'
import requests
import json
inputfile=open('output/com.infonow.bofacontent.txt').read().split('\n')
resultfile=open("alchemy_result_keyword_bofa.txt","w+")
for id in inputfile:
    n='http://gateway-a.watsonplatform.net/calls/text/TextGetRankedKeywords?outputMode=json&showSourceText=1&sentiment=1&apikey=db7ed74365433979bf3f7c1eeb07fb0a105055fe&text='+id
    r=requests.get(n)
    result=r.json()
    json.dump(result,resultfile)
#     finalength = len(result["keywords"])
#
#     resultfile.write(result["text"]+':[')
#     for i in range(finalength):
#         if result["keywords"][i]["sentiment"]["type"]=='negative':
#             resultfile.write('{'+'\n')
#             resultfile.write("type :"+result["keywords"][i]["sentiment"]["type"]+',\n')
#             resultfile.write("score: "+result["keywords"][i]["sentiment"]["score"]+',\n')
#             resultfile.write("relevance: "+result["keywords"][i]["relevance"]+',\n')
#             resultfile.write("keywordtext: "+result["keywords"][i]["text"]+',\n')
#             resultfile.write('},'+'\n')
#     resultfile.write(']'+'\n')
# resultfile.close()
print "completed"
