from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
#ActionChainsクラスは通常のクリック処理や値の設定以外にもShiftを押しながら入力という処理やF1やF3など特殊なキー操作を行うことができる
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
#browser=webdriver.Chrome()
def login():
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    f=open('insta.txt','a',encoding='utf-8')
    f.write("instagramにアクセスしました\n")
    f.close()
    time.sleep(5)

    #メアドとパスワードを入力
    browser.find_element_by_name('username').send_keys('shokoshi2')
    time.sleep(5)
    browser.find_element_by_name('password').send_keys('evnLEX8P')
    time.sleep(5)

    #ログインボタンを押す
    browser.find_element_by_class_name('L3NKy       ').click()
    time.sleep(random.randint(7,12))
    f=open('insta.txt','a',encoding='utf-8')
    f.write("instagramにログインしました\n")
    f.close()
    time.sleep(5)
    
def tagsearch(tag):
    #指定したtagのページへ移動
    instaurl='https://www.instagram.com/explore/tags/'
    browser.get(instaurl+tag)
    time.sleep(random.randint(7,15))
    f=open('insta.txt','a',encoding='utf-8')
    f.write("listtagより、"+ tag +"で検索を行いました\n")
    f.close()
    time.sleep(5)

def clicknice_follow():
    target=browser.find_elements_by_class_name('_9AhH0')[10]#写真のtag
    actions=ActionChains(browser)
    actions.move_to_element(target)#ターゲット要素(target)にマウスカーソル移動
    actions.perform()#実行
    f=open('insta.txt','a',encoding='utf-8')
    f.write("最新の投稿まで画面を移動しました\n")
    f.close()
    time.sleep(5)
    
    try:
            browser.find_elements_by_class_name('_9AhH0')[9].click()#写真のtag
            time.sleep(random.randint(7,15))
            f=open('insta.txt','a',encoding='utf-8')
            f.write('投稿をクリックしました\n')
            f.close()
            time.sleep(5)
            browser.find_element_by_class_name('fr66n').click()#いいねのtag
            time.sleep(random.randint(7,15))
            f=open('insta.txt','a',encoding='utf-8')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(5)
            browser.find_element_by_class_name('bY2yH').click()#フォローのtag
            f=open('insta.txt','a',encoding='utf-8')
            f.write("フォローしました\n")
            f.close()
            time.sleep(5)

    except webDriverException:
        f=open('insta.txt','a',encoding='utf-8')
        f.write("エラーが発生しました\n")
        f.close()
        return
    
    for i in range(random.randint(5,10)):
        try:
            browser.find_element_by_class_name('coreSpriteRightPaginationArrow').click()#次の写真へ移動するtag
            f = open('insta.txt','a',encoding='utf-8')
            f.write("次の投稿へ移動しました\n")
            f.close()
            time.sleep(random.randint(random.randint(7, 12), random.randint(15, 20)))
            
            browser.find_element_by_class_name('fr66n').click()#いいねのtag
            f = open('insta.txt','a',encoding='utf-8')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(random.randint(random.randint(7, 12), random.randint(15, 20)))
            
            browser.find_element_by_class_name('bY2yH').click()#フォローのtag
            f=open('insta.txt','a',encoding='utf-8')
            f.write("フォローしました\n")
            f.close()
            time.sleep(5)
    
        except WebDriverException:
            f = open('insta.txt','a',encoding='utf-8')
            f.write("２つ目の位置でエラーが発生しました\n")
            f.close()
            break
#browser = webdriver.Chrome()
if __name__ == '__main__':#おまじない
#以下のtaglistには、いいねをしたいtagをセットしてください
    taglist = ['animal', 'animals', 'reptile', 'animalcute']
    
    while True:
        options=ChromeOptions()
        #ヘッドレスモードを有効にする
        options.add_argument('--headless')
        #ChromeのWebDriverオブジェクトを作成する
        browser=Chrome(options=options)
        #browser = webdriver.Chrome()#指定の位置にwebdriverのpathを書いてください　例）/Users/ユーザー名/chromedriver
        time.sleep(5)
        login()

        tagsearch(random.choice(taglist))#ランダムにtagを選択
        clicknice_follow()

        browser.close()

        abc = random.randint(random.randint(20,100 ), random.randint(120, 1800))
        #encoding = "utf-8"
        f = open('insta.txt','a',encoding='utf-8')
        f.write(str(abc)+"秒待機します\n")
        f.close()

        time.sleep(abc)        
