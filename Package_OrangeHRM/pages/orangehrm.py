from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrangeHRMPage:
    url = "https://orangehrm-demo-6x.orangehrmlive.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # loading the page
    def load(self):
        self.driver.get(self.url)

    # finds the login button
    def login(self):
        return self.driver.find_element(By.NAME, 'Submit')

    # finds Recruitment dropdown list
    def findRecruitment(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div/div[4]/ul/li[6]/a")

    # finds Candidates element from Recruitment dropdownlist
    def findCandidates(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div/div[4]/ul/li[6]/div/ul/li[2]/a")

    # refreshes the page and finds out the number of candidates
    def findNumberOfCandidates(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('noncoreIframe')

        number_of_candidates = self.driver.find_element(By.ID, "fromToOf").get_attribute('innerText')
        self.driver.switch_to.default_content()
        return int(number_of_candidates.split(' ')[-1])

    # adds candidate using its name, middle name, last name, email, cv and vacancy
    def addCandidate(self, name, middlename, lastname, email, path_to_cv):
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "addItemBtn").click()
        first_name = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 "/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/div[2]/div[1]/input")))
        first_name.send_keys(name)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/div[2]/div[2]/input").send_keys(
            middlename)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/div[2]/div[3]/input").send_keys(
            lastname)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/div[3]/div[1]/input").send_keys(
            email)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/div[1]/div[1]/div/input").send_keys(
            path_to_cv)

        # clicks on Vacancy dropdown box
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/div[5]/div[1]/div/label").click()

        # chooses the "Customer Success Executive" vacancy
        cse = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/div[5]/div[1]/div/div/ul/div/li[1]/a/p")))
        cse.click()

        # returns the Save button
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/a[1]")

    # returns the checkbox of the newest candidate
    def checkboxOfTheNewestCandidate(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('noncoreIframe')
        checkbox = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[7]/div/div[2]/table/tbody/tr[1]/td[1]/label")))
        return checkbox

    # delete all chosen candidates
    def delete(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/div[1]/div[7]/div/div[2]/table/thead/tr/th[1]/a").click()
        delete_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[7]/div/div[2]/table/thead/tr/th[1]/ul/li[3]/a")))
        delete_button.click()
        delete_confirmation = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/a[2]")))
        delete_confirmation.click()

    # logs user out of website
    def logOut(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('noncoreIframe')
        account_name = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/a/span[2]")))
        account_name.click()
        logout = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/ul/li[3]/a")))
        logout.click()
