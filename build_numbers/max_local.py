import requests
from bs4 import BeautifulSoup
import json
from os import path
from subprocess import call

#variables
build = '1912'

# target URL to scrap
url = "http://10.204.217.152:5000/v2/contrail-vrouter-agent/tags/list"

# headers

# send request to download the data
response = requests.request("GET", url)

# parse the downloaded data
data = BeautifulSoup(response.text, 'lxml')
# print(type(data.find_all('p')))
# print(type(data.find('p').text))
parsed_dict = json.loads(data.find('p').text)
count = 0
max = 0
for tag in parsed_dict['tags']:
    if build in tag and tag.split(".")[0].isnumeric():
        # import pdb;pdb.set_trace()
        id = tag.split(".")[1]
        # For branch build
        if len(id) <= 2:
            if int(id) > max:
                max = int(id)
            # print(tag)
            # print(id)
            count += 1

# print("Count:", count)
print("Max:", max)

if path.exists("/home/nuthanc/build_numbers/loc_latest.py"):
    import loc_latest
    if (max > loc_latest.max and int(build) >= loc_latest.build) or (int(build) > loc_latest.build):
        # Do provisioning

        # For now send mail
        rc = call("/home/nuthanc/build_numbers/loc_send_mail.sh", shell=True)

with open("/home/nuthanc/build_numbers/loc_latest.py","w") as f:        
    f.write("build={}\n".format(build))
    f.write("max={}".format(max))
