import requests
import json
import pandas as pd
from io import StringIO  # for reading json strings into pandas

## Documentation from:
# https://data.police.uk/docs/method/crime-street/
# Build a query with:
# base_url + crime_type + date + coords
# It will return all crimes for the given month within a 1 mile radius of the coords


## Date
def get_api_date() -> str:
    """
    Obtains the date of the latest API data
    
    Returns:
    str A date in the format YYYY-MM
    """
    date_url = "https://data.police.uk/api/crime-last-updated"
    response = requests.get(date_url)
    if response.status_code != 200:
        api_error = f"Error in get_api_date(): {response.status_code} - {response.text}"
        return api_error
    response = response.json().get('date')
    response = response[:7]  # YYYY-MM-DD is returned but it expects YYYY-MM
    return response

## crime types
## https://data.police.uk/api/crime-categories?date=2024-01
# all-crime
# anti-social-behaviour
# bicycle-theft
# burglary
# criminal-damage-arson
# drugs
# other-theft
# possession-of-weapons
# public-order
# robbery
# shoplifting
# theft-from-the-person
# vehicle-crime
# violent-crime
# other-crime


def get_records(date, crime_type = "burglary", lat = 53.1282, lng = -1.2677):
    """
    Downloads the requested records from the data.police.uk API
    Defaults to burglaries in the treatment area for the latest month

    Returns:
    str A string with the json text from the API
    """
    base_url = "https://data.police.uk/api/crimes-street/"
    query_url = base_url + crime_type + "?date=" + date + "&lat=" + str(lat) + "&lng=" + str(lng)
    response = requests.get(query_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    latest_date = get_api_date()
    print(latest_date)

    burglaries = get_records(date = latest_date)
    burglaries = json.dumps(burglaries)  # converts ' to " for correct json
    burglaries = pd.read_json(StringIO(burglaries))
    print(burglaries)
