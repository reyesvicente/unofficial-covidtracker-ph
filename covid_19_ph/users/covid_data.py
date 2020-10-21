import requests
import environ

env = environ.Env()

def get_data():
    DATA_URL = env("DATA_URL")
    headers = {'Accept': 'application/json'}
    r = requests.get(DATA_URL, headers=headers)
    stat = r.json()
    stat_data = {
      'stat': stat
    }
    return stat_data


def get_vaccine():
  VACCINE_URL = env("VACCINE_URL")
  headers = {'Accept': 'application/json'}
  request = requests.get(VACCINE_URL, headers=headers)
  vaccine = request.json()
  vaccine_data = {
    'vaccine': vaccine
  }
  return vaccine_data


def get_therapeutic():
  TP_URL = env("TP_URL")
  headers = {'Accept': 'application/json'}
  r = requests.get(TP_URL, headers=headers)
  therapeutic = r.json()
  tp_data = {
    'therapeutic': therapeutic
  }
  return tp_data


def get_news():
    NEWS_URL = env("NEWS_URL")
    querystring = {"safeSearch":"true","toPublishedDate":"null","fromPublishedDate":"null","withThumbnails":"true","pageSize":"10","q":"covid, covid vaccine trial, covid therapeutics","autoCorrect":"false","pageNumber":"1"}
    headers = {
      'x-rapidapi-host': env("API_HOST"),
      'x-rapidapi-key': env("API_KEY"),
    }
    r = requests.get(NEWS_URL, headers=headers, params=querystring)
    news = r.json()
    article_data = {
      'news': news,
    }
    return article_data