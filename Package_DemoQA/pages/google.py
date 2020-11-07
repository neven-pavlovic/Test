from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    url = "https://www.google.com/"

    # locating the search text box
    search_input = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver

    # loading the page
    def load(self):
        self.driver.get(self.url)

    # googling the phrase
    def search(self, phrase):
        search_input = self.driver.find_element(*self.search_input)
        search_input.send_keys(phrase + Keys.RETURN)

    # returns first result of google search
    def first_result(self):
        result = self.driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/a/h3")
        return result

    # returns the number of results
    def number_of_results(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[7]/div/div/div/div/div").get_attribute(
            'innerText')
        string_no_of_results =  text.split('(')[0].replace('.', '')
        int_no_of_results = int(''.join(filter(str.isdigit, string_no_of_results)))
        return int_no_of_results
