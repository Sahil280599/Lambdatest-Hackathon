import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--platform", action="store", default="Windows 10")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture(scope="function")
def driver(browser, platform):
    username = os.getenv("LAMBDATEST_USERNAME")
    access_key = os.getenv("LAMBDATEST_ACCESS_KEY")
    
    if not username or not access_key:
        raise ValueError("LambdaTest credentials not found in environment variables")
    
    options = webdriver.ChromeOptions()
    lt_options = {
        "build": "LambdaTest Hackathon",
        "name": "Test Automation",
        "platformName": platform,
        "browserName": browser,
        "browserVersion": "latest",
        "selenium_version": "4.0.0",
        "w3c": True,
        "console": True,
        "network": True,
        "visual": True
    }
    
    options.set_capability('LT:Options', lt_options)
    
    grid_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )
    
    yield driver
    
    driver.quit()

@pytest.fixture(autouse=True)
def setup_teardown(driver):
    # Setup
    driver.maximize_window()
    yield
    # Teardown
    pass 