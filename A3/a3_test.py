import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        #self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("num1")
        elem.send_keys("12")
	elem2 = driver.find_element_by_name("num2")
        elem2.send_keys("12")
	time.sleep(2)
        elem2.send_keys(Keys.RETURN)
	time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
