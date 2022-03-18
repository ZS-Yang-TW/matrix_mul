from selenium import webdriver  #操縱網頁的套件
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup   #爬蟲工具

from ConnectDatabase import database
import time

DB = database()
DB.connect()

options = Options()
options.add_argument("--disable-notifications")

# In[] 開啟矩陣計算機
driver = webdriver.Firefox()
driver.get("https://matrixcalc.org/zh/")

# In[] A矩陣元素定位
A_0_0 = driver.find_element_by_id("A-0-0")
A_0_1 = driver.find_element_by_id("A-0-1")
A_0_2 = driver.find_element_by_id("A-0-2")
A_1_0 = driver.find_element_by_id("A-1-0")
A_1_1 = driver.find_element_by_id("A-1-1")
A_1_2 = driver.find_element_by_id("A-1-2")
A_2_0 = driver.find_element_by_id("A-2-0")
A_2_1 = driver.find_element_by_id("A-2-1")
A_2_2 = driver.find_element_by_id("A-2-2")

# In[] B矩陣元素定位
B_0_0 = driver.find_element_by_id("B-0-0")
B_0_1 = driver.find_element_by_id("B-0-1")
B_0_2 = driver.find_element_by_id("B-0-2")
B_1_0 = driver.find_element_by_id("B-1-0")
B_1_1 = driver.find_element_by_id("B-1-1")
B_1_2 = driver.find_element_by_id("B-1-2")
B_2_0 = driver.find_element_by_id("B-2-0")
B_2_1 = driver.find_element_by_id("B-2-1")
B_2_2 = driver.find_element_by_id("B-2-2")

# In[] 設定A矩陣
A_0_0.send_keys("1"), A_0_1.send_keys("2"), A_0_2.send_keys("3")
A_1_0.send_keys("2"), A_1_1.send_keys("2"), A_1_2.send_keys("3")
A_2_0.send_keys("1"), A_2_1.send_keys("2"), A_2_2.send_keys("1")

# In[] 設定B矩陣
B_0_0.send_keys("1"), B_0_1.send_keys("2"), B_0_2.send_keys("99")
B_1_0.send_keys("3"), B_1_1.send_keys("4"), B_1_2.send_keys("3")
B_2_0.send_keys("1"), B_2_1.send_keys("2"), B_2_2.send_keys("1")

# In[] 計算A + B
# btn_Add = driver.find_element_by_xpath("//button[@data-expression = 'A + B']")
# btn_Add.click()

btn_Mul = driver.find_element_by_xpath("//button[@data-expression = 'A * B']")
btn_Mul.click()

# btn_Det = driver.find_element_by_xpath("//button[@data-expression = 'determinant A']")
# btn_Det.click()

# In[] 選取計算結果的表示方式
btn_type = driver.find_element_by_xpath("//button[@data-for-matrix = 'i1-7']")
time.sleep(1)
btn_type.click()

show = driver.find_element_by_xpath("//a[@data-i = '5']")  # 以純文字表示
time.sleep(1)
show.click()

# In[] 獲得計算結果
soup = BeautifulSoup(driver.page_source, "html.parser")

result = soup.find("div", {"id": "dialog-content"})
detail = result.find("input", {"type": "text"})
print(detail["value"])

DB.insert(detail["value"])

methon = soup.find("li", {"id": "action-1"})
result2 = methon.find_all("details", {"data-i": "1"})
for detail2 in result2:
    post = detail2.find("summary")
    print(post.getText())

driver.quit()