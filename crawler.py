from unicodedata import category
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver") # 다운받은 크롬드라이버 위치
driver.implicitly_wait(3)
driver.get("https://www.wadiz.kr/web/wreward/category/288?keyword=&endYn=ALL&order=recommend") #크롤링 대상 페이지

import time
wadiz_body=[]
wadiz_title=[]
wadiz_category=[]

from selenium.webdriver.common.by import By

#table = driver.find_element(By.CLASS_NAME , "ProjectCardList_container__3Y14k") # 상품들을 포함하는 껍데기
#rows = table.find_element(By.CLASS_NAME, "ProjectCardList_item__1owJa") # 열하나 = 상품 하나

for i in range(1, 3):
    table = driver.find_element(By.CLASS_NAME , "ProjectCardList_container__3Y14k") # 표 전체
    rows = table.find_elements(By.CLASS_NAME , "ProjectCardList_item__1owJa")
    rows = table.find_elements(By.CLASS_NAME , "ProjectCardList_item__1owJa")[i]
    rows.click()
    time.sleep(0.3)
    
    body = driver.find_elements(By.XPATH, f'//*[@id="introdetails"]/div')
    for value in body:
        wadiz_body.append(value.text)

    title = driver.find_element(By.XPATH, f'//*[@id="container"]/div[3]/h2/a')
    wadiz_title.append(title.text)

    category = driver.find_element(By.XPATH, f'//*[@id="container"]/div[3]/p')
    wadiz_category.append(category.text)

    time.sleep(0.2)

    driver.back()
    
    #button = driver.find_element(By.CLASS_NAME, "back-btn")
    #button.click()

    time.sleep(0.2)

import pandas as pd
import numpy as np
df1 = pd.DataFrame([{'title':wadiz_title,'body':wadiz_body,'category':wadiz_category}])

len(df1)

import csv
df1.to_csv("wadiz.csv",mode='w',encoding='utf-8-sig')


driver.quit()