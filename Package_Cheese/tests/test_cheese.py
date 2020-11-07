import unittest

from selenium import webdriver

from Package_DemoQA.pages import google


class CheeseTest(unittest.TestCase):

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

    def test_cheese(self):
        # this block googles "cheese"
        driver = self.driver
        google_search_page = google.GoogleSearchPage(driver)
        google_search_page.load()
        google_search_page.search("cheese")

        self.assertEqual(google_search_page.number_of_results(), 777, "There is too much cheese on the internet")


if __name__ == '__main__':
    unittest.main()
