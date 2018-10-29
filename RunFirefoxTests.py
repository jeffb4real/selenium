from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(
            executable_path="/Users/urieow/Documents/Webdriver/geckodriver"
        )

        # Load webpage
        driver.get("https://letskodeit.teachable.com/p/practice")

ff = RunFFTests()
ff.testMethod()
