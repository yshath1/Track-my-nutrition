import requests
from datetime import datetime
import os
APP_ID="App_id"
API_KEY="Api_key"
today=datetime.now()
NUTRITIONIX_EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS={
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
    'content-type':'application/json'
}
today_str=today.strftime("%d/%m/%Y")
time_str=today.time().strftime("%H:%M:%S")
query={
 "query":"i did tabata for 30mins and qingong for 10mins",
 "gender":"male",
 "weight_kg":"72.5",
 "height_cm":"167.64",
 "age":"33"
}
response=requests.post(NUTRITIONIX_EXERCISE_ENDPOINT,headers=HEADERS,json=query)
data=response.json()
exercise=data['exercises'][0]['user_input']
duration=int(data['exercises'][0]['duration_min'])
calories=int(data['exercises'][0]['nf_calories'])
headers={
    'Authorization':'Basic c2hha2EyMDIyOmNoaWxkb2Znb2Qx'
}
sheety_ENDPOINT="https://api.sheety.co/c06c8c81a5ea4e26088b5a1502f4e049/myWorkouts/workouts"
data_post={'workout':{
    'date':today_str,
    'time':time_str,
    'exercise':exercise,
    'duration':duration,
    'calories':130,
    'id':2
}
}
# res=requests.get(sheety_ENDPOINT)
# sheety_data=res.json()
# print(sheety_data)

respond=requests.post(url=sheety_ENDPOINT,json=data_post,headers=headers)
print(respond.text)
