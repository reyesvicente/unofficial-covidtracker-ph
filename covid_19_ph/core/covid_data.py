import requests


def get_data():
    url = "https://disease.sh/v3/covid-19/countries/PH"
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    stat = r.json()
    stat_data = {
      'stat': stat
    }
    return stat_data