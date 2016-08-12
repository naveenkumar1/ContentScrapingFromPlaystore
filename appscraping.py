__author__ = 'HP 15'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
#import pprint #for prettyprinting on the console
import json
#https://play.google.com/store/apps/details?id='+id+'&hl=en
def appopen(id):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://play.google.com/store/apps/details?id='+id)
    sample = ".//*[@id='body-content']/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]"
    buttonElement = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(sample))
    buttonElement.click()
    time.sleep(10)
    #commentfile=open('output/'+id+"content.txt","w+")
    try:            
        for x in range(10):
            print x
            if driver.find_element_by_xpath(sample).is_displayed():
                buttonElement.click()
                time.sleep(1)
                scraping_text=driver.page_source
            else:
                scraping_text=driver.page_source
                time.sleep(10)
                buttonElement.click()
                time.sleep(1)
        soup=BeautifulSoup(scraping_text,'html.parser')
        author_name = soup.find_all('span', {"class": "author-name"})
        review_text = soup.find_all('div', {'class': 'review-body'})
        review_title = soup.find_all('span',{'class': 'review-title'})
        review_date = soup.find_all('span',{'class': 'review-date'})
        rating = soup.find_all('div', {'class': 'tiny-star star-rating-non-editable-container'})
        final_author_name,final_review_text,final_review_title,final_review_date,final_rating=[],[],[],[],[]
        for y in rating:
            final_rating.append(str(str(y)[35]))
        for x in author_name:
            final_author_name.append(x.text.encode('ascii','ignore'))
        for x in review_date:
            final_review_date.append(str(x.text))
        for w in review_title:
            final_review_title.append(w.text.encode('ascii','ignore'))
        for m in review_text:
            final_review_text.append(m.text.encode('ascii','ignore'))
        #    commentfile.write(str(m.text.encode('ascii','ignore'))+'\n')
        #commentfile.close()
        absolute_rating=final_rating[9:len(final_rating)-17]
        absolute_author_name= final_author_name[6:]
        absolute_date= final_review_date
        absolute_review_text=final_review_text
        absolute_title=final_review_title[8:]
        result=zip(absolute_rating,absolute_author_name,absolute_date,absolute_title,absolute_review_text)
        keys=["rating","name","Date","title","comments"]
        myfile=open('output/'+id+".txt","w+")
        for res in result:
            json.dump(dict(zip(keys,res)),myfile,ensure_ascii=False)
            #pprint.pprint(dict(zip(keys,res)))
            myfile.write(',\n')
        myfile.close()
        driver.quit()
    except Exception as e:
        soup=BeautifulSoup(scraping_text,'html.parser')
        author_name = soup.find_all('span', {"class": "author-name"})
        review_text = soup.find_all('div', {'class': 'review-body'})
        review_title = soup.find_all('span',{'class': 'review-title'})
        review_date = soup.find_all('span',{'class':'review-date'})
        rating = soup.find_all('div', {'class': 'tiny-star star-rating-non-editable-container'})
        final_author_name,final_review_text,final_review_title,final_review_date,final_rating=[],[],[],[],[]
        for y in rating:
            print y
            final_rating.append(str(str(y)[35]))
        for x in author_name:
            final_author_name.append(x.text.encode('ascii','ignore'))
        for x in review_date:
            final_review_date.append(str(x.text))
        for w in review_title:
            final_review_title.append(w.text.encode('ascii','ignore'))
        for m in review_text:
            final_review_text.append(m.text.encode('ascii','ignore'))
            #commentfile.write(str(m.text.encode('ascii','ignore'))+'\n')
        #commentfile.close()
        absolute_rating=final_rating[9:len(final_rating)-17]
        absolute_author_name= final_author_name[6:]
        absolute_date= final_review_date
        absolute_review_text=final_review_text
        absolute_title=final_review_title[8:]
        result=zip(absolute_rating,absolute_author_name,absolute_date,absolute_title,absolute_review_text)
        keys=["rating","name","Date","title","comments"]
        myfile=open('output/'+id+".txt","w+")
        for res in result:
            json.dump(dict(zip(keys,res)),myfile,ensure_ascii=False)
            #pprint.pprint(dict(zip(keys,res)))
            myfile.write(',\n')
        myfile.close()
        print e
        driver.quit()

'''
This is removed just to remove the dependency in the script. Accidental change in script may lead to complete loss of functionality
Uncomment this section just if you want to give inputs directly from the script
idlist=['com.whatsapp','com.bsb.hike','com.kiloo.subwaysurf']
for id in idlist:
    appopen(id) '''

#This code is added to give the inputs from a separate file so that the in script changes will be minimum and to remove dependency in the script
idlist = open("sample.txt").read()
idlist = idlist.split('\n')
for id in idlist:
    appopen(id)