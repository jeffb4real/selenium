from selenium import webdriver
import os

class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "/Users/urieow/Documents/Webdriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("https://letskodeit.teachable.com/p/practice")

ff = RunChromeTests()
ff.test()