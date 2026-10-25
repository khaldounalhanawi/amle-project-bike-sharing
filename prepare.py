def prepare(data):
    """All manual changes to the data, collected in one place."""
    data = data.copy()
    dt = data["datetime"]

    # 1. the hour 02:00 on the second Sunday of March does not exist (clocks go forward)
    nonexistent = (dt.dt.month == 3) & (dt.dt.dayofweek == 6) & dt.dt.day.between(8, 14) & (dt.dt.hour == 2)
    data = data[~nonexistent]
    dt = data["datetime"]

    # 2. calendar features
    data["hour"] = dt.dt.hour
    data["weekday"] = dt.dt.dayofweek
    data["month"] = dt.dt.month
    data["year"] = dt.dt.year

    # 3. + 4. flags for holidays and working days
    data["is_holiday"] = data["holiday"].notna().astype(int)
    data["is_working_day"] = ((data["weekday"] < 5) & (data["is_holiday"] == 0)).astype(int)

    # 5. drop replaced, redundant and leaking columns
    return data.drop(columns=["holiday", "feels_like", "weather_code", "casual", "member"])