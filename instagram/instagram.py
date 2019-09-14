
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
#ActionChainsクラスは通常のクリック処理や値の設定以外にもShiftを押しながら入力という処理やF1やF3など特殊なキー操作を行うことができる
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


# In[ ]:


#loginする関数
def login():
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    f=open('insta.txt','a',encoding='utf-8')
    f.write("instagramにアクセスしました\n")
    f.close()
    time.sleep(random.randint(5,10))

    #メアドとパスワードを入力
    """
    browser.find_element_by_name('username').send_keys('care24_animal')#ユーザー名を入力してください
    time.sleep(5)
    browser.find_element_by_name('password').send_keys('evnLEX8P')#パスワードを入力してください
    time.sleep(5)
    """
    browser.find_element_by_name('username').send_keys('shokoshi2')#ユーザー名を入力してください
    time.sleep(random.randint(5,10))
    browser.find_element_by_name('password').send_keys('evnLEX8P')#パスワードを入力してください
    time.sleep(random.randint(5,10))
    #ログインボタンを押す
    browser.find_element_by_class_name('L3NKy       ').click()
    time.sleep(random.randint(7,12))
    f=open('insta.txt','a',encoding='utf-8')
    f.write("instagramにログインしました\n")
    f.close()
    time.sleep(random.randint(5,10))


# In[ ]:


#指定したtagで検索する関数
def tagsearch(tag):
    #指定したtagのページへ移動
    instaurl='https://www.instagram.com/explore/tags/'
    browser.get(instaurl+tag)
    time.sleep(random.randint(2,10))
    f=open('insta.txt','a')
    f.write("listtagより、"+tag+"で検索を行いました\n")
    f.close()
    time.sleep(random.randint(5,10))


# In[ ]:


#いいねとフォローをする関数
def clicknice_follow():
    target=browser.find_elements_by_class_name('_9AhH0')[10]#写真のtag
    actions=ActionChains(browser)
    actions.move_to_element(target)#ターゲット要素(target)にマウスカーソル移動
    actions.perform()#実行
    f=open('insta.txt','a')
    f.write("最新の投稿まで画面を移動しました\n")
    f.close()
    time.sleep(random.randint(5,10))
    
    try:
            browser.find_elements_by_class_name('_9AhH0')[9].click()#写真のtag
            time.sleep(random.randint(2,10))
            f=open('insta.txt','a')
            f.write('投稿をクリックしました\n')
            f.close()
            time.sleep(1)
            browser.find_element_by_class_name('fr66n').click()#いいねのtag
            time.sleep(random.randint(2,10))
            f=open('insta.txt','a')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(random.randint(5,10))
            browser.find_element_by_class_name('bY2yH').click()#フォローのtag
            f=open('insta.txt','a')
            f.write("フォローしました\n")
            f.close()
            time.sleep(random.randint(5,10))

    except webDriverException:
        f=open('insta.txt','a')
        f.write("エラーが発生しました\n")
        f.close()
        return
    
    for i in range(random.randint(5,10)):
        try:
            browser.find_element_by_class_name('coreSpriteRightPaginationArrow').click()#次の写真へ移動するtag
            f = open('insta.txt','a')
            f.write("次の投稿へ移動しました\n")
            f.close()
            time.sleep(random.randint(random.randint(2, 5), random.randint(10, 15)))
            
            browser.find_element_by_class_name('fr66n').click()#いいねのtag
            f = open('insta.txt','a')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(random.randint(random.randint(2, 5), random.randint(10, 15)))
            
            browser.find_element_by_class_name('bY2yH').click()#フォローのtag
            f=open('insta.txt','a')
            f.write("フォローしました\n")
            f.close()
            time.sleep(random.randint(5,10))
    
        except WebDriverException:
            f = open('insta.txt','a')
            f.write("２つ目以降でエラーが発生しました\n")
            f.close()
            break
    


# In[ ]:


if __name__ == '__main__':#おまじない
#いいね、フォローをしたいtagを入力
    taglist = ['animal', 'animals', 'reptile', 'animalcute','animallovers','animalcrossing','fish','animali','cat','dog']
    while True:
        browser = webdriver.Chrome()#指定の位置にwebdriverのpathを書いてください　例）/Users/ユーザー名/chromedriver
        time.sleep(random.randint(5,10))
        login()
        
        tagsearch(random.choice(taglist))#ランダムにtagを選択
        
        clicknice_follow()
        
        browser.close()

        abc = random.randint(random.randint(3000,5000 ), random.randint(6000, 12000))
        #encoding = "utf-8"
        f = open('insta.txt','a')
        f.write(str(abc)+"秒待機します\n")
        f.close()

        time.sleep(abc)        

