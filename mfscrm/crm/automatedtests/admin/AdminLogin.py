import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AdminLogin(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_chat_admin_login(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://foodservice2.herokuapp.com/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://foodservice2.herokuapp.com/home/")
        assert "Logged In"
        time.sleep(5)

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

