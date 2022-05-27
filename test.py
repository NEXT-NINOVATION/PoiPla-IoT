import sys
import requests
import json

url = "http://localhost:8080"

payload = json.dumps({
  "status": sys.argv[1]
})

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)