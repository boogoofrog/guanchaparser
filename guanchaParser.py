#!/usr/bin/python
#coding:utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib
import csv
import datetime

def guancha(keyword, page):
    global time
    
    driver = webdriver.PhantomJS()
    url = 'https://user.guancha.cn/main/search?click=news&keyword=' + urllib.quote(keyword)
    driver.get(url)

    for x in range(1, page):
        print('Start fetching page ' + str(x) + '...')
        driver.find_element_by_class_name('index-add-more').click()
        time.sleep(3)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    title_tag = soup.find_all('div', class_='list-item')

    s = "%Y%m%d%H%M%S"
    with open(datetime.datetime.now().strftime(s) + '.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        
        writer.writerow(['title','url','date'])

        for tag in title_tag:
            h4 = tag.find('h4')
            # print(str(h4.a.attrs['href']))
            time = str(h4.a.attrs['href']).rsplit('/',1)[1].replace('.shtml','')
            times = time.rsplit('_',1)[0]
            # print(h4.a.text)
            print(times.replace('_','/') + ' ' + h4.a.text)
            writer.writerow([h4.a.text.encode('utf-8'), h4.a.attrs['href'], times.replace('_','/')])

guancha('韩国瑜', 5)