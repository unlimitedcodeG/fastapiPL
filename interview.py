from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置WebDriver路径
driver_path = 'D:\\personalLearn\\fastapiPL\\chromedriver.exe'

# 使用新的参数设置方式
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(driver_path), options=options)

# 打开网页
driver.get('https://www.picchealth.com/picchealth/gkxxpl/jbxx/bxjbxx/zsbxcp/index.html')
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

try:
    time.sleep(3)
    # 找到产品下拉菜单并点击（这需要你根据实际的HTML元素修改选择器）
    product_dropdown = driver.execute_async_script('document.querySelector("body > div.portlet > div > div.sjscroll > div > div:nth-child(2) > div.bbcl > span")')
    print(product_dropdown)


finally:
    # 完成后关闭浏览器
    driver.quit()
