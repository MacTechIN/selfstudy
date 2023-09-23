# http://openapi.gbis.go.kr/ws/rest/busrouteservice?serviceKey=1234567890&keyword=11
# return value :  String routeName:노선 번호
#Rest 접속 xml값받아오기 


import pandas as pd
import requests 
from bs4 import BeautifulSoup 
import xmltodict 
import json
import xml.etree.ElementTree as et 



bus_no = 112

# REST용 url 만들기 
service_url = "http://apis.data.go.kr/6410000/busrouteservice"
service_name = "/getBusRouteList?"
encoding_key = "%2BltohkyQC0eQUMVVaH5qwUi4FxaROssy0kpwzEdkqsFqedo%2FKlvT05Ap0svSUr2xQsOHd9%2FK2pXWpnH5N%2BmTcg%3D%3D" 
serviceKey = "serviceKey="+encoding_key 
keyword = f"&keyword={bus_no}"

#final_url 확인 
final_url = service_url + service_name + serviceKey + keyword
#디버깅용 

#print(final_url)

def find_route_Id (final_url):
    bus_info_xml = requests.get(final_url)
    bus_route_df = make_df(xtod(bus_info_xml))
    return set_suwon_bus(bus_route_df)[0]

def xtod(xml_data):
    #contents 분리 
    content = xml_data.content 
    #dictionary 볂환 
    bus_route_dic = xmltodict.parse(content)
    return bus_route_dic

def make_df(dic_obj):
    jsonString = json.dumps(dic_obj['response']['msgBody']['busRouteList'])
    json_object = json.loads(jsonString)
    df = pd.DataFrame(json_object)
    return df 

def set_suwon_bus(df):
    is_Suwon_bus = df['regionName'] == '수원'
    route_Id_df = df[is_Suwon_bus]['routeId']
    return route_Id_df


print(find_route_Id(final_url))