import requests
import time
def fetch_quiz_questions():
    response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
    data = response.json()
    time.sleep(1)
    return data['results']
