import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%B0%95%EB%AA%85%EC%88%98%EC%A7%A4") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#여러 개 가져오기

i = 1

thumbnails = soup.select('#imgList > div > a > img')
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'img_homework/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기