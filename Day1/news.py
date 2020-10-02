from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#news title 1개만 : select_one()
#sp_nws1 > dl > dt > a
#print(articles.text)#src에서 text만 가져오기


#news title 여러 개 : select()
articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

for article in articles:
    title = article.select_one('dl > dt > a').text#기사 제목
    url = article.select_one('dl > dt > a')['href']#a태그 안 href속성 가져오기(dictionary형태)
    comp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')#언론사
    ws1.append([title , url, comp])



driver.quit()
wb.save(filename='articles.xlsx')