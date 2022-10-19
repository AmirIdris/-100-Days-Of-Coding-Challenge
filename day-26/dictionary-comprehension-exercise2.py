weather_c = {
    "Monday":12,
    "Tuesday":20,
    "Wednesday":25,
    "Thursday":30,
    "Friday":35,
    "Saturday":40,
    "Sunday":45
}

weather_f = {day:(temp_c*9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)

