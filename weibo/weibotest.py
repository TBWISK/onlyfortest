from weibo import APIClient
"""
太复杂
"""
APP_KEY = "1678610898"
APP_SECRET = ""
CALLBACK_URL = "http://tbwisk.github.com"

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)

url = client.get_authorize_url()
print url
