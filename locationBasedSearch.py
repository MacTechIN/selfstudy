import requests, json
import pandas as pd
import time

key = "KakaoAK b958bdf89a2ea48dc1e8c2792f0483f7"
myAdd = "경기도 수원시 권선구 세권로108번길 10"


def get_xy_postion(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": key}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    res = api_json['documents']
    res_dict = res[0]
    json_str = json.dumps(res_dict['road_address'])


get_xy(json_str)


def get_xy(json_str):
    json_obj = json.loads(json_str)
    print(f"Latitude : {json_obj['x']} Longitude :{json_obj['y']}")
    return json_obj['x'], json_obj['y']


# %%

# res = get_location(myAdd)['documents']

print(res)
print(type(res))  # <class 'list'>
print(type(res[0]))  # <class 'dict'>

# %%

res_dict = res[0]

print(res_dict)

# %%

json_str = json.dumps(res_dict['road_address'])


def get_xy(json_str):
    json_obj = json.loads(json_str)
    print(f"Latitude : {json_obj['x']} Longitude :{json_obj['y']}")
    return json_obj['x'], json_obj['y']


print(get_xy(json_str))
