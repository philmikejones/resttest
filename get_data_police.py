import requests

# Documentation from:
# https://data.police.uk/docs/method/crime-street/

# Example request with poly area:
# https://data.police.uk/api/crimes-street/all-crime?date=2024-01&lat=52.629729&lng=-1.131592

# Replace with your API endpoint
base_url = "https://data.police.uk/api/crimes-street/"
crime_type = "burglary"
# crime_type choices:
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

date = "2025-01"
lat = 53.1282
lng = -1.2677

query_url = base_url + crime_type + "?date=" + date + "&lat=" + str(lat) + "&lng=" + str(lng)

def get_resource():
    response = requests.get(query_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    result = get_resource()
    print(query_url)
