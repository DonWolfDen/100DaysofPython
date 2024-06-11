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


user_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_END, json=user_parameters)
# print(response.text)


graph_config = {
    "id": coding_graph_id,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}
# response = requests.post(url=PIXELA_GRAPHS_END, headers=headers, json=graph_config)
# print(response.text)


now = datetime.now()
coding_params = {
    "date": now.strftime("%Y%m%d"),
    "quantity": input("How many hours did you spend coding today? ")
}
response = requests.post(url=coding_graph_end, headers=header, json=coding_params)
print(response.text)


put_params = {
    "quantity": "1"
}
# response = requests.put(url=f"{coding_graph_end}/20220628", headers=header, json=put_params)
# print(response.text)

# response = requests.delete(f"{coding_graph_end}/20220628", headers=header)
# print(response.text)


