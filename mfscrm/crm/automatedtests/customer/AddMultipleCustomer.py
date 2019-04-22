import unittest
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AddMultipleCustomer(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_add_multiple_customer(self):
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
        with open('/Users/Sandy/PycharmProjects/foodservice2/mfscrm/crm/automatedtests/testdata/customer_add.csv') as csvDataFile:
         csvreader = csv.reader(csvDataFile)
         for row in csvreader:
             elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a")
             elem.click()
             time.sleep(2)
             elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span")
             elem.click()
             time.sleep(2)
             elem = driver.find_element_by_id("id_cust_name")
             elem.send_keys(row[0])
             time.sleep(2)
             elem = driver.find_element_by_id("id_organization")
             elem.send_keys(row[1])
             time.sleep(2)
             elem = driver.find_element_by_id("id_role")
             elem.send_keys(row[2])
             time.sleep(2)
             elem = driver.find_element_by_id("id_bldgroom")
             elem.send_keys(row[3])
             time.sleep(2)
             elem = driver.find_element_by_id("id_account_number")
             elem.send_keys(row[4])
             time.sleep(2)
             elem = driver.find_element_by_id("id_address")
             elem.send_keys(row[5])
             time.sleep(2)
             elem = driver.find_element_by_id("id_city")
             elem.send_keys(row[6])
             time.sleep(2)
             elem = driver.find_element_by_id("id_state")
             elem.send_keys(row[7])
             time.sleep(2)
             elem = driver.find_element_by_id("id_zipcode")
             elem.send_keys(row[8])
             time.sleep(2)
             elem = driver.find_element_by_id("id_email")
             elem.send_keys(row[9])
             time.sleep(2)
             elem = driver.find_element_by_id("id_phone_number")
             elem.send_keys(row[10])
             time.sleep(2)
             elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button")
             time.sleep(2)
             elem.click()
             driver.get("https://foodservice2.herokuapp.com/home/")

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

