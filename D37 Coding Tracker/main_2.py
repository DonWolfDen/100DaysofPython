import requests
from datetime import datetime
import os

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
PIXELA_END = os.environ.get("PIXELA_END")
PIXELA_GRAPHS_END = os.environ.get("PIXELA_GRAPHS_END")

coding_graph_id = "graph2"
coding_graph_end = f"{PIXELA_GRAPHS_END}/{coding_graph_id}"

header = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

now = datetime.now()
coding_params = {
    "date": now.strftime("%Y%m%d"),
    "quantity": input("How many hours did you spend coding today? ")
}
response = requests.post(url=coding_graph_end, headers=header, json=coding_params)
print(response.text)
