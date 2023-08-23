import csv
import json

import requests

# encoding_key = 'EtszyX5rgdQCBVMcXDPLcuk%2FGESQ0GRPuVB9ydqZelRwNSm8F1BIajAX%2FFCV0qt00CBEieOv7LuoqAkwjKuTCg%3D%3D'
decoding_key = 'EtszyX5rgdQCBVMcXDPLcuk/GESQ0GRPuVB9ydqZelRwNSm8F1BIajAX/FCV0qt00CBEieOv7LuoqAkwjKuTCg=='

def get_find_dust(region='서울'):
    url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc'
    params = {
        'serviceKey': decoding_key,
        'returnType': 'json',
        'numOfRows': '100',
        'pageNo': '1',
        'sidoName': region,
        'ver': '1.0',
    }
    response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty', params=params)
    data = json.loads(response.text)
    print("시/도명, 동/구명, 미세먼지 수치, 미세먼지 등급, 측정시간")
    result = [['시/도명', '동/구명', '미세먼지 수치', '미세먼지 등급', '측정시간']]
    for info in data['response']['body']['items']:
        print(f"{info['sidoName']}, {info['stationName']}, {info['pm25Value']}, {info['pm25Grade']},{info['dataTime']}")
        result.append([info['sidoName'], info['stationName'], info['pm25Value'], info['pm25Grade'], info['dataTime']])
    with open('airinfo.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(result)

get_find_dust('서울')
# get_find_dust('강원')