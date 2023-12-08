import sys
import yaml
from tinglysning_cookies import get_session_cookies
from tinglysning_rest import get_property, get_property_summary

def main():
  # Load config
  with open("config.yaml", 'rt') as f:
      config = yaml.safe_load(f.read())

  # Get cookies
  cookies = get_session_cookies(config)
  
  hovednoteringsnummer = sys.argv[1] # This is for testing purpose and will be removed later
  property = get_property(config, cookies, hovednoteringsnummer)
  if property is None: sys.exit(0)
  
  summary = get_property_summary(config, cookies, property["items"][0]["uuid"])
  if summary is None: sys.exit(0)
  
  print(summary["EjendomSummariskHentResultat"]["ns:EjendomSummarisk"]["ns7:ModelId"])
  


if __name__ == "__main__":
    main()