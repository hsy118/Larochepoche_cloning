from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request as req
import urllib.parse
import os
import csv
import re
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
url = 'https://www.larocheposay.co.kr/product/list.do?cate2=1004'
r = requests.get(url, headers = headers)


"""
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
"""

driver = webdriver.Chrome(executable_path='/Users/sengyuphan/Desktop/web_crawling/chromedriver')

driver.get('https://www.larocheposay.co.kr/product/list.do?cate2=1004')
time.sleep(4.0)




body = driver.find_element_by_css_selector('body')

body = driver.find_element_by_css_selector('body')



plus_btn_count = 0
while plus_btn_count < 8:
    try:
        plus_btn_count += 1
        body.send_keys(Keys.END)
        #body.send_keys(Keys.END)
        time.sleep(3)

    finally:
        pass


req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')


ul_tag = soup.find('ul', {'class': 'product_list'})

a_tag = ul_tag.find_all('a', href =True)

url_list = []

for num in a_tag:
    port_number = num['href']
    # four_number = port_number[25:29]
    url_list.append(port_number)
   
true_list = []
for i in url_list:
    i=i.replace(",","").split("'")
    Q=i[1]
    true_list.append(Q)
    

csv_filename = 'product.csv'
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)

# tag_string = ''

for i in true_list:

    driver.get(f'https://www.larocheposay.co.kr/product/view/{i}.do')
    time.sleep(1.0)

    req = driver.page_source
    soup1 = BeautifulSoup(req, 'html.parser')

    #tags = driver.find_element_by_class_name('datail_info_top').find_element_by_class_name('hash').text
    tags = driver.find_element_by_class_name('datail_info_top').find_element_by_class_name('hash').find_elements_by_tag_name('a')
    tag_string = ''
    for idtags in range(0, len(tags)):
        if idtags >=0 and idtags <= (len(tags)-2):
            tag_string += tags[idtags].text + ','
        else:
            tag_string += tags[idtags].text

    

    title = driver.find_element_by_class_name('datail_info_top').find_element_by_class_name('tit').text
    split_title = title.split('\n')

    for word in split_title:
        category = split_title[0]
        name = split_title[1]
        detail = split_title[2]


    image_string=''

    big_image = driver.find_element_by_class_name('view').find_elements_by_tag_name('li')
    for  big_img in big_image:
        small_img = big_img.get_attribute('style').split("\"")
        image_string += small_img[1]+ "뿌"
        
        # middle_img = small_img.split("\"")
        #image_string += middle_img[1]+ "뿌"
        
    star = driver.find_element_by_class_name('star').text
    #soup1.find('span', {'class': 'star'}).text

    
    try:
        gifts = driver.find_element_by_class_name('gift').find_elements_by_tag_name('i')
        gift_string = ''
        for idx in range(0, len(gifts)):
            if idx >=0 and idx <= (len(gifts)-2):
                gift_string += gifts[idx].text + ','
            else:
                gift_string += gifts[idx].text

        gift_setting = gift_string.split(',')
        free = ''
        sale = ''

        for j in gift_setting:
            if j == '증정':
                free = True
            elif j == '세일':
                sale = True
            else:
                pass



    except:
        free = ''
        sale = ''
    
    #price = driver.find_element_by_class_name('datail_info_data').find_element_by_class_name('price').text
    detail_info_data = driver.find_element_by_class_name('datail_info_data')
    try:
        sale_price = detail_info_data.find_element_by_tag_name('del').text.replace(',','').replace('원','')
        price = detail_info_data.find_element_by_class_name('price').text.replace(',','').replace('원','')
    except:
        price = detail_info_data.find_element_by_class_name('price').text.replace(',','').replace('원','')
        sale_price = detail_info_data.find_element_by_class_name('price').text.replace(',','').replace('원','')

    try:
        component_string = ''
        item_components = soup1.find('span', {'class' : 'component'})
        em_component = item_components.find_all('em')
        em_components = re.compile('[가-힣]+').findall(str(em_component))
        for id_com in range(0, len(em_components)):
            if id_com >= 0 and id_com <= (len(em_components)-2):
                component_string += em_components[id_com] + ','
            else:
                component_string += em_components[id_com]
    except:
        em_components = ''
        component_string = ''

    csv_writer.writerow((
        category, name, detail,price, sale_price, tag_string, free, sale, component_string, image_string
        ))

csv_open.close()


