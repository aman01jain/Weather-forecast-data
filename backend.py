import requests

API_KEY = "0d78a3dd8435e0a7de068f8f18fe048e"

def get_data(place,forecast_day=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={place}&APPID={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data= data["list"]
    nr_values= 8*forecast_day
    filtered_data = filtered_data[:nr_values]
    if kind== "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind== "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_day=3,kind="Temperature"))