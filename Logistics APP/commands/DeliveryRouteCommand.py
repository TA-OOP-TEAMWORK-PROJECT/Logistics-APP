import datetime
current_datetime = datetime.datetime.now()
tomorrow_date = current_datetime + datetime.timedelta(days=1)
date_time_tommorow = datetime(tomorrow_date.month, tomorrow_date.day, 6, 0)


average_speed_kmh = 87
travel_time = datetime.timedelta(hours=1376 / average_speed_kmh)
current_time = date_time_tommorow + travel_time
print(current_time)


