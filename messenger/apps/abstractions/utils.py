import requests
import datetime


def get_current_time_by_city_name(city_name: str) -> datetime.datetime:
    URL: str = ('https://api.api-ninjas.com/v1/worldtime?'
                f'city={city_name}')
    headers = {'X-Api-Key': 'f7xVZFQ//LSeJ1ym1TGgSw==hlohz1xQ8LzSqXPc'}
    r: requests.Response = requests.get(url=URL, headers=headers)
    data = r.json()
    if data.get('error'):
        return
    time = datetime.datetime(
        year=int(data.get('year')),
        month=int(data.get('month')),
        day=int(data.get('day')),
        hour=int(data.get('hour')),
        minute=int(data.get('minute')),
        second=int(data.get('second')))
    return time
