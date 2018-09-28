import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


class RunFfTests(unittest.TestCase):

    # we need to override TestCase class's method
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://192.168.0.252:9999")
        # time.sleep(5)

    def test_title(self):
        element = self.driver.find_element_by_tag_name("h2")
        actual_title_test = element.text
        expected_title_test = "Jersey RESTful Web Application!"
        self.assertEqual(actual_title_test,expected_title_test,'the title "%s" does not match with expected "%s"' %(actual_title_test,expected_title_test))

    # we need to override TestCase class's method
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
