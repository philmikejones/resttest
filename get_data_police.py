import requests

## Documentation from:
# https://data.police.uk/docs/method/crime-street/
# Build a query with:
# base_url + crime_type + date + coords
# It will return all crimes for the given month within a 1 mile radius of the coords

base_url = "https://data.police.uk/api/crimes-street/"

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
