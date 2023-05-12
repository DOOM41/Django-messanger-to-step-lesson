import requests
import datetime

from settings.base import API_TOKEN


def get_current_time_or_none_by_city_name(city_name: str) -> datetime.datetime:
    URL: str = ('https://api.api-ninjas.com/v1/worldtime?'
                f'city={city_name}')
    headers: dict[str, str] = {'X-Api-Key': API_TOKEN}
    r: requests.Response = requests.get(url=URL, headers=headers)
    # Check if response status code is 200
    status: int = r.status_code
    if status != 200:
        return None
    # Get data from response and check if there any errors
    data: dict = r.json()
    if data.get('error'):
        return None
    # Create datetime variable to return
    time: datetime.datetime = datetime.datetime(
        year=int(data.get('year')),
        month=int(data.get('month')),
        day=int(data.get('day')),
        hour=int(data.get('hour')),
        minute=int(data.get('minute')),
        second=int(data.get('second'))
    )
    return time
