from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

class test_GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://suninjuly.github.io/get_attribute.html')
        cls.driver.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("All test passed!")

    def test_Calculate(self):
        driver = self.driver

        x_element = driver.find_element_by_id('treasure')
        x = x_element.get_attribute("valuex")
     #   x = x_element.text
        y = calc(x)
        input_field = self.driver.find_element_by_id('answer')
        input_field.send_keys(y)

        people_radio = driver.find_element_by_id("peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked == "true", "People radio is not selected by default"

        check_box = self.driver.find_element_by_id('robotCheckbox')
        check_box.click()
        print("robotCheckbox is Clicked ")
        radio_btn = self.driver.find_element_by_id('robotsRule')
        radio_btn.click()
        print("robotsRule is Clicked ")
        btnSubmit = self.driver.find_element_by_css_selector('button')
        btnSubmit.click()
        print("button is Clicked ")
        time.sleep(1)

        wait = WebDriverWait(driver, 2)
        rez = wait.until(EC.alert_is_present(),"Alert in not opened")
        alert = driver.switch_to.alert
        print("alert text = " + alert.text )
        alert.accept()


    #try:
        #rez = WebDriverWait(driver, 5).until(EC.alert_is_present(),"Alert in not opened")
        #alert = driver.switch_to.alert
        #print("alert text = " + alert.text)
        #alert.accept()
    #except TimeoutException:
    #    print("alert does not Exist in page")   
        
if __name__ == '__main__':
   unittest.main()         
  