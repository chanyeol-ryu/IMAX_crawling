from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import telepot

token = '6086502097:AAHCdxSaFxMUDoDaPOT4-vYV9Wpi8qAP4oU'
mc = '5713613686'   # userinfobot -> ID
bot = telepot.Bot(token)

# 크롬 실행
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# cgv 접속
driver.get("https://www.cgv.co.kr/")

# 극장 클릭
xpath = "//a[@href='/theaters/']"
driver.find_element("xpath",xpath).click()

# CGV 용산 아이파크몰 클릭
xpath = "//a[@title='CGV용산아이파크몰']"
driver.find_element("xpath",xpath).click()

while True:
    # iframe 처리
    driver.switch_to.frame("ifrm_movie_time_table")
    # 날짜 클릭
    driver.find_element(By.XPATH, '//*[@id="slider"]/div[1]/ul/li[6]/div/a').click()
    # IMAX 있는지 확인 (없으면 -1, 있으면 다른 값)
    xpath = "//div[@class='sect-showtimes']"
    if driver.find_element("xpath",xpath).text.find("IMAX") == -1:
        # 새로고침
        driver.refresh()
        print("예매 불가")
        bot.sendMessage(mc, '예매 불가')
        time.sleep(1)
    else:
        print("예매 가능")
        bot.sendMessage(mc, '예매 가능')
        break
