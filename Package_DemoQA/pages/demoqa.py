from selenium.webdriver.common.by import By


class DemoQAPage:
    def __init__(self, driver):
        self.driver = driver

    # returns interaction web element at demoqa.com
    def findInteraction(self):
        interaction = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[5]")
        return interaction

    # returns "Droppable" from interaction dropbox
    def droppable(self):
        drag_and_drop = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div/div/div[2]/div[1]/div/div/div[5]/div/ul/li[4]")
        return drag_and_drop

    # returns draggable and droppable boxes
    def dragAndDrop(self):
        draggable = self.driver.find_element(By.ID, 'draggable')
        droppable = self.driver.find_element(By.ID, 'droppable')
        return draggable, droppable

    # finds Widgets dropbox from side menu
    def widgets(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[4]")

    # finds "Tooltips" from Widgets dropbox
    def tooltips(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[7]")

    # finds hover button
    def hoverButton(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/button")

    # finds the tooltip text
    def toolTipText(self):
        return self.driver.find_element(By.ID, "buttonToolTip").get_attribute('innerText')
