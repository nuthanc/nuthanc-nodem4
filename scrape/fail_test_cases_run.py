import requests
import re
import os
import subprocess
subprocess.run(["pip3", "install", "bs4"])
from bs4 import BeautifulSoup

#variables

# target URL to scrap
# url = input("Enter url to scrape tc: ") 
url = "http://10.204.216.50/Docs/logs/2005-3_2020_04_25_18_22_59_1587848768.469263/junit-noframes.html"
# http://10.204.216.50/Docs/logs/2005-3_2020_04_25_18_22_59_1587848768.469263/junit-noframes.html

# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(response.text, 'html.parser')
# print(data.find("tr",{"class":"Error"}).prettify()) 
error_tc = data.find_all("tr", {"class": "Error"})
print(len(error_tc))

tc_list = []

for case in data.find_all("tr", {"class": "Error"}):
    failed_methods = (case.find('td').text).split("[")[0]
    tc_list.append(failed_methods)
    print(failed_methods)

print("\nLocation of test cases\n")
test_cases = set()


for code in data.find_all("code"):
    cases = re.findall(r'/contrail-test/s.*py',code.text)
    for case in cases:
        test_cases.add(case)
        
for tc in test_cases:
    print(tc)
print()

file_list = []
for file_path in test_cases:
    f = file_path.split("contrail-test/")[1].split(".py")[0]
    f = f.replace("/",".")
    file_list.append(f)

failed_test_cases = []
for i,f in enumerate(file_list):
  tc = f + "." + tc_list[i]
  failed_test_cases.append(tc)

print(failed_test_cases)
    
for tc in failed_test_cases:
    os.system(f"python -m subunit.run {tc}")
