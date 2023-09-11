import requests
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv
import os

load_dotenv()

repo = os.getenv("REPO","apache/airflow")
dbname = os.getenv("PG_DB", "app")
user = os.getenv("PG_USER", "postgres")
password = os.getenv("PG_PW", "example")
dbhost = os.environ.get("PG_HOST","localhost")


query = {
    'per_page': 100,
    'page': 1,
    "since": "2023-03-01"
}
url = 'https://api.github.com/repos/{}/commits'.format(repo)
data = []
response = requests.get(url, params=query)
while response.ok and len(response.json()) > 0:
    commits = response.json()
    for commit in commits:
        data.append((commit["sha"], commit["commit"]["author"]["name"], commit["commit"]["author"]["date"], commit["commit"]["message"]))
    query["page"] += 1
    response = requests.get(url,params=query)


cols = "id,author,datetime,message"
insertquery = "INSERT INTO stocks (%s) VALUES %%s ON CONFLICT DO NOTHING" %cols
with psycopg2.connect(dbname=dbname, user=user, password=password, host=dbhost) as conn:
    with conn.cursor() as curs:
        cols = "id, author, datetime, message"
        insertquery = "INSERT INTO app.ft_commits (%s) VALUES %%s ON CONFLICT DO NOTHING" %cols
        extras.execute_values(curs,insertquery,data)
    conn.commit()