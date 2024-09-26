import requests

def fetch_quiz_questions():
    response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
    data = response.json()
    return data['results']
