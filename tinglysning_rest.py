import requests
import xmltodict

def __check_status_code(res):
  print(res.status_code)
  if res.status_code in range (200, 300):
    return True, True # Success, continue
  elif res.status_code in range (400, 500):
    return False, True # Success, continue
  elif res.status_code in range (500, 600):
    return False, False # Success, continue

def __get_request_url(url, cookies, config):
  headers = {
    "Cookie": f"TDK_JSESSIONID={cookies['TDK_JSESSIONID']}; TDK_CSRFTOKEN={cookies['TDK_CSRFTOKEN']}",
    "Accept": "application/json",
  }
  res = requests.get(url, headers=headers)

  success, continue_ = __check_status_code(res)
  if not success:
    if not continue_:
      exit(config["error_messages"]["error_5xx"])
    else:
      return None

  if res.headers['content-type'].find("application/json") != -1:
    return res.json()
  elif res.headers['content-type'].find("application/xml") != -1:
    return xmltodict.parse(res.content)

def get_property(config, cookies, hovednoteringsnummer):
  url = config["rest"]["urls"]["get_property"].format(hovednoteringsnummer)
  res = __get_request_url(url, cookies, config)
    
  return res

def get_property_summary(config, cookies, uuid):
  url = config["rest"]["urls"]["get_property_summary"].format(uuid)
  res = __get_request_url(url, cookies, config)

  return res
