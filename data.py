import requests

params = {
    'amount': 10,
    'type': 'boolean'
}

r = requests.get('https://opentdb.com/api.php', params=params)
r.raise_for_status()
data = r.json()
question_data = data['results']
