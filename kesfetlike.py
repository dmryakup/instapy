#before run please download chrome driver and write your path down
#using pip or pip3, install time,selenium,random and keyboard to your environment
#write your user name and password. it will like the posts from your explore section

from time import sleep
from selenium import webdriver
from keyboard import press
import random

username=""
password=""
begenisayisi=500
yapilanbegeni=0
dongusayisi=50

browser = webdriver.Chrome("C:/Users/"write the drivers path"/chromedriver.exe")

browser.get('https://www.instagram.com/accounts/login/')

sleep(2)

username_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

username_input.send_keys(username)
password_input.send_keys(password)

browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click() #login buttonuna tıklama

sleep(4)

browser.get("https://www.instagram.com/explore/")
sleep(6)

'''for i in range(0,30):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(1)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

for i in range(0,12):
    browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
    sleep(1)
'''

#browser.find_element_by_xpath("///*[@id='react-root']/section/main/div/div[1]/div/div[1]/div[1]").click()
ilkgonderi = browser.find_element_by_css_selector("div[class='pKKVh']")
browser.implicitly_wait(2)
ilkgonderi.click()
browser.implicitly_wait(2)

#browser.minimize_window()

for yapilanbegeni in range(0,begenisayisi):
    sleep(3*random.random())
    try:
        like_button = browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
        browser.implicitly_wait(5)
        sleep(2)
    finally:   
        sleep(1)
    try:
        browser.execute_script("arguments[0].click();", like_button[0])
        browser.implicitly_wait(5)
        sleep(2)
    finally:   
        sleep(1)
    browser.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()

    yapilanbegeni += 1

    if(yapilanbegeni%3 == 0):
        sleep(1+2*random.random()+random.random())
    elif(yapilanbegeni%3==1):
        sleep(1+4*random.random()+2*random.random())
    elif(yapilanbegeni%3==2):
        sleep(1+2*random.random()+2*random.random())
    
    if(yapilanbegeni%8==0):
        print("{} fotoğraf beğenildi. 15 saniye dinleniyor".format(yapilanbegeni))
        sleep(10+random.random()*5+random.random()*10)

    if(yapilanbegeni%11==0):
        print("{} fotoğraf beğenildi. 20 saniye dinleniyor".format(yapilanbegeni))
        sleep(10+random.random()*10+random.random()*10)

    if(yapilanbegeni%dongusayisi==0):
        print("{} fotoğraf beğenildi. İnstagram limitleri dolayısıyla 300 saniye dinleniyor".format(yapilanbegeni))
        sleep(100+random.random()*100+random.random()*200)

browser.delete_all_cookies()
browser.close()

print("Yapılan işlem sonucu {} fotoğraf başarıyla beğenildi",format(yapilanbegeni))
print("İnstagram limitlerine takılmamak adına 1 2 saat sonra tekrar çalıştırabilirsiniz.")