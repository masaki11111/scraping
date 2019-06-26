from selenium import webdriver
import pandas as pd
import time

driver=webdriver.Chrome()

driver.get('https://www.ekiten.jp/area/')
path='/html/body/div[2]/div/div[2]/main/div[44]/div/a'
lists=[]
i=6

elems=driver.find_elements_by_class_name('p-shop_box')#class名に空白がある場合はどちらか一方を選んであげるとよい
for elem in elems:
    list=[]
    elem_title=elem.find_element_by_class_name('p-shop_box_head_title_body').text
    list.append(elem_title)
    elem_supplement=elem.find_element_by_class_name('p-shop_box_head_supplement').text
    list.append(elem_supplement)
    elem_address=elem.find_element_by_class_name('p-shop_box_basic_info').find_elements_by_class_name('p-shop_box_basic_info_item')[1]
    elem_address=elem_address.text.split('\n')[1]
    list.append(elem_address)
    href = elem.find_element_by_tag_name("a").get_attribute("href")#リンク先のURLの取得方法
    list.append(href)
    lists.append(list)
    
next_page=driver.find_element_by_xpath(path).get_attribute("href")
driver.get(next_page)
driver.implicitly_wait(10)#implicity_wait():指定したドライバに対して引数の時間分（秒）、要素が見つかるまで(ロードされるまで)待機
time.sleep(10)
path="/html/body/div[2]/div/div[2]/main/div[44]/div[2]/a"

while True:
#len(elem)
    elems=driver.find_elements_by_class_name('p-shop_box')#class名に空白がある場合はどちらか一方を選んであげるとよい
    for elem in elems:
        list=[]
        elem_title=elem.find_element_by_class_name('p-shop_box_head_title_body').text
        list.append(elem_title)
        elem_supplement=elem.find_element_by_class_name('p-shop_box_head_supplement').text
        list.append(elem_supplement)
        elem_address=elem.find_element_by_class_name('p-shop_box_basic_info').find_elements_by_class_name('p-shop_box_basic_info_item')[1]
        elem_address=elem_address.text.split('\n')[1]
        list.append(elem_address)
        href = elem.find_element_by_tag_name("a").get_attribute("href")#リンク先のURLの取得方法
        list.append(href)
        lists.append(list)
    lists
    #if len(driver.find_elements_by_xpath(path))>0:
    if i>0:
        next_page=driver.find_element_by_xpath(path).get_attribute("href")
        driver.get(next_page)
        driver.implicitly_wait(10)#implicity_wait():指定したドライバに対して引数の時間分（秒）、要素が見つかるまで(ロードされるまで)待機
        time.sleep(10)
        
        path="/html/body/div[2]/div/div[2]/main/div[44]/div[3]/a"
        i-=1    
    else:
        break
#type('elems')

df=pd.DataFrame(lists)
df.columns=['店舗名','ジャンル','住所','URL']
df.to_csv('ekiten.csv',encoding="utf_8_sig")#インデックスを消すためにはFalseを
