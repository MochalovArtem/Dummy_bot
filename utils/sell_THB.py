import requests

cookies = {
    'deviceId': 'f9d74070-a9dc-c3fb-1417-562591909a86',
    '_by_l_g_d': 'f99cf85e-9599-b9a4-ddca-56aba306992b',
    'sajssdk_2015_cross_new_user': '1',
    'b_t_c_k': '',
    '_gcl_au': '1.1.1734450553.1700642245',
    '_ga': 'GA1.1.808882825.1700642247',
    '_ym_uid': '170064224745076190',
    '_ym_d': '1700642247',
    '_ym_isad': '2',
    'BYBIT_REG_REF_prod': '{"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.google.com/","source":"google.com","medium":"other","url":"https://www.bybit.com/ru-RU/help-center/article/How-to-retrieve-API-documentations"}',
    'BYBIT_REG_REF_local': '{"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=","source":"bybit.com","medium":"other","url":"https://www.bybit.com/future-activity/ru-RU/developer"}',
    '_abck': '93FE6D3509D0256B419F0D67D48112A0~0~YAAQL5bvUK1wsc6LAQAA/FtO9wojuenbcpyyF+dXNKBXsK6zX1YHde+AGyirzh3rIaSHwk0vO6e6ryygtUsGoiosN0FStdqPszTJfoSu2kTAgxDQL/eCu6U5Pqp/XCF3kUsFmrxSAc85TDU0Pl8l9eXJ9eLx9uzk3NqO+NP+vchyHSocSeBqerx5ziC3geOY/RyX2ZUSfDT7JrXwwyAmMiTs4+Vy5xC7/3S5S5V+FsjDpr/07Hz7RoWnDFysHk0+i1Rf2Cc6HMPXk401vd3HleX5nTekLi2VSYsWW00LLEb4+ocUomuJ924eFnt9nb7ntHf4wx/ngnM3CfvcxwXWVbM0T+FAjwKdTTydjQEWO2xava6U9qwReFPUzYkizavd3lHt6pX5pRQVA50xA5XHikVtZ3JvZE4=~-1~-1~-1',
    'bm_sz': '8E0FF7387E61F3058DF3F2266B8AED98~YAAQL5bvULBwsc6LAQAA/FtO9xV/f2LJWrkklSi8r+S2W9/s+zp2Vxct1RNpKLeIxLqI2mVggAMWT1zuqOxPpLPrl+8q/0BGk9DtCs+2GSAcIH7AOAtSI3FVFqVpDBpVF317NjDw3Aa0Po/6qrp9FWtmFxmPBLoAVLJ0380jKUJI6Qv7OgRRjzBlbeJies5nMdTYOrcTTUJEr2Wx9qFmK6Z4U3J1FvcQ6SHCSjSCRV+O98U3epWfyhOmBlhu/7E67Lv5hO7CBVSPoVdV9f6RXkjr3NOD9nWHLkMFt4SYji0YSw==~3162436~3486532',
    'detection_time': '1700697600000',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_a_u_v%22%3A%220.0.5%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiZjYyZDMzMTAzN2QtMDg3NDJhNmJiY2RiNjg4LTI2MDMxMDUxLTIwNzM2MDAtMThiZjYyZDMzMTFjYmYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%7D',
    'ak_bmsc': 'EBC8AB23A69D2BF5F07ED5F0294FEB54~000000000000000000000000000000~YAAQVoVlX195I92LAQAAMbjO9xW3p48xVWJmkHjPIRMtvYoWfmX06vexdNYqz1e3Om1jsKk26BxYAY8pYwxeT7mflQHrB5lxnh6iwshDY086typaXKPaHzc16hsSxUuJCuCCoazMz/ddOM2LRp8EnJYxlOJqQ+Aaw/SJndwMxmOQ8VOGKkdStw47ZfdUPwWGihy/nC4vrtFfqfajyd9zdqcBeBr7ENxZBMCMZufXEUKdwBlnZ4Jre6JHxMQCV0/kSRXCH0U+XF6YBzVod3j++fsTNVcmxcF4BK+P53qnfZr7LTBgf6UbmIAQE3k4x7ReMmyb2lgmpXMPzXLu2gtN5z6fK0mZa+/jFogwCjMP39KB/I8Pst9QgBaaEjTw303hHb9p0cGe1nSo',
    'bm_sv': '241ACFD52F4DEBDDFBED0ACD75FF9373~YAAQVoVlX4Z5I92LAQAAJrvO9xUDLId92gtMnsbbe/xz4Kg57a7ohnpAITNtbQTpLntQVpavxck31zoe92E5fqqCO0MHT0/gewOa8AKdhCctm8WjZhP9Rv6U45IhRL2bWq0h3S3xHiKREbFpaowpzN3BVpoGDguAz88oXthmajj6kyAddxkA8f/AkSyOikTeTcMbaCQB4y6rHJVIqMTQ5ja8SOV+M0J8AMfEqceS/ihRdcnMlE4SIoytN3Lk6QQ=~1',
    '_ga_SPS4ND2MGC': 'GS1.1.1700661188.2.1.1700669603.60.0.0',
}

