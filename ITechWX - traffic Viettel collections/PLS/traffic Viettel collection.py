from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select
from PIL import Image
from telegram import Bot
import asyncio
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Có thể thử nếu gặp lỗi đồ họa
chrome_options.add_argument("--remote-debugging-port=9222")

# Create driver for chrome control

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Go to web Viettel monitor

driver.get("https://mve.viettel.vn")

# Login account

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#username"))
)

user = driver.find_element(By.CSS_SELECTOR, "#username")
user.send_keys("congtypvs") # Fill username

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#password"))
)

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("12345678a@A") # Fill password

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#loginSubmit"))
)

login = driver.find_element(By.CSS_SELECTOR, "#loginSubmit")
login.click() # Submit login

# Go to "Tra cuu"

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#treeFind > a"))
)

tracuu_tag = driver.find_element(By.CSS_SELECTOR, "#treeFind > a")
tracuu_tag.click() 

# Go to "Dich vu dang su dung"

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/aside/section/ul/li[4]/ul/li[1]/a/span[1]"))
)

services_tag = driver.find_element(By.XPATH, "/html/body/div[1]/aside/section/ul/li[4]/ul/li[1]/a/span[1]")
services_tag.click() 

# Go to "Vien thong"

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#menuKT"))
)

vienthong_tag = driver.find_element(By.CSS_SELECTOR, "#menuKT")
vienthong_tag.click() 

# Choose service

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/div[3]/ng-view/section/div[1]/form/div[1]/div/div/div[2]/div[1]/div/span/span[1]/span/span"))
)

service_choices = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/ng-view/section/div[1]/form/div[1]/div/div/div[2]/div[1]/div/span/span[1]/span/span")
service_choices.click()

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.ID, "listServices"))
)
ill_tag = Select(driver.find_element(By.ID, "listServices"))
ill_tag.select_by_visible_text("Leasedline Internet")

# Search channel

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#searchChannel"))
)

searchchannel = driver.find_element(By.CSS_SELECTOR, "#searchChannel")
searchchannel.click()

# Choose channel and view traffic monitor

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#channelList_paginate > ul > li:nth-child(4) > a"))
)

list2 = driver.find_element(By.CSS_SELECTOR, "#channelList_paginate > ul > li:nth-child(4) > a")
list2.click() # Go to list 2
     
WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/div[3]/ng-view/section/div[2]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td[5]/a[1][contains(@onclick, 'Tân Cảng')]"))
)

view = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/ng-view/section/div[2]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td[5]/a[1][contains(@onclick, 'Tân Cảng')]")
view.click()

# Change to traffic during a month
try:
 WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[3]/ng-view/div[4]/div/div/div[2]/div[1]/div[2]/div/div/i"))
)
except Exception as e:
 print ("kHONG TIM THAY ELEMENT")

settime = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/ng-view/div[4]/div/div/div[2]/div[1]/div[2]/div/div/i")
settime.click() # Click icon to choose

end_time_value = datetime.now()
start_time_value = end_time_value -timedelta(days=15)

end_time_str = end_time_value.strftime("%d/%m/%Y %H:%M")
start_time_str = start_time_value.strftime("%d/%m/%Y %H:%M")

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[15]/div[1]/div[1]/input"))
)

start_time = driver.find_element(By.XPATH, "/html/body/div[15]/div[1]/div[1]/input")
start_time.clear()
start_time.send_keys(start_time_str) # Start time

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[15]/div[2]/div[1]/input"))
)

end_time = driver.find_element(By.XPATH, "/html/body/div[15]/div[2]/div[1]/input")
end_time.clear()
end_time.send_keys(end_time_str) # End time

WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[15]/div[3]/div/button[1]"))
)

submit_time = driver.find_element(By.XPATH, "/html/body/div[15]/div[3]/div/button[1]")
submit_time.click() # Submit

# Screenshot and crop photos

screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'traffic.png')

time.sleep(10)
driver.save_screenshot(screenshot_path)

img = Image.open(screenshot_path)

cropped_img = img.crop((149.5,56 , 1145.5, 768))
cropped_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'final traffic photo.png')
cropped_img.save(cropped_path)

# Send photo to telegram

start_date = start_time_value.strftime("%d/%m/%Y")
end_date   = end_time_value.strftime("%d/%m/%Y")

caption_text = (
    "[Ultron](tg://user?id=7186932047)\n"
    "*\\#TRAFFIC \\#BANDWIDTH*\n\n"
    f"*Lưu lượng băng thông từ {start_date} đến {end_date}*\n"
    f"  \\_Chi nhánh: Sun\n"
    f"  \\_Nhà mạng: Viettel\n"
    f"  \\_Mã kênh: t008\\_gll\\_pvscttvt9\n"
    f"  \\_Loại kênh: ILL\n"
    "PVS trân trọng gửi thông tin đến quý khách hàng\n\n"
    "🤖 A message from PVS BOT\\!"
)

async def send_photo_to_telegram(image_path):
    bot = Bot(token='7186932047:AAGM4WO868umgAKSQ7klPZmM4tO4m6xPpYE')
    with open(image_path, 'rb') as image_file:
        await bot.send_photo(chat_id=-4279839509, photo=image_file, caption=caption_text,parse_mode='MarkdownV2')

# Thực thi hàm async
async def main():
    await send_photo_to_telegram(cropped_path)

# Chạy chương trình
if __name__ == "__main__":
    asyncio.run(main())

time.sleep(300) 
driver.quit()