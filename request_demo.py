import requests
import json
headers = {'user-agent': 'my-app/0.0.1'}
req =  requests.get('https://httpbin.org/status/404',headers=headers)
# print(req.status_code)
# print(req.raise_for_status())
# print(req.headers['CONTENT-TYPE'])
# print(req.url)
# print(req.content)
print (json.dump(req.headers))

