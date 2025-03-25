import requests, json, time, uuid, logging
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from kafka import KafkaProducer

default_args = {
    'owner': 'Brian',
    'start_date': datetime(2022, 3, 25, 12, 0)
}


def extract_data():
    resp = requests.get("https://randomuser.me/api/")
    resp = resp.json()
    resp = resp['results'][0]

    return resp


def format_data(resp):
    data = {}
    location = resp['location']
    data['id'] = uuid.uuid4()
    data['first_name'] = resp['name']['first']
    data['last_name'] = resp['name']['last']
    data['gender'] = resp['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = resp['email']
    data['username'] = resp['login']['username']
    data['dob'] = resp['dob']['date']
    data['registered_date'] = resp['registered']['date']
    data['phone'] = resp['phone']
    data['picture'] = resp['picture']['medium']
    data['nationality'] = resp['nat']

    return data



def stream_data():
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: # 1 minute
            break
        try:
            resp = extract_data()
            resp = format_data(resp)

            producer.send('users_created', json.dumps(resp).encode('utf-8'))
        except Exception as e:
            logging.error(f"An Error Occurred: {e}")
            continue


with DAG('user_automation', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    stream_data_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )