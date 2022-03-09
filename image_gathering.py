from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import io
from urllib import request
from PIL import Image

# webdriver.Chrome path
CHROMEDRIVER = 'C:\git\python-tutorial\chromedriver.exe'  # 99.0.4844.51

# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=chrome_service)

# 画像ページにアクセス
browser.get('https://scraping-for-beginner.herokuapp.com/image')

# 画像のurlを取得
elems = browser.find_elements(By.CLASS_NAME, 'material-placeholder')
for index,elem in enumerate(elems):
    elem = elem.find_element(By.TAG_NAME, 'img')
    url = elem.get_attribute('src')

    f = io.BytesIO(request.urlopen(url,timeout=3).read())
    img = Image.open(f)
    img.save('image/img{}.jpg'.format(index))
