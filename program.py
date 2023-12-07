import yaml
from tinglysning_cookies import get_session_cookies

def main():
  # Load config
  with open("config.yaml", 'rt') as f:
      config = yaml.safe_load(f.read())

  # Get cookies
  cookies = get_session_cookies(config)


if __name__ == "__main__":
    main()