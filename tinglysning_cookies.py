from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def get_session_cookies():
  # Define options for Chrome driver
  options = webdriver.ChromeOptions()
  options.add_argument("--log-level=3")
  options.add_argument("window-size=600,1000")
  
  # Get the latest version of Chrome driver and install it
  s = Service(ChromeDriverManager().install())
  
  # Start chrome instance and go to tinglysning redirect url for nemlog-in
  driver = webdriver.Chrome(service=s, chrome_options=options)
  driver.get("https://www.tinglysning.dk/tmv/")
  
  driver.quit()
  