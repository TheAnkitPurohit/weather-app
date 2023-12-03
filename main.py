from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env
load_dotenv()

api_key = os.environ.get("API_KEY")

city = input("Enter the name of city: ")

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": city}

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

res = response.json()

current_temperature_celsius = res['current']['temp_c']

weather = f"Say Current Temperature in  {city} is  {current_temperature_celsius} degree celcius"
os.system(weather)



