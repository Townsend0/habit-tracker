import requests
import datetime

json = {
    "x-app-id": "287c85c7",
    "x-app-key": "5a50f94763fb437309102af392c30a03",
    "Content-Type": "application/json"
}

json1 = {
    "query": input("What did you do today: "),
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 183,
    "age": 20
}

date = datetime.date.today()
time = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
a = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json = json1, headers=json)
sheet_inputs = {
        "sheet1": {
            "date": str(date),
            "time": str(time),
            "exercise": a.json()["exercises"][0]["user_input"],
            "duration": str(a.json()["exercises"][0]["duration_min"]),
            "calories": str(a.json()["exercises"][0]["nf_calories"]),
        }
    }
requests.post("https://api.sheety.co/e727c248aeb3c57bae687178bfc5a928/untitledSpreadsheet/sheet1", json = sheet_inputs, headers = { "Authorization Header": "Bearer Ksfaq137"})