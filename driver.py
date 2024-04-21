from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


class Driver():
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_page(self, url):
        self.driver.get(url)
        self.source = self.driver.page_source

    def new_tab(self):
        self.driver.switch_to.new_window('tab')

    def answer_form(self, info):
        for i in range(len(info[0])):
            inputs = self.driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")
            actions = ActionChains(self.driver)
            for j, input in enumerate(inputs):
                actions.send_keys_to_element(input, info[j][i])
                actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            self.driver.find_element(By.LINK_TEXT, "Submit another response").click()

    def quit(self):
        self.driver.quit()
