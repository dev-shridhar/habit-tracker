import requests
from datetime import datetime

date = datetime.now()


pixela_endpoint ="https://pixe.la/v1/users"
TOKEN ="token"
USER_NAME ="your user name"
GRAPH_ID = "yur graph id"
user_params ={
    "token" : TOKEN,
    "username" : USER_NAME ,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config ={
    "id":GRAPH_ID,
    "name":"Coding graph",
    "unit":"Hour",
    "type":"int",
    "color":"sora"
}

headers={
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(graph_response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

pixela_data={
    "date":date.strftime("%Y%m%d"),
    "quantity":"5",

}


update_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20211017"

new_pixel_data ={
    "quantity":"5"
}

response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
print(response.text)

delet_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20200922"
delet_pixel = requests.delete(url=delet_endpoint,headers=headers)
