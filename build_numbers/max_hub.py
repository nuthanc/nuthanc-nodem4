#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import json
from os import path
from subprocess import call
#variables
build = '1912'

# target URL to scrap
url = "https://hub.juniper.net/v2/contrail-nightly/contrail-vrouter-agent/tags/list"

# headers
headers = {
    'Authorization': "Basic Sk5QUi1DdXN0b21lcjIwMDpGU2cwdkxXXjdvTSNHWnk4SnUqZg=="
}

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(response.text, 'lxml')
# print(type(data.find_all('p')))
# print(type(data.find('p').text))
parsed_dict = json.loads(data.find('p').text)
count = 0
max = 0 
for tag in parsed_dict['tags']:
    if build in tag and '.' in tag and '-' not in tag:
        id = tag.split(".")[1]
        # For branch build
        if len(id)<=2 and int(id)<60:
            if int(id)>max:
                max=int(id)
            # print(tag)
            # print(id)
            count+=1

# print("Count:",count)
print("Max:",max)

if path.exists("/home/nuthanc/build_numbers/latest.py"):
    import latest
    if (max > latest.max and int(build) >= latest.build) or (int(build) > latest.build):
        # Do provisioning
        # For now send mail
        rc = call("/home/nuthanc/build_numbers/send_mail.sh", shell=True)

with open("/home/nuthanc/build_numbers/latest.py","w") as f:        
    f.write("build={}\n".format(build))
    f.write("max={}".format(max))

