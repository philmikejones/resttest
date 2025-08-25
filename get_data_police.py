import requests
import json

## Documentation from:
## https://data.police.uk/docs/method/crime-street/
## Build a query with:
## base_url + crime_type + date + coords
## It will return all crimes for the given month within a 1 mile radius of the coords

base_url = "https://data.police.uk/api/crimes-street/"

## crime_type choices:
## uses `all-crime` by default unless specified
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

## Date
## Specify a date in the format YYYY-MM
## By default uses most recent month data is available for

def get_api_date() -> str:
    date_url = "https://data.police.uk/api/crime-last-updated"
    response = requests.get(date_url)
    if response.status_code != 200:
        api_error = f"Error in get_api_date(): {response.status_code} - {response.text}"
        return api_error
    response = response.json()
    return response

def truncate_day(date_str):
    # Assumes input format is 'YYYY-MM-DD'
    return date_str[:7]


# Example request with poly area:
# https://data.police.uk/api/crimes-street/all-crime?date=2024-01&lat=52.629729&lng=-1.131592



#lat = 53.1282
#lng = -1.2677
#
#query_url = base_url + crime_type + "?date=" + date + "&lat=" + str(lat) + "&lng=" + str(lng)

def get_resource():
    response = requests.get(query_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    date = get_api_date()
    print(date)
