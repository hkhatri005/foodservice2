import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class EditProductDetails(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_edit_product_details(self):
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
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_product_name")
        elem.clear()
        elem.send_keys("UNO_ATS_Test_Product_Updated")
        time.sleep(2)
        elem = driver.find_element_by_id("id_description")
        elem.clear()
        elem.send_keys("Student ATS test product creation updated")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button")
        time.sleep(2)
        elem.click()

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

