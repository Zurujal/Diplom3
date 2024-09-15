from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 50).until(
            expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator):
        WebDriverWait(
            self.driver, 50).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_text_switch(self,locator, value):
        WebDriverWait(self.driver, 50).until_not(expected_conditions.text_to_be_present_in_element(locator, value))


    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def drag_and_drop(self, element_from, element_to):
        from_element = self.find_element_with_wait(element_from)
        to_element = self.find_element_with_wait(element_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()
