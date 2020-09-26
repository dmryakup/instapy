#before run please download chrome driver and write your path down
#using pip or pip3, install time,selenium,random and keyboard to your environment
#write your user name, password and hastag for like

from time import sleep 
from selenium import webdriver
from keyboard import press
import random

username="" #write your username
password="" #write your password
hashtag="likesforfollowers"
begenisayisi=500
yapilanbegeni=0
dongusayisi=50

browser = webdriver.Chrome("C:/Users/"the path"/chromedriver.exe") #write your path

browser.get('https://www.instagram.com/accounts/login/')

sleep(2)

username_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

username_input.send_keys(username)
password_input.send_keys(password)

browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click() #login buttonuna tıklama

sleep(4)

browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
sleep(2)

browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
browser.implicitly_wait(2)

#browser.minimize_window()

for yapilanbegeni in range(0,begenisayisi):
    sleep(3*random.random())
    try:
        like_button = browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
        browser.implicitly_wait(5)
    finally:   
        sleep(1)
    try:
        browser.execute_script("arguments[0].click();", like_button[0])
        browser.implicitly_wait(5)
    finally:
        sleep(1)
    sleep(random.random())
    yapilanbegeni += 1
    browser.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click() #sonraki
    sleep(2*random.random())

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

    yapilanbegeni += 1

browser.delete_all_cookies()
browser.close()

print("Yapılan işlem sonucu {} fotoğraf başarıyla beğenildi",format(yapilanbegeni))
print("İnstagram limitlerine takılmamak adına 1 2 saat sonra tekrar çalıştırabilirsiniz.")