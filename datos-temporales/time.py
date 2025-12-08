from datetime import datetime, date, time, timedelta

dt = datetime.now()

print(dt)
print(type(dt))
print(dt.year)
print(dt.month)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.tzinfo) # zona horaria, nula por defecto
print(dt.time())

dt = datetime(2022, 7, 11, 15, 7, 6)
print(dt)

dt = dt.isoformat()
print(dt)