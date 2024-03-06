from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by, locator):
        return self.driver.find_element(by, locator)
        
    def click_element(self, by, locator):
        self.get_element(by, locator).click()

    def set_text_element(self, by, locator, text):
        elem = self.get_element(by, locator)
        elem.clear()
        elem.send_keys(text)

    def verify_element_text(self, by, locator, text):
        return EC.text_to_be_present_in_element(self.get_element(by,locator), text)

    def verify_element_present(self, by, locator):
        return EC.presence_of_element_located(self.get_element(by,locator))
    
    def get_text_element(self, by, locator):
        elem = self.get_element(by, locator)
        return elem.get_property("value")
    
    def wait_element_visible(self, locator):
        return wait.WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        
        