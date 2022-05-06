from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


sayac = 1
tekrar = 5

while True:
    browser = webdriver.Chrome()

    browser.implicitly_wait(3)

    browser.get("https://tr.tradingview.com/symbols/FX_IDC-XAUTRYG/")

    time.sleep(2)
    alis = browser.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/span')

    print(f"Alış Fiyatı: {alis.text}")


    f = open("altın.txt", "a", encoding="utf-8")
    f.write(f"Alış Fiyatı: {alis.text} \n")
    f.close()
    buton = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div/div/button[1]')
    buton.click()
    aramaClick = browser.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div/div[1]/span/form/input')
    aramaClick.send_keys("BTC")
    time.sleep(1)
    aramaClick.send_keys(Keys.ENTER)
    time.sleep(1)
    
    if sayac==tekrar:
        print("döngü bitti")
        time.sleep(2)
        browser.close()
        break
    else:
        sayac+=1
        browser.close()
