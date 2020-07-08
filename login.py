from selenium import webdriver
from time import sleep
from argparse import ArgumentParser

def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))
    
class TuongTacCheo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get("https://tuongtaccheo.com")
        elm = self.driver.find_element_by_xpath("""//*[@id="memberModal"]/div/div/div[3]/button""").click()
        username_ele = self.driver.find_element_by_name('username')
        username_ele.send_keys("pduykhang01")
        password_ele = self.driver.find_element_by_name('password')
        password_ele.send_keys("8948187Q")
        login_ele = self.driver.find_element_by_xpath("""//*[@id="login"]/div/div[2]/form/input[3]""")
        login_ele.click()

    def verify_login(self):
        try:
            self.driver.find_element_by_name('username')
            return False
        except:
            return True

if __name__ == '__main__':
 

    ttc = TuongTacCheo()
    ttc.login()
    if ttc.verify_login():
        print('Đăng nhập thành công!')
    else:
        print('Đăng nhập thất bại')
 
    
