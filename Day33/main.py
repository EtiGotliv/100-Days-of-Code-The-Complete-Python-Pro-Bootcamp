import requests
from datetime import datetime
from time import sleep
import smtplib

MY_EMAIL = "etigotliv2134@gmail.com"
MY_PASSWORD = "password"  
TO_EMAIL = "etigotliv2134@gmail.com"
MY_LAT = 43.653225
MY_LONG = -79.383186

def iss_is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5

def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return time_now >= sunset or time_now <= sunrise

while True:
    time_now = datetime.now()  # עדכון השעה
    if is_night() and iss_is_above():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject: International Space Station Alert\n\nLook into the sky, you can see the ISS passing"
            )
        print("Email sent!")

    sleep(60)
