from django.shortcuts import render
import requests

def weather(request):
    if request.method == "POST":
        city = request.POST.get('city')  # Use get method for safety
        if city:
            try:
                api_key = "0b5715c215784d31270e27840d556c1c"  # Replace with your actual API key
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for HTTP errors
                weather_data = response.json()

                data = {
                    "country_code": weather_data['sys']['country'],
                    "coordinate": f"{weather_data['coord']['lon']} {weather_data['coord']['lat']}",
                    "temp": f"{weather_data['main']['temp']}K",
                    "pressure": weather_data['main']['pressure'],
                    "humidity": weather_data['main']['humidity'],
                }
            except requests.exceptions.RequestException as e:
                data = {"error": f"An error occurred while retrieving weather data: {e}"}
        else:
            data = {"error": "City name not provided"}
    else:
        data = {}  # Empty data for initial page load

    return render(request, "weather.html", data)
