import requests
import validators


def check(url):
    if(validators.url(url)):
        r = requests.get(url)
        if(r.status_code is 200):
            return True
    else:
        return False
