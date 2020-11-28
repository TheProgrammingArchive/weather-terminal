if __name__ == '__main__':
    from weather_today import weatherHourly
    from weather_tenday import weatherTenDay
    from dropdown import get_tendayweather
    weather_hourly = weatherHourly()
    weather_tenday = weatherTenDay()
    weather_hourly.getHourlyweather()
    weather_hourly.getdateofreport()
    weather_hourly.weather_atThisHour()

else:
    raise ImportError
    exit(1)
