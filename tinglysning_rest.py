def __check_status_code(res):
  print(res.status_code)
  if res.status_code in range (200, 300):
    return True, True # Success, continue
  elif res.status_code in range (400, 500):
    return False, True # Success, continue
  elif res.status_code in range (500, 600):
    return False, False # Success, continue

