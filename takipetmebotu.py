#before run please download chrome driver and write your path down
#using pip or pip3, install time,selenium,random and keyboard to your environment
#write your user name, password and the username for follow its followers

from time import sleep
from selenium import webdriver
from keyboard import press
import random

username=""
password=""
takipedilecekkullaniciadi="" #takipçilerine takip isteği atmak istediğiniz kullanıcı adı

takipedilecekkullanicisayisi=500
dongusayisi=28

browser = webdriver.Chrome("C:/Users/yakup/Desktop/Python3_calismalarim/instabot/chromedriver.exe")

browser.get('https://www.instagram.com/accounts/login/')

sleep(2)

username_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

username_input.send_keys(username)
password_input.send_keys(password)

browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click() #login buttonuna tıklama

sleep(4)

search_input=browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input") #arama kutusu
search_input.send_keys(takipedilecekkullaniciadi)
browser.implicitly_wait(5)
press("enter")
sleep(1)
press("enter")
sleep(1)
press("enter")
sleep(3)

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click() #takipçi penceresi açma

#followers = browser.find_elements_by_class_name('FPmhX')
#for follower in followers:
#    toplamtakipcisayisi+=1

pencere = browser.find_element_by_css_selector("div[class='isgrP']")
for i in range(0,30):
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
    sleep(1)
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)

for i in range(0,12):
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - 5*arguments[0].offsetHeight;', pencere)
    sleep(1)

buttons = browser.find_elements_by_xpath('//button[contains(text(), "Takip Et")]')

#browser.minimize_window()

print("Takip işlemi başladı")
for takipedilen in range(0,takipedilecekkullanicisayisi):
    if(takipedilen%3 == 0):
        browser.execute_script("arguments[0].click();", buttons[takipedilen])
        sleep(1+2*random.random()+random.random())
        takipedilen+=1
    elif(takipedilen%3==1):
        browser.execute_script("arguments[0].click();", buttons[takipedilen])
        sleep(1+4*random.random()+2*random.random())
        takipedilen+=1
    elif(takipedilen%3==2):
        browser.execute_script("arguments[0].click();", buttons[takipedilen])
        sleep(1+2*random.random()+2*random.random())
        takipedilen+=1
    if(takipedilen%6==0):
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
    if(takipedilen%8==0):
        print("{} kullanıcı takip edildi. 50 saniye dinleniyor".format(takipedilen))
        sleep(35+random.random()*20+random.random()*15)
    if(takipedilen%11==0):
        print("{} kullanıcı takip edildi. 20 saniye dinleniyor".format(takipedilen))
        sleep(17+random.random()*5+random.random()*2)
    if(takipedilen%dongusayisi==0):
        print("{} kullanıcı takip edildi. İnstagram limitleri dolayısıyla 400 saniye dinleniyor".format(takipedilen))
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
        sleep(100+random.random()*250+random.random()*200)

browser.close()
browser.delete_all_cookies()

print("Yapılan işlem sonucu {} kullanıcı başarıyla takip edildi".format(takipedilen))
print("İnstagram limitlerine takılmamak adına 1 2 saat sonra tekrar çalıştırabilirsiniz.")