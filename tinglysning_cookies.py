import sys
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

  # Check if browser is redirected to nemlog-in and wait for user to log in
  # if we are not redirected back to tinglysning.dk within 120 seconds we quit
  url = driver.current_url
  if (url.startswith("https://nemlog-in")):
    try:
      WebDriverWait(driver, 120).until(
        EC.url_contains("tinglysning.dk")
      )
    except Exception as e:
      driver.quit()
      sys.exit("Error: Login took too long, exiting...")
  

  driver.quit()