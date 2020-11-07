import os
import unittest
from datetime import date

from selenium import webdriver

from Package_OrangeHRM.pages import orangehrm


class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # you can change this line to:
        # self.driver = webdriver.Firefox(executable_path=r"PATH_TO_DRIVER") or
        # self.driver = webdriver.Edge(executable_path=r"PATH_TO_DRIVER")
        # use geckodriver for Firefox, EdgeDriver for Edge
        cls.driver = webdriver.Chrome(executable_path=r"C:\\Drivers\chromedriver.exe")

    @classmethod
    def tearDown(cls):
        cls.driver.close()

    def test_orangehrm(self):
        # this block loads the page and log us in
        driver = self.driver
        driver.maximize_window()
        orangehrm_page = orangehrm.OrangeHRMPage(driver)
        orangehrm_page.load()
        orangehrm_page.login().click()

        # this block navigates us to list of candidates
        orangehrm_page.findRecruitment().click()
        orangehrm_page.findCandidates().click()

        # finds out and prints the number of candidates
        number_of_candidates = orangehrm_page.findNumberOfCandidates()
        print(number_of_candidates)

        # adds new candidate with given name, middle name, last name, email and cv
        # vacancy is auto filled as "Customer Success Executive"
        # also, you can specify path to your cv
        orangehrm_page.addCandidate("QA Automation", "-", str(date.today()), "email@email.com",
                                    os.getcwd() + r'\cv.pdf').click()

        # checks if the number of candidates is increased by 1
        new_number_of_candidates = orangehrm_page.findNumberOfCandidates()
        self.assertEqual(number_of_candidates + 1, new_number_of_candidates)

        # deletes the new candidate
        orangehrm_page.checkboxOfTheNewestCandidate().click()
        orangehrm_page.delete()

        # checks if the number of candidates is decreased by 1
        driver.refresh()
        self.assertEqual(orangehrm_page.findNumberOfCandidates(), new_number_of_candidates - 1)

        # log out
        orangehrm_page.logOut()


if __name__ == '__main__':
    unittest.main()
