from django.shortcuts import render
import requests

# Create your views here.
def weather(request):
    if request.method == "POST":
     city = request.POST['city']
     source ="http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=0b5715c215784d31270e27840d556c1c"
     try:
         list_of_data = requests.get(source).json()
         data = {
              "country_code": str(list_of_data['sys']['country']),
              "coordinate": str(list_of_data['coord']['lon']) + ' '
              + str(list_of_data['coord']['lat']),
              "temp": str(list_of_data['main']['temp']) + 'k',
              "pressure": str(list_of_data['main']['pressure']),
              "humidity": str(list_of_data['main']['humidity']),
         }
     except requests.exceptions.RequestException:
         data = {
              "error": "An error occurred while retrieving weather data."
         }
    else:
        data = {}
    return render(request, "weather.html", data)
