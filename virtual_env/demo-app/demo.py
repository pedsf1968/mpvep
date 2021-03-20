# import requests package
import requests

# Send request GET to www.example.com
r= requests.get('http://www.example.com')

# Display request status return
print(r.status_code)
print(r.text)