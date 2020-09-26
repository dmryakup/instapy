#before run please download chrome driver and write your path down
#using pip or pip3, install time,selenium,random and keyboard to your environment
#write your user name, password and hastag for like

from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from keyboard import press
import random

username="" #giriş yapılacak kullanıcı adı
password="" #giriş yapılacak kullanıcı parolası
unfollow_count=500 #takipten çıkılacak kişi sayısı
dongusayisi=28 #kac unfollow sonrası 1.5 dakika bekleyecek

browser = webdriver.Chrome("C:/Users/yakup/Desktop/Python3_calismalarim/instabot/chromedriver.exe") #chroma driver konumu. kullacağınız tarayıcıya göre driver indirip burayı değiştirebilirsiniz

browser.get('https://www.instagram.com/accounts/login/') #instagram giriş ekranımızı açıyoruz

sleep(2) #internette oluşacak yavaşlık doolayısıyla 2 sn bekliyoruz

username_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input") #kullanıcı adı kutucugunun konumu
password_input=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input") #şifre kutucuğunun konumu

username_input.send_keys(username)  #kutucuğa kullanıcı adı yazdırma
password_input.send_keys(password)  #kutucuğa şifre yazdırma

browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click() #login buttonuna tıklama

sleep(4) #4 saniye giriş ve yükleme için bekliyoruz

browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click() # profil simgesine yıklama
browser.implicitly_wait(2)  #kodu bulamazsa 2 sn boyunca tekrar deneyecek
browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div").click() #profilim yazısına tıklama
browser.implicitly_wait(2)  #kodu bulamazsa 2 sn boyunca tekrar deneyecek

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click() #takipçi penceresi açma
browser.implicitly_wait(2)  #kodu bulamazsa 2 sn boyunca tekrar deneyecek

browser.find_element_by_class_name('isgrP').click() #butnları doğru tespit etmek için takipçi penceresine 1 kere tıklama
sleep(2)

pencere = browser.find_element_by_css_selector("div[class='isgrP']")
for i in range(0,30):
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
    sleep(1)
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)

for i in range(0,12):
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - 5*arguments[0].offsetHeight;', pencere)
    sleep(1)

buttons = browser.find_elements_by_xpath('//button[text() = "Takiptesin"]') #takip edilenler butonları

#browser.minimize_window()

print("Takipten çıkarma işlemi başladı")
for unfollow in range(0,unfollow_count):
    if(unfollow%3 == 0):
        browser.execute_script("arguments[0].click();", buttons[unfollow])
        sleep(3+random.random())
        try:
            element = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//button[text() = "Takibi Bırak"]')))
            element.click()
        finally:
            sleep(1)
        sleep(2+random.random()*2+random.random())
        unfollow+=1
    elif(unfollow%3==1):
        browser.execute_script("arguments[0].click();", buttons[unfollow])
        sleep(3+random.random())
        try:
            element = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//button[text() = "Takibi Bırak"]')))
            element.click()
        finally:
            sleep(1)
        sleep(1+random.random()*6)
        unfollow+=1
    elif(unfollow%3==2):
        browser.execute_script("arguments[0].click();", buttons[unfollow])
        sleep(3+random.random())
        try:
            element = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//button[text() = "Takibi Bırak"]')))
            element.click()
        finally:
            sleep(1)
        sleep(1+random.random()*4)
        unfollow+=1
    if(unfollow%6==0):
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
    if(unfollow%8==0):
        print("{} kullanıcı takipten çıkarıldı. 50 saniye dinleniliyor".format(unfollow))
        sleep(40+random.random()*20)
    if(unfollow%11==0):
        print("{} kullanıcı takipten çıkarıldı. 20 saniye dinleniliyor".format(unfollow))
        sleep(15+random.random()*10)
    if(unfollow%dongusayisi==0):
        print("{} kullanıcı takipten çıkarıldı. İnstagram limitleri dolayısıyla 500 saniye dinleniyor".format(unfollow))
        sleep(100+random.random()*250+random.random()*200)

browser.delete_all_cookies()
browser.close()

print("Yapılan işlem sonucu {} kullanıcı başarıyla takipten çıkıldı",format(unfollow))
print("İnstagram limitlerine takılmamak adına 1 2 saat sonra tekrar çalıştırabilirsiniz.")

