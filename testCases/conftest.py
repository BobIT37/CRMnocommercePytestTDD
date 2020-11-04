from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="/Users/bobit/PycharmProjects/CRMnopcommercePytestPOM/Drivers/chromedriver")
        print("Launching Chrome brwoser.................")
#adeddededede
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="/Users/bobit/PycharmProjects/CRMnopcommercePytestPOM/Drivers/geckodriver")
        print("Launching Firefox brwoser.................")

    else:
        print("Check your browser... No found browser...!")
    return driver

def pytest_addoption(parser):    #This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

################ PyTest HTML Report #################

# It is hook for Adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Product Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'BobIT'

# It is hook for delete/ modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
