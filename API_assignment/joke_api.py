import requests

apiurl = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(apiurl)
    if response.status_code==200:
        apiresult = response.json()
        print(apiresult['value'])
except requests.exceptions.RequestException as e:
    print ("Something went wrong!Please try again.")
