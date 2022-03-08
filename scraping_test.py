from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import pandas as pd


# webdriver.Chrome path
CHROMEDRIVER = 'C:\git\python-tutorial\chromedriver.exe' #99.0.4844.51

# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=chrome_service)

# ランキングページにアクセス
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

# すべての観光地名、ランクを格納するリストを用意
titles = []
ranks = []
categories = []

for page in range(1,4):
    url = 'https://scraping-for-beginner.herokuapp.com/ranking/?page={}'.format(page)
    browser.get(url)

    elems_rankingBox = browser.find_elements(By.CLASS_NAME, 'u_areaListRankingBox')
    for elem_rankingBox in elems_rankingBox:
        # 観光地名
        elem_title = elem_rankingBox.find_element(By.CLASS_NAME,'u_title')
        title = elem_title.text.split('\n')[1]
        titles.append(title)

        # 総合評価
        elem_rank = elem_rankingBox.find_element(
            By.CLASS_NAME, 'u_rankBox').find_element(By.CLASS_NAME, 'evaluateNumber')
        rank = float(elem_rank.text)
        ranks.append(rank)

        # 各項目の評価
        evals = []
        elem_evalList = elem_rankingBox.find_element(
            By.CLASS_NAME, 'u_categoryTipsItem').find_elements(By.CLASS_NAME, 'is_rank')
        for elem_eval in elem_evalList:
            elem_eval.find_element(By.CLASS_NAME, 'evaluateNumber')
            eval = float(elem_eval.text)
            evals.append(eval)
        categories.append(evals)

# DataFrameを定義
df = pd.DataFrame()
df['観光地名'] = titles
df['総合評価'] = ranks

df_categories = pd.DataFrame(categories)
df_categories.columns = ['楽しさ','人混みの多さ','景色','アクセス']

df = pd.concat([df,df_categories],axis=1)
df.to_csv('観光地情報.csv',index=False)
