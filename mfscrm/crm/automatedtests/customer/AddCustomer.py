import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AddCustomer(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_add_customer(self):
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
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("ATS_Customer1")
        time.sleep(2)
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("UNO")
        time.sleep(2)
        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Student")
        time.sleep(2)
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("pki-178")
        time.sleep(2)
        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("700120")
        time.sleep(2)
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("Dodge Street")
        time.sleep(2)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        time.sleep(2)
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("Nebraska")
        time.sleep(2)
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68182")
        time.sleep(2)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("test@unomaha.edu")
        time.sleep(2)
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("8240749752")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button")
        time.sleep(2)
        elem.click()

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

