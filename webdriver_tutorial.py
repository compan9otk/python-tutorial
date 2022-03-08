from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
import pandas as pd

# webdriver.Chrome path
CHROMEDRIVER = 'C:\git\python-tutorial\chromedriver.exe' #99.0.4844.51

# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=chrome_service)

# ログインページにアクセス
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

#ログインページの要素を指定
elem_username = browser.find_element(By.ID, 'username')
elem_password = browser.find_element(By.ID, 'password')
elem_login_btn = browser.find_element(By.ID, 'login-btn')
#要素に対してアクションを行う
elem_username.send_keys('imanishi')
elem_password.send_keys('kohei')
elem_login_btn.click()

#プロフィールページのテーブルから要素を取り出す
keys =[]
values = []
elems_th = browser.find_elements(By.TAG_NAME,'th')
elems_td = browser.find_elements(By.TAG_NAME,'td')

for elem_th in elems_th:
    keys.append(elem_th.text)

for elem_td in elems_td:
    values.append(elem_td.text)

# 空のDataFrameを定義
df = pd.DataFrame()

df['項目'] = keys
df['値'] = values

# csvに出力
df.to_csv('講師情報.csv',index=False)