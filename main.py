import requests
import time


skada_data = {
    "regnr": "YXL327",
    "date": "2023-09-11"
}

login_data = {
    "username": USERNAME,
    "password": PASSWORD
}

# Logga in och hämta token, userinfo måste skickas som 'data'
response = requests.post("https://sensor-claims-api.azurewebsites.net/token", data = login_data)
if response.status_code == 200:
    token = response.json()["access_token"]
    print(response.json())
  
else:
    print(f"Failed to login with status code: {response.status_code}")
    exit()

# Skicka anrop med registreringsnummer och skadedatum, skickas som query parametrar. Header med "Bearer" och access token måste skickas med för authentication
response = requests.post("https://sensor-claims-api.azurewebsites.net/icq_cabas?regnr="+skada_data["regnr"]+"&date="+skada_data["date"], headers={"Authorization": f"Bearer {token}"})

if response.status_code == 200:
    response = response.json()
    print(response)
else:
    print(f"Request failed with code: {response.status_code}")
    exit()
