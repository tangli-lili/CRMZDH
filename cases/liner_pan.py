from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#打开登录网页
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)

#添加组件
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
                                    "> div.nav-collapse.collapse > ul.nav.pull-right > "
                                    "li:nth-child(6) > a > img").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
sleep(2)
driver.find_element(By.ID,"add").click() #点击添加组件
sleep(2)
driver.find_element(By.ID,"title").send_keys("哈哈")
sleep(2)
driver.find_element(By.NAME,"submit").click()
sleep(6)
driver.quit()
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
#组件修改
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
                                    "> div.nav-collapse.collapse > ul.nav.pull-right > "
                                    "li:nth-child(6) > a > img").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
sleep(2)
driver.find_element(By.ID,"update_widget").click()
sleep(2)
driver.find_element(By.NAME,"title").clear()
driver.find_element(By.NAME,"title").send_keys("hello")
sleep(2)
driver.find_element(By.NAME,"submit").click()
sleep(5)
driver.quit()
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
# 添加日程
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
                                    "> div.nav-collapse.collapse > ul.nav.pull-right > "
                                    "li:nth-child(6) > a > img").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#calendar > div.c-event-grid > div.c-event-body >"
                                    " div.data-head > a").click()
sleep(2)
driver.find_element(By.NAME,"subject").send_keys("胜任")
sleep(2)
driver.find_element(By.NAME,"submit").click()

sleep(5)
driver.quit()
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
# 切换到公告列表
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
                                    "> div.nav-collapse.collapse > ul.nav.pull-right > "
                                    "li:nth-child(6) > a > img").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
sleep(2)

driver.find_element(By.CSS_SELECTOR,"#widgets > div > div:nth-child(6) > div > div.dash-title > a").click()
sleep(5)
driver.quit()
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
# 商机统计
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
                                    "> div.nav-collapse.collapse > ul.nav.pull-right > "
                                    "li:nth-child(6) > a > img").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a").click()
sleep(2)

driver.find_element(By.CSS_SELECTOR,"#widgets > div > div.sort-list.ui-sortable >"
                                    " div:nth-child(1) > div > div.dash-title > a").click()
sleep(5)
driver.quit()





