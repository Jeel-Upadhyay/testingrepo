import requests


city = input("Enter City name: ")
apikey = 'e11a324afa430c2c9f45e9f32ee58bc'
apiurl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}9&units=metric"

try:
    response = requests.get(apiurl)
    if response.status_code==200:
        apiresult = response.json()
        weather_description = apiresult["weather"][0]["description"]
        temperature = apiresult["main"]["temp"]

        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature} °C")
        # print(apiresult)
except requests.exceptions.RequestException as e:
    print ("Something went wrong!Please try again.")