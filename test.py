import sys
import requests
import json

url = "https://poipla.yumekiti.net/api/iot/dust-box-pushes"

payload = json.dumps({
 "token": "hoge"
})

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)