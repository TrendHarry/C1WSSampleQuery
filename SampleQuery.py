import requests
import json
import zipfile
import os


endpoints = ["contacts", "computers", "roles", "policies", "certificates", "systemsettings","antimalwareconfigurations","directorylists","fileextensionlists","filelists","computergroups","computers?overrides=true","intrusionpreventionrules"]



region = input("Enter your region: ")
api_key = input("Enter your C1 API key: ")   


files = []


for endpoint in endpoints:
    url = f"https://workload.{region}.cloudone.trendmicro.com/api/{endpoint}"
    headers = {
        'Authorization': f'ApiKey {api_key}',
        'api-version': 'v1',
        'Content-Type': 'application/json',
    }
    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        filename = f"{endpoint.replace('?','_')}.json"
        files.append(filename)

        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"File '{filename}' created.")
    else:
        print(f"Request to {url} failed with status code {response.status_code}.")


with zipfile.ZipFile('Data.zip', 'w') as zipf:
    for file in files:
        zipf.write(file)
    print("All files zipped successfully!") 

for file in files:
    os.remove(file)
