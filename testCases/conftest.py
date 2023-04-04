import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
        driver = webdriver.Chrome()
        print("Launching chrome browser...........")
        return driver

# ++++++++++++++++++++++++++++++++++++++ pyTest HTML Report ++++++++++++++++++++++++++++++++ #

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Brahma kumar'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop("Plugins", None)