headers = {
    'authority': 'api2.bybit.com',
    'accept': 'application/json',
    'accept-language': 'ru-RU',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'deviceId=f9d74070-a9dc-c3fb-1417-562591909a86; _by_l_g_d=f99cf85e-9599-b9a4-ddca-56aba306992b; sajssdk_2015_cross_new_user=1; b_t_c_k=; _gcl_au=1.1.1734450553.1700642245; _ga=GA1.1.808882825.1700642247; _ym_uid=170064224745076190; _ym_d=1700642247; _ym_isad=2; BYBIT_REG_REF_prod={"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.google.com/","source":"google.com","medium":"other","url":"https://www.bybit.com/ru-RU/help-center/article/How-to-retrieve-API-documentations"}; BYBIT_REG_REF_local={"lang":"ru-RU","g":"f99cf85e-9599-b9a4-ddca-56aba306992b","referrer":"www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=","source":"bybit.com","medium":"other","url":"https://www.bybit.com/future-activity/ru-RU/developer"}; _abck=93FE6D3509D0256B419F0D67D48112A0~0~YAAQL5bvUK1wsc6LAQAA/FtO9wojuenbcpyyF+dXNKBXsK6zX1YHde+AGyirzh3rIaSHwk0vO6e6ryygtUsGoiosN0FStdqPszTJfoSu2kTAgxDQL/eCu6U5Pqp/XCF3kUsFmrxSAc85TDU0Pl8l9eXJ9eLx9uzk3NqO+NP+vchyHSocSeBqerx5ziC3geOY/RyX2ZUSfDT7JrXwwyAmMiTs4+Vy5xC7/3S5S5V+FsjDpr/07Hz7RoWnDFysHk0+i1Rf2Cc6HMPXk401vd3HleX5nTekLi2VSYsWW00LLEb4+ocUomuJ924eFnt9nb7ntHf4wx/ngnM3CfvcxwXWVbM0T+FAjwKdTTydjQEWO2xava6U9qwReFPUzYkizavd3lHt6pX5pRQVA50xA5XHikVtZ3JvZE4=~-1~-1~-1; bm_sz=8E0FF7387E61F3058DF3F2266B8AED98~YAAQL5bvULBwsc6LAQAA/FtO9xV/f2LJWrkklSi8r+S2W9/s+zp2Vxct1RNpKLeIxLqI2mVggAMWT1zuqOxPpLPrl+8q/0BGk9DtCs+2GSAcIH7AOAtSI3FVFqVpDBpVF317NjDw3Aa0Po/6qrp9FWtmFxmPBLoAVLJ0380jKUJI6Qv7OgRRjzBlbeJies5nMdTYOrcTTUJEr2Wx9qFmK6Z4U3J1FvcQ6SHCSjSCRV+O98U3epWfyhOmBlhu/7E67Lv5hO7CBVSPoVdV9f6RXkjr3NOD9nWHLkMFt4SYji0YSw==~3162436~3486532; detection_time=1700697600000; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_a_u_v%22%3A%220.0.5%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiZjYyZDMzMTAzN2QtMDg3NDJhNmJiY2RiNjg4LTI2MDMxMDUxLTIwNzM2MDAtMThiZjYyZDMzMTFjYmYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218bf62d331037d-08742a6bbcdb688-26031051-2073600-18bf62d3311cbf%22%7D; ak_bmsc=EBC8AB23A69D2BF5F07ED5F0294FEB54~000000000000000000000000000000~YAAQVoVlX195I92LAQAAMbjO9xW3p48xVWJmkHjPIRMtvYoWfmX06vexdNYqz1e3Om1jsKk26BxYAY8pYwxeT7mflQHrB5lxnh6iwshDY086typaXKPaHzc16hsSxUuJCuCCoazMz/ddOM2LRp8EnJYxlOJqQ+Aaw/SJndwMxmOQ8VOGKkdStw47ZfdUPwWGihy/nC4vrtFfqfajyd9zdqcBeBr7ENxZBMCMZufXEUKdwBlnZ4Jre6JHxMQCV0/kSRXCH0U+XF6YBzVod3j++fsTNVcmxcF4BK+P53qnfZr7LTBgf6UbmIAQE3k4x7ReMmyb2lgmpXMPzXLu2gtN5z6fK0mZa+/jFogwCjMP39KB/I8Pst9QgBaaEjTw303hHb9p0cGe1nSo; bm_sv=241ACFD52F4DEBDDFBED0ACD75FF9373~YAAQVoVlX4Z5I92LAQAAJrvO9xUDLId92gtMnsbbe/xz4Kg57a7ohnpAITNtbQTpLntQVpavxck31zoe92E5fqqCO0MHT0/gewOa8AKdhCctm8WjZhP9Rv6U45IhRL2bWq0h3S3xHiKREbFpaowpzN3BVpoGDguAz88oXthmajj6kyAddxkA8f/AkSyOikTeTcMbaCQB4y6rHJVIqMTQ5ja8SOV+M0J8AMfEqceS/ihRdcnMlE4SIoytN3Lk6QQ=~1; _ga_SPS4ND2MGC=GS1.1.1700661188.2.1.1700669603.60.0.0',
    'guid': 'f99cf85e-9599-b9a4-ddca-56aba306992b',
    'lang': 'ru-RU',
    'origin': 'https://www.bybit.com',
    'platform': 'PC',
    'pragma': 'no-cache',
    'referer': 'https://www.bybit.com/',
    'risktoken': 'dmVyMQ|NjAwZDlkNGVkMW0wNjBhYmY3ZnJ5c2trdGllYmQwZDEwNDFkMjc=||v2:gRoGuBbUmiOm0VgAobZitOkCR5ZecJ6nRVXAufnV0Ati6vsajdxYo8yp8ZoxvZmCR9knBtkL3Xq6z7yNBXFID/fza7YdhCFTdA7vpJHHmtULiIvwr/oXG+8aaaPNptga0UehUrydKfKl+bAbY2qg9a/y7Qaooo/gpyjNg2fHlsinDPjjY5nP86/mluqhrf8Ad4FhZkX9c1wWIcTqQHOwdpLrTmoHDIZG0LilquzqmA==',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'traceparent': '00-9563f40794b6fb1f40821f1529ad5a08-478d7a5d936aeab8-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

json_data = {
    'userId': '',
    'tokenId': 'USDT',
    'currencyId': 'THB',
    'payment': [],
    'side': '0',
    'size': '10',
    'page': '1',
    'amount': '',
    'authMaker': False,
    'canTrade': False,
}


def get_sell_thb():
    s = requests.Session()
    response = s.post('https://api2.bybit.com/fiat/otc/item/online', cookies=cookies, headers=headers, json=json_data)
    return response.json()


if __name__ == '__main__':
    get_sell_thb()
