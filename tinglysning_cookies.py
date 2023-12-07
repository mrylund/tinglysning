import sys
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_session_cookies(config):
  """Get the session cookies needed to make requests to tinglysning.dk

  Returns
  -------
  dict
      Dictionary containing the cookies needed to make requests to tinglysning.dk
  """  
  # Define options for Chrome driver
  options = webdriver.ChromeOptions()
  options.add_argument("--log-level=3")
  options.add_argument("window-size=600,1000")

  # Get the latest version of Chrome driver and install it
  s = Service(ChromeDriverManager().install())
  
  # Start chrome instance and go to tinglysning redirect url for nemlog-in
  driver = webdriver.Chrome(service=s, chrome_options=options)
  driver.get(config["tinglysning"]['nemlog_in_redirect_url'])

  # Check if browser is redirected to nemlog-in and wait for user to log in
  # if we are not redirected back to tinglysning.dk within 120 seconds we quit
  url = driver.current_url
  if (url.startswith(config["tinglysning"]["nemlog_in_login_url_start"])):
    try:
      WebDriverWait(driver, 120).until(
        EC.url_contains(config["tinglysning"]["nemlog_in_success_string"])
      )
    except Exception as e:
      driver.quit()
      sys.exit(config['error_messages']['nemlog_in_timeout'])
  
  # Get cookies from browser and define a dictionary for the cookies we need
  cookies = driver.get_cookies()
  cookie_dict = {}
  
  # Add the cookies we need to the dictionary
  for cookie in cookies:
    if cookie['name'] == 'TDK_JSESSIONID' or cookie['name'] == 'TDK_CSRFTOKEN':
      cookie_dict[cookie['name']] = cookie['value']

  # Check if cookie_dict contains the cookies we need
  if not ('TDK_JSESSIONID' in cookie_dict and 'TDK_CSRFTOKEN' in cookie_dict):
    sys.exit(config['error_messages']['insufficient_cookies'])
    
  # Quit the browser, we don't need it anymore
  driver.quit()
  
  return cookie_dict
