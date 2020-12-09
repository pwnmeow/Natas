import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
url = 'http://%s.natas.labs.overthewire.org' % username
session = requests.Session()
response = requests.post(url , data={"secret" : "oubWYf2kBq", "submit" : "submit"}, auth = (username, password))
content = response.text

#print content
print re.findall('Access granted. The password for natas9 is (.*)', content)[0]