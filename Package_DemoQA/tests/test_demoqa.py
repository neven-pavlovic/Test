import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from Package_DemoQA.pages import demoqa
from Package_DemoQA.pages import google


class DemoQATest(unittest.TestCase):

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

    def test_demoqa(self):

        # this block gets us to demoqa.com
        driver = self.driver
        google_search_page = google.GoogleSearchPage(driver)
        google_search_page.load()
        google_search_page.search("demoqa.com")
        google_search_page.first_result().click()

        # this block gets us to drag and drop page and prints out text of droppable box after dropping
        demoqa_page = demoqa.DemoQAPage(driver)
        demoqa_page.findInteraction().click()
        demoqa_page.droppable().click()
        drag, drop = demoqa_page.dragAndDrop()
        ActionChains(driver).drag_and_drop(drag, drop).perform()
        print(drop.text)

        # you can specify the path to screenshot
        driver.save_screenshot("screenshot.png")

        # this block gets us to tooltip page, hovers over the button and prints out the tooltip text
        demoqa_page.widgets().click()
        driver.implicitly_wait(0.5)
        demoqa_page.tooltips().click()
        ActionChains(driver).move_to_element(demoqa_page.hoverButton()).perform()
        print(demoqa_page.toolTipText())


if __name__ == '__main__':
    unittest.main()
